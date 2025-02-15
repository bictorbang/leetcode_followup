import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    city = insurance.duplicated(["lat", "lon"], keep = False)
    tiv_2015 = insurance.duplicated("tiv_2015", keep = False)
    return insurance[(~city)&(tiv_2015)][["tiv_2016"]].sum().to_frame(name = "tiv_2016")