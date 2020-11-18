from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        return (self.amount * ((1 + self.rate) ** self.n) * self.rate) / (((1 + self.rate) ** self.n) - 1)

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        table = {"t": [], "B": [self.amount], "A": [np.nan], "P": [np.nan], "I": [np.nan]}
        table["t"] = list(range(0, self.n + 1))
        table["A"] = [self.annuity for i in range(self.n + 1)]
        for i in range(self.n):
            inte = table["B"][i] * self.rate
            P = self.annuity - inte
            B = table["A"][i] - P
            table["P"].append(P)
            table["I"].append(inte)
            table["B"].append(B)
        return pd.DataFrame(table, columns=["t", "B", "A", "P", "I"])

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        raise NotImplementedError
