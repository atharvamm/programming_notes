# Write a solution to find managers with at least five direct reports.

# Return the result table in any order.

# The result format is in the following example.


# PANDAS
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    x = employee.groupby("managerId")["id"].count()
    names = []
    for ele in zip(x.index,x.values):
        if ele[1] > 4:
            temp = employee[employee["id"] == ele[0]]
            if len(temp):               
                names.append(temp["name"].values)
    return pd.DataFrame(data = names, columns = ["name"])    


