import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    df = students.merge(subjects, how = "cross").sort_values(by = ["student_id", "subject_name"]).merge(examinations.groupby(["subject_name", "student_id"]).agg(attended_exams = ("subject_name", "count")).reset_index(), how = "left")
    df["attended_exams"].fillna(0, inplace = True)
    return df