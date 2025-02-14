import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.merge(employee[["id", "salary"]], left_on = "managerId", right_on = "id", how = "left", suffixes = (None, "_y"))
    return employee[employee.salary > employee.salary_y][["name"]].rename({"name" : "Employee"}, axis = 1)