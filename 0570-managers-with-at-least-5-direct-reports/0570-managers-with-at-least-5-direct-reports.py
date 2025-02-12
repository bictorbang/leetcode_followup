import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    ag = employee.groupby("managerId").agg(cnt = ("managerId", "count")).reset_index()
    ag = ag[ag["cnt"] > 4]["managerId"].values
    return employee[employee["id"].isin(ag)][["name"]]