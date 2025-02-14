import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    cnt = person.groupby("email").count().reset_index()
    return cnt[cnt["id"] > 1][["email"]]