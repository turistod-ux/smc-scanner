"""
SMC X Binance Gateway
Единая точка взаимодействия с Binance.
"""

from dataclasses import dataclass
from typing import Optional

from binance.client import Client


@dataclass
class GatewayStatus:
    connected: bool = False
    server_time: Optional[int] = None
    api_weight: int = 0


class BinanceGateway:

    def __init__(self, api_key: str = "", api_secret: str = ""):
        self.client = Client(api_key, api_secret)
        self.status = GatewayStatus()

    def ping(self):
        self.client.ping()
        self.status.connected = True
        return self.status

    def server_time(self):
        self.status.server_time = self.client.get_server_time()["serverTime"]
        return self.status.server_time


if __name__ == "__main__":
    gateway = BinanceGateway()
    print(gateway.ping())
    print(gateway.server_time())
