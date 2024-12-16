class NcsiControlPacketHeader:

    def __init__(self, data: bytes):
        self.mc_id = data[0]
        self.header_revision = data[15]
        self.reserved1 = data[16]
        self.instance_id = data[17]
        self.control_packet_type = data[18]
        self.channel_id = data[19]
        flags_byte = data[20]
        self.flags = flags_byte & 0x0F
        
        payload_length = int.from_bytes(data[21:23], byteorder="big")
        self.payload_length = payload_length & 0x0FFF

        self.reserved2 = "".join(f"{b:02X}" for b in data[23:27])
        self.reserved3 = "".join(f"{b:02X}" for b in data[27:31])
        self.response_code = "".join(f"{b:02X}" for b in data[31:33])
        self.reason_code = "".join(f"{b:02X}" for b in data[33:35])
        self.checksum = "".join(f"{b:02X}" for b in data[35:39])
        self.padding = "".join(f"{b:02X}" for b in data[39:63])
    
    def display(self):
        print(f"\nNCSI Control Packet Header:")
        print(f"MC ID: 0x{self.mc_id:02X}")
        print(f"Header Revision: 0x{self.header_revision:02X}")
        print(f"Reserved1: 0x{self.reserved1:02X}")
        print(f"Instance ID (IID): 0x{self.instance_id:02X}")
        print(f"Control Packet Type: 0x{self.control_packet_type:02X}")
        print(f"Channel ID: 0x{self.channel_id:02X}")
        print(f"Flags: 0x{self.flags:02X}")
        print(f"Payload Length: 0x{self.payload_length:03X}")
        print(f"Reserved2: 0x{self.reserved2}")
        print(f"Reserved3: 0x{self.reserved3}")
        print(f"Response Code: 0x{self.response_code}")
        print(f"Reason Code: 0x{self.reason_code}")
        print(f"Checksum: 0x{self.checksum}")
        print(f"Padding: 0x{self.padding}")