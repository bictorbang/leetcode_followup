import pandas as pd

def most_friends(request_accepted: pd.DataFrame) -> pd.DataFrame:
    persons = pd.concat([request_accepted["requester_id"], request_accepted["accepter_id"]])
    persons = persons.groupby(persons).size().reset_index().rename({"index" : "id", 0 : "num"}, axis = 1)
    return persons[persons["num"] == persons["num"].max()]