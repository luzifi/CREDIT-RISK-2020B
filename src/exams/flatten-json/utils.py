import json
from typing import Dict


class FLT:

    def flatten_dict(fll) -> dict:
        with open(fll, "r", ) as f:
            fll = json.load(f)
        flatten_out = {}

        def fld(dc, prr=''):
            if type(dc) is dict:

                for k in dc:
                    fld(dc[k], prr + k + '.')

            elif type(dc) is list:
                cs = 0
                for k in dc:
                    fld(k, prr + str(cs) + '.')
                    cs += 1
            else:
                flatten_out[prr[:-1]] = dc
        fld(fll)
        return flatten_out
