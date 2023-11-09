# Write a solution to find the second highest salary from the Employee table. If there is no second highest salary, return null (return None in Pandas).

# PANDAS
import pandas as pd
def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee.sort_values(by = ["salary"],inplace=True,ascending = [False])
    employee.drop_duplicates(subset = ["salary"],keep = 'first',inplace = True)
    if(len(employee) > 1):
        return pd.DataFrame(data = [employee.iloc[1]["salary"]],columns = ["SecondHighestSalary"])
    else:
        return pd.DataFrame(data = [None],columns = ["SecondHighestSalary"])
    

