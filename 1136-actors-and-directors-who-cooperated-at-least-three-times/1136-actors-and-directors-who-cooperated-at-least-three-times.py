import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    actor_director = actor_director.groupby(["actor_id", "director_id"]).count().reset_index()
    return actor_director[actor_director.timestamp > 2][["actor_id", "director_id"]]