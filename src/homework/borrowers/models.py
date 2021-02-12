import json
from typing import Dict

from .utils import get_current_utc


class Borrower:

    def __init__(self, email: str, age: int, income: float):
        self.created_at = get_current_utc()
        self.updated_at = self.created_at
        self.email = email
        self.age = age
        self.income = income

    def to_json(self) -> Dict:
        # TODO: return a json with the: email, age, income, created_at, and updated_at
        return {
            "email": self.email,
            "age": self.age,
            "income": self.income,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def save(self, file: str):
        # TODO: save the borrower into the json file!
        with open(file, "r") as f:
            content = f.read()
            fl = json.loads(content)
            fl["candidates"].append(self.to_json())
            fl["updated_at"] = self.updated_at
            with open(file, "w") as f:
                f.write(json.dumps(fl))

    def update(self, file: str):
        # TODO: update the borrower on the json file that match the email of the current borrower.
        with open(file) as f:
            fl = json.load(f)
        for i in fl['candidates']:
            if i["email"] == self.email:
                i["age"] = self.age
                i["income"] = self.income
                i["updated_at"] = self.updated_at
        fl["updated_at"] = self.updated_at

        with open(file, 'w') as f:
            f.write(json.dumps(fl, indent=4))
