import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #employee = employee.rename({"name": "Employee"}, axis = 1)
    #return employee.merge(department, left_on = "departmentId", right_on = "id").rename({"name" : "Department", "salary": "Salary"}, axis = 1)[["Department", "Employee", "Salary"]].groupby("Department").apply(lambda x: x[x["Salary"] == x["Salary"].max()])
    employee = employee.rename({"name" : "Employee"}, axis = 1)
    df = employee.merge(department, left_on = "departmentId", right_on = "id").rename({"name" : "Department", "salary": "Salary"}, axis = 1)[["Department", "Employee", "Salary"]]
    print(df)
    #df = df.groupby("Department").apply(lambda x : x[x["Salary"].isin(x[["Salary"]].drop_duplicates().sort_values(by = "Salary", ascending = False).head(3))])
    df_ = df[["Department", "Salary"]].drop_duplicates().sort_values("Salary", ascending = False).groupby("Department").head(3)
    print(df_)

    return df.merge(df_, on = ["Department", "Salary"])