import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = 0
    employees.loc[(employees.name.apply(lambda x: x[0]) != "M")&(employees.employee_id % 2 == 1), "bonus"] = employees["salary"]
    return employees[["employee_id", "bonus"]].sort_values("employee_id")