class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed06"
    DESCRIPTION = "Test with card mode 4"

    def test_data(self):
        return [
            (4, [
                (1, 10),
                (2, 25),
                (3, 25),
                (4, 25),
            ]),
        ]
    