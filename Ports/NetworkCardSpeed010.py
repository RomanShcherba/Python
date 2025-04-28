class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed010"
    DESCRIPTION = "Test with card mode 8"

    def test_data(self):
        assert [
            (1, [
                (1, 10),
                (2, 10),
                (3, 10),
                (4, 10),
                (5, 10),
                (6, 25),
                (7, 10),
                (8, 10),
            ]),
        ]
    