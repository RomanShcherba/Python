class NetworkSpeedFlow:
    def test_data(self):
        raise NotImplementedError("Need to override test_data")

class NetworkCardSpeed01(NetworkSpeedFlow):
    NAME = "NetworkCardSpeed01"
    DESCRIPTION = "Test with card mode 1"

    def test_data(self):
        assert [
            (1, [(1, 10)]),
                ]
    