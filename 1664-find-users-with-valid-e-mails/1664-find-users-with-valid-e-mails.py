import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    def valid(x):
        if not x[0].isalpha(): return False
        if len(x) < 13: return False
        if x[-13:] != "@leetcode.com": return False
        for elt in x[:-13]:
            if not elt.isalnum() and elt not in "_.-": return False
        return True
    return users[users.mail.apply(valid)]