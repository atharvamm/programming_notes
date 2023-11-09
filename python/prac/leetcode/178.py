# Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

# The scores should be ranked from the highest to the lowest.
# If there is a tie between two scores, both should have the same ranking.
# After a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no holes between ranks.
# Return the result table ordered by score in descending order.

# PANDAS
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    if len(scores):
        scores.sort_values(by = ["score"],ascending = [False],inplace = True,ignore_index = True)
        scores["rank"] = None
        rank = 1
        scores.iloc[0,2] = rank
        for i in range(1,len(scores)):
            score_prev = scores.iloc[i - 1,1]
            score_cur = scores.iloc[i,1]
            if score_cur != score_prev:
                rank += 1
            scores.iloc[i,2] = rank
        return scores[["score","rank"]]
    return pd.DataFrame(data = [],columns=["score","rank"])

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores.sort_values(by = "score",ascending = False,inplace = True)
    scores["rank"] = scores["score"].rank(method = "dense", ascending = False)
    return scores[["score","rank"]]
