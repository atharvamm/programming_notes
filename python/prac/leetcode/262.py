# The cancellation rate is computed by dividing the number of canceled (by client or driver) requests with unbanned users by the total number of requests with unbanned users on that day.

# Write a solution to find the cancellation rate of requests with unbanned users (both client and driver must not be banned) each day between "2013-10-01" and "2013-10-03". Round Cancellation Rate to two decimal points.

# Return the result table in any order.

# The result format is in the following example.


# PANDAS
import pandas as pd

def trips_and_users(trips: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    dates = []
    cancellation_rate = []
    users["banned"].replace({"No":False,"Yes":True},inplace=True)
    trips["client_banned"] = trips.merge(users,how = "left",left_on = "client_id",right_on="users_id",right_index=False)["banned"]
    trips["driver_banned"] = trips.merge(users,how = "left",left_on = "driver_id",right_on="users_id",right_index=False)["banned"]
    trips["banned"] = trips["client_banned"] | trips["driver_banned"]
    trips.drop(trips[trips['banned'] == True].index,inplace=True)
    trips.drop(columns=["banned","client_banned","driver_banned","city_id","driver_id","id"],inplace=True)
    for date in ["2013-10-01", "2013-10-02","2013-10-03"]:
        temp = trips[trips["request_at"] == date]
        condition = temp["status"] != "completed"
        if len(condition) > 0:
            dates.append(date)
            cancellation_rate.append(round(sum(condition)/len(condition),2))
    return pd.DataFrame(data = {"Day":dates,"Cancellation Rate":cancellation_rate})
    


