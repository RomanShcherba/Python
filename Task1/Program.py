import os
import sys

# Додаємо шлях до Task1 у пошук модулів
sys.path.append(os.path.join(os.path.dirname(__file__)))

from Parser.EthernetFrameHeader import EthernetFrameHeader
from Parser.NCSIControlPackHeader import NcsiControlPacketHeader


class Program:

    @staticmethod
    def main():
        file_path = os.path.join("Task1", "Data", "HexInput.txt")

        print(f"File path: {file_path}")
        if not os.path.exists(file_path):
            print("File does not exist.")
            return
        else:
            print("File exists.")

        with open(file_path, "r") as file:
            hex_strings = file.readlines()

        for hex_string in hex_strings:
            hex_string = hex_string.strip()

            try:
                data = bytes.fromhex(hex_string)
                ethernet_header = EthernetFrameHeader(data)
                ethernet_header.display()

                ncsi_control_packet_header = NcsiControlPacketHeader(data)
                ncsi_control_packet_header.display()
            except ValueError as e:
                print(f"Error processing line: {hex_string}. Details: {str(e)}")


# Запуск програми
if __name__ == "__main__":
    Program.main()
