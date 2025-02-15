import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    persons = pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]])
    cnt = persons.value_counts()
    return pd.DataFrame({"id": [cnt.index[0]], "num" : [cnt.values[0]]})