class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed08"
    DESCRIPTION = "Test with card mode 8"

    def test_data(self):
        assert [
            (8, [
                (1, 0),
                (2, 10),
                (3, 0),
                (4, 10),
                (5, 10),
                (6, 10),
                (7, 50),
                (8, 0)
            ]),
        ]
    