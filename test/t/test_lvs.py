import pytest


class TestLvs:

    @pytest.mark.complete("lvs --",
                          skipif="! lvs --help &>/dev/null")
    def test_1(self, completion):
        assert completion
