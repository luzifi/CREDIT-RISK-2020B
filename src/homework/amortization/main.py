from typing import Optional

from fintools import Amortization


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        f = Amortization(amount, rate, n)
        res = f.annuity
        return res

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        ta = Amortization(amount, rate, n)
        tt = ta.get_table(save_file)
        return tt

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        raise NotImplementedError
