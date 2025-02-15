import pandas as pd

def find_valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    return users[users["email"].str.match("(\w)+@([a-zA-Z])+.com$")]