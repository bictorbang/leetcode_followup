import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium["hundred"] = stadium["people"].apply(lambda x: 0 if x < 100 else 1)
    labels = (stadium.hundred.diff().ne(0)).cumsum()
    stadium['flag'] = (labels.map(labels.value_counts()) >= 3).astype(int)
    return stadium[(stadium["flag"] == 1)][["id", "visit_date", "people"]]