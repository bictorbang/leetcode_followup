import pandas as pd
import numpy as np

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    return tweets.loc[tweets.content.apply(lambda x : np.nan if len(x)>15 else 0).isna(), ["tweet_id"]]