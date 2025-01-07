class NetworkSpeedTemplate:

    def __init__(self):
        self._test_data = None

    @property
    def TestData(self):
        return self._test_data

    @TestData.setter
    def TestData(self, value):
        self._test_data = value

    def Prepare(self):
        pass

    def Run(self):
        pass

    def Clean(self):
        pass

    def CheckActiveCardMode(self, mode):
        print(f"\nActive card mode {mode} ")

    def CheckEachSpeed(self, port, speed):
        print(f"\nPort speed {port}, {speed} ")

    def SaveCardMode(self):
        print("\nSave active card mode ")

    def RestoreDefaultMode(self):
        print("\nRestore default mode ")

    def RestoreDefaultSpeed(self):
        print("\nRestore default speed ")

    def Waiting(self):
        print("\nWaiting time 3 secs ")

    def SetCardMode(self, mode):
        print(f"\nCard mode {mode} ")

    def Reset(self):
        print("\nReset ")

    def SetPortSpeed(self, port_number, port_speed):
        print(f"\nSetting port speed {port_number} to {port_speed} ")

    def CheckPortStatus(self, port_number):
        print(f"\nChecking status of port {port_number} ")
