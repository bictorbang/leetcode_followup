import pandas as pd

def exchange_seats(seat: pd.DataFrame) -> pd.DataFrame:
    seat.loc[(seat.id % 2 == 1) ,  "new"] = seat.student.shift(-1)
    seat.loc[(seat.id % 2 == 0) ,  "new"] = seat.student.shift()
    seat["student"] = seat.apply((lambda x: x.new if not pd.isna(x.new) else x.student), axis = 1)
    return seat.drop("new", axis = 1)