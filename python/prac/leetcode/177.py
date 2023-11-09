# Write a solution to find the nth highest salary from the Employee table. If there is no nth highest salary, return null.

# PANDAS
import pandas as pd
def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    employee.drop_duplicates(subset = ["salary"],inplace = True, keep = 'first')
    # employee.sort_values(by = ["salary"],ascending = [False], inplace = True)
    salary = employee["salary"].sort_values(ascending = False)
    ans = [None]
    if len(employee) >= N:
        ans = [salary.iloc[N - 1]]
    col_name = "getNthHighestSalary" + "("+str(N)+")"
    return pd.DataFrame(data = ans, columns = [col_name])