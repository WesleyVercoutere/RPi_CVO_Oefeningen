import socket

class IPAddressHelper:

    def __init__(self) -> None:
        pass

    def get_ip_address(self) -> str:
        ip_address = 'Runs on ESP32'
        # s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # s.connect(("8.8.8.8",80))
        # ip_address = s.getsockname()[0]
        # s.close()

        return ip_address
        