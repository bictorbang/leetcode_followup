import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    dup = my_numbers.drop_duplicates(keep = False)
    if len(dup) == 0: 
        return pd.DataFrame({"num" : [None]})
    return dup.max().to_frame(name = "num")