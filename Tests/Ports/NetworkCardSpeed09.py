class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed09"
    DESCRIPTION = "Test with card mode 8"

    def test_data(self):
        return [
            (8, [
                (1, 10),
                (2, 10),
                (3, 0),
                (4, 0),
                (5, 25),
                (6, 10),
                (7, 10),
                (8, 0),
            ]),
        ]
    