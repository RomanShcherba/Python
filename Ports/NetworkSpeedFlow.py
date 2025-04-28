import NetworkSpeedTemplate


class NetworkSpeedFlow(NetworkSpeedTemplate):

    NAME = "NetworkSpeedFlow"
    DESCRIPTION = "Network speed flow test"

    def Prepare(self):
        print("\nPrepare test")
        mode = self.TestData[0][0]
        self.CheckActiveCardMode(mode)
        self.SaveCardMode()
        self.Reset()
        return True

    def Run(self):
        print("\nRunning test")
        for mode, speeds in self.TestData:
            print(f"\nRunning mode: {mode}")
            self.Waiting()
            for port, speed in speeds:
                self.SetPortSpeed(port, speed)
                self.CheckPortStatus(port)

    def Clean(self):
        self.RestoreDefaultMode()
        self.RestoreDefaultSpeed()
        print("\nCleaning up after test")
        return True