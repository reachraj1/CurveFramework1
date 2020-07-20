import glob
import json
from utils import objects, CurveBuilder


def buildCurves(date):
    curve_path = 'curves/*.json'
    curves = {}
    for file in glob.glob(curve_path):
        f = json.load(open(file))
        curves = {**curves, **
                  {crv: CurveBuilder(f[crv], date).curve for crv in f}}
    return curves


curves = buildCurves('16-09-2019')

'''
for c in curves:
    print(c, curves[c].discount(1))
'''
