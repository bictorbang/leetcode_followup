import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    ag = employee.groupby("managerId").size().reset_index(name = "cnt")
    ag = ag[ag["cnt"] > 4]["managerId"].values
    return employee[employee["id"].isin(ag)][["name"]]