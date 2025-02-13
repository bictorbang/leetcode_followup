import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee = employee.rename({"name" : "Employee"}, axis = 1)
    df = employee.merge(department, left_on = "departmentId", right_on = "id").rename({"name" : "Department", "salary": "Salary"}, axis = 1)[["Department", "Employee", "Salary"]]
    return df.merge(df.drop("Employee", axis = 1).drop_duplicates().sort_values("Salary", ascending = False).groupby("Department").head(3), on = ["Department", "Salary"])