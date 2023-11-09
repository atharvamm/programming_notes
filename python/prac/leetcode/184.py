# Write a solution to find employees who have the highest salary in each of the departments.

# Return the result table in any order.

# The result format is in the following example.

# PANDAS
import pandas as pd
def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
  max_series = employee.groupby("departmentId")["salary"].transform(max)
  df = (employee[employee["salary"] == max_series][["name","departmentId","salary"]]).merge(department[["id","name"]],left_on = "departmentId",right_on = "id",how = "left")
  df.rename(columns={"name_x": "Employee", "name_y": "Department","salary":"Salary"},inplace = True)
  return df[["Department","Employee","Salary"]]

