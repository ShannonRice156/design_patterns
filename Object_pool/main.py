"""A module to show an example of the object pool design pattern"""

from dataclasses import dataclass
import time


@dataclass
class pool():
    """A class which represents a pool which executes a request"""
    _request: str = ""
    _communicating: bool = False
    _start_time: int = 0

    def communicating(self) -> bool:
        """Polls self and returns a boolean that represents whether communication is still occurring"""
        self.poll()
        return self._communicating

    def send_request(self, request: str) -> None:
        """Send the request and sets communication variable"""
        print(request)
        self._request = request
        self._communicating = True
        self._start_time = time.time()

    def poll(self) -> None:
        """Poll the request to see if communication is still occurring"""
        if (time.time() - self._start_time) < 20000:
            self._communicating = False
            self._request = ""


def main():
    """The main function which executes the object pool design pattern"""

    pools = [pool(), pool(), pool(), pool(), pool(), pool()]
    x = 0
    while x < 30:
        for p in pools:
            p.poll()

        for p in pools:
            if p.communicating() is False:
                x += 1
                p.send_request(
                    f"this is my request {str(x)} using pool index {pools.index(p)}")
