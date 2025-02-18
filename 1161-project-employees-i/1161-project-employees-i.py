import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    return project.merge(employee).groupby("project_id").agg(average_years = ("experience_years", "mean")).round(2).reset_index()