import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees["total_time"] = employees["out_time"] - employees["in_time"]
    return employees.groupby(["emp_id", "event_day"])["total_time"].sum().reset_index().rename({"event_day" : "day"}, axis = 1)