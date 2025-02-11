import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    if employee.empty or department.empty:
        return pd.DataFrame(columns=['Department','Employee', 'Salary'])
    employee = employee.rename({"name": "Employee"}, axis = 1)
    return employee.merge(department, left_on = "departmentId", right_on = "id").rename({"name" : "Department", "salary": "Salary"}, axis = 1)[["Department", "Employee", "Salary"]].groupby("Department").apply(lambda x: x[x["Salary"] == x["Salary"].max()])