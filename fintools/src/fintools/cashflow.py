from typing import Dict, Optional
import numpy_financial as npf
import numpy as np


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        vp = round((npf.pv(r, self.n, 0, self.amount)) * -1, 2)
        return CashFlow(amount=vp, n=0)

    def shift(self, n: int, r: float) -> 'CashFlow':
        vs = round((npf.fv(r, n - self.n, 0, self.amount)) * -1, 2)
        return CashFlow(amount=vs, n=n - self.n)

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        vm = CashFlow.pv(self, r)
        vm1 = CashFlow.pv(other, r)
        return vm, vm1

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }
