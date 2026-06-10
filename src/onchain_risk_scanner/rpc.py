from __future__ import annotations

import json
import urllib.error
import urllib.request
from dataclasses import dataclass
from typing import Any


class RpcError(RuntimeError):
    pass


@dataclass
class JsonRpcClient:
    url: str
    timeout: float = 20.0
    _request_id: int = 0

    def call(self, method: str, params: list[Any]) -> Any:
        self._request_id += 1
        payload = {
            "jsonrpc": "2.0",
            "id": self._request_id,
            "method": method,
            "params": params,
        }
        request = urllib.request.Request(
            self.url,
            data=json.dumps(payload).encode("utf-8"),
            headers={
                "content-type": "application/json",
                "user-agent": "onchain-risk-scanner/0.1",
            },
            method="POST",
        )
        try:
            with urllib.request.urlopen(request, timeout=self.timeout) as response:
                body = json.loads(response.read().decode("utf-8"))
        except urllib.error.URLError as exc:
            raise RpcError(f"RPC request failed: {exc}") from exc
        except json.JSONDecodeError as exc:
            raise RpcError("RPC returned invalid JSON") from exc

        if "error" in body:
            message = body["error"].get("message", body["error"])
            raise RpcError(f"RPC error for {method}: {message}")
        return body.get("result")

    def get_code(self, address: str, block: str = "latest") -> str:
        return self.call("eth_getCode", [address, block])

    def get_balance(self, address: str, block: str = "latest") -> int:
        raw = self.call("eth_getBalance", [address, block])
        return int(raw, 16)

    def get_storage_at(self, address: str, slot: str, block: str = "latest") -> str:
        return self.call("eth_getStorageAt", [address, slot, block])
