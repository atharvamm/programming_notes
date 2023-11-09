# Write a solution to report all the duplicate emails. Note that it's guaranteed that the email field is not NULL.

# Return the result table in any order.


# PANDAS
import pandas as pd
def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    x = person["email"].value_counts()
    name_list = []
    for email,count in zip(x.index,x.values):
        if count > 1:
            name_list.append(email)
    return pd.DataFrame(data = name_list,columns = ["Email"])

