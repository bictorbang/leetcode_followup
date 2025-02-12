import pandas as pd
#
def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    courses = courses.groupby("class").count().reset_index()
    return courses.loc[courses.student > 4][["class"]]