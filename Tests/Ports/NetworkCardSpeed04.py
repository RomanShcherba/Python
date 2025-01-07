class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed04"
    DESCRIPTION = "Test with card mode 2"

    def test_data(self):
        return [
            (2, [
                (1, 25),
                (2, 50),
            ]),
        ]
    