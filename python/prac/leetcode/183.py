# Write a solution to find all customers who never order anything.
# Return the result table in any order.
# The result format is in the following example.

# PANDAS
import pandas as pd
def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    customerNames = [] 
    ans = customers[["id","name"]].merge(orders[["customerId"]],left_on = "id",right_on = "customerId",how = "left")
    customerNames = ans[ans["customerId"].isna()]["name"].tolist()
    return pd.DataFrame(data = customerNames,columns = ["Customers"])

