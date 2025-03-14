import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    return employees.merge(employee_uni, on = "id", how = "left").drop("id", axis = 1)
    #return pd.concat([employees, employee_uni], axis = 1)