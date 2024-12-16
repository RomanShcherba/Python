class EthernetFrameHeader:

    def __init__(self, data: bytes):
        self.destination_address = ":".join(f"{byte:02X}" for byte in data[:6])
        self.source_address = ":".join(f"{byte:02X}" for byte in data[6:12])
        self.ether_type = int.from_bytes(data[12:14], "big")  # 16-бітний EtherType
    
    def display(self):
        print(f"\nEthernet frame header:")
        print(f"Destination Address (DA): {self.destination_address}")
        print(f"Source Address (SA): {self.source_address}")
        print(f"EtherType: 0x{self.ether_type:04X}")