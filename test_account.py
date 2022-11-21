import pytest
from account import *


class Test:
    def setup_method(self):
        self.account1 = Account('Billy', 10)
        self.account2 = Account('Sarah')

    def teardown_method(self):
        del self.account1
        del self.account2

    def test_init(self):
        assert self.account1.get_name() == 'Billy'
        assert self.account1.get_balance() == pytest.approx(10, abs=0.001)
        assert self.account2.get_name() == 'Sarah'
        assert self.account2.get_balance() == pytest.approx(0, abs=0.001)

    def test_deposit(self):
        assert self.account1.deposit(0) is False
        assert self.account1.get_balance() == pytest.approx(10, abs=0.001)
        assert self.account2.deposit(-5) is False
        assert self.account2.get_balance() == pytest.approx(0, abs=0.001)
        assert self.account1.deposit(10) is True
        assert self.account1.get_balance() == pytest.approx(20, abs=0.001)
        assert self.account2.deposit(5) is True
        assert self.account2.get_balance() == pytest.approx(5, abs=0.001)

    def test_withdraw(self):
        assert self.account1.withdraw(2) is True
        assert self.account1.get_balance() == pytest.approx(8, abs=0.001)
        assert self.account1.withdraw(20) is False
        assert self.account1.get_balance() == pytest.approx(8, abs=0.001)
        assert self.account2.withdraw(10) is False
        assert self.account2.get_balance() == pytest.approx(0, abs=0.001)
