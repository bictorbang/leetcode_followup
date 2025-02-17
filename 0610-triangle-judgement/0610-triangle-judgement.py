import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = np.where((triangle.x + triangle.y > triangle.z) & (triangle.x + triangle.z > triangle.y) & (triangle.y + triangle.z > triangle.x), "Yes", "No")
    return triangle