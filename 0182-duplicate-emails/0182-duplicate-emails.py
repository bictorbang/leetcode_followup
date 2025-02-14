import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    return person.loc[person.duplicated('email')][['email']].drop_duplicates(keep = 'first')