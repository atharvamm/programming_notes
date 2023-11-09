# Write a solution to find the employees who earn more than their managers.
# Return the result table in any order.


# PANDAS
import pandas as pd
def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    df = employee.merge(employee[["id","salary"]],how = 'inner',left_on = "managerId",right_on = "id",right_index = False)
    df["condn"] = df["salary_x"] > df["salary_y"]
    return pd.DataFrame(data = df[df["condn"] == True]["name"].tolist(),columns = ["Employee"])
    
