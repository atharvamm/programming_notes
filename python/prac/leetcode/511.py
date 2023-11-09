# Write a solution to find the first login date for each player.
# Return the result table in any order.
# The result format is in the following example.

# PANDAS
import pandas as pd

def game_analysis(activity: pd.DataFrame) -> pd.DataFrame:
    activity.sort_values(by = ["event_date","player_id"],ascending = [True,True],inplace = True)
    activity.drop_duplicates(subset = ["player_id"],inplace = True, keep = "first")
    activity.drop(columns = ["games_played","device_id"],inplace = True)
    activity.rename(columns = {"event_date":"first_login"},inplace = True)
    return activity

