import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    weather = weather.sort_values(by = "recordDate")
    weather["diff"] = weather["recordDate"] - weather.shift()["recordDate"]
    return weather[(weather["temperature"] > weather["temperature"].shift()) & (weather["diff"]==pd.Timedelta(days = 1))][["id"]]