import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] =  triangle.apply(lambda r: 'Yes' if (r['x'] + r['y'] > r['z']) & (r['y'] + r['z'] > r['x'])
& (r['x'] + r['z'] > r['y']) else 'No', axis=1)
    return triangle