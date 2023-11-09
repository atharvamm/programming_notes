import pandas as pd
import json
import random
# fpath = r"my_practice/sner_data.csv"
# df = pd.read_csv(fpath,delimiter=" ",names = ["text","label"])

with open("my_practice/train_data.json","r") as f:
    ip_json = f.read()


ip_json = json.loads(ip_json)

# print([x["value"] for x in ip_json[0]["annotations"][0]["result"]])
paperid = set([jsonstr["data"]["paperid"] for jsonstr in ip_json])

random.seed(100)
random.shuffle(list(paperid))
wdata = "\n".join(paperid)

with open("my_practice/paperid.txt","w") as f:
    f.write(wdata)
