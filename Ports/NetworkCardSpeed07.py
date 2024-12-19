class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed07"
    DESCRIPTION = "Test with card mode 4"

    def test_data(self):
        return [
            (4, [
                (1, 0),
                (2, 10),
                (3, 10),
                (4, 50),
            ]),
        ]
    