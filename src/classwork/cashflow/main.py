import json

from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        cf = CashFlow(amount, n)
        res = cf.pv(rate)
        return json.dumps(res.to_dict())

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        cf = CashFlow(amount, 0)
        # Shift to n=24
        res = cf.shift(n, rate)
        return json.dumps(res.to_dict())
