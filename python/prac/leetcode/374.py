# We are playing the Guess Game. The game is as follows:

# I pick a number from 1 to n. You have to guess which number I picked.

# Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

# You call a pre-defined API int guess(int num), which returns three possible results:

# -1: Your guess is higher than the number I picked (i.e. num > pick).
# 1: Your guess is lower than the number I picked (i.e. num < pick).
# 0: your guess is equal to the number I picked (i.e. num == pick).
# Return the number that I picked.

class Guesser:
    def __init__(self,k) -> None:
        self.k = k

    def guess(self,num):
        # print(num,self.k)
        if num == self.k:
            return 0
        elif num > self.k:
            return -1
        else:
            return 1 


def guessNumber(n: int,picked) -> int:
    if n < 2:
        return n
    start,mid,end = 0,0,n

    while start <= end:
        mid = (start + end) // 2
        check_pick = guess(mid)

        if check_pick == 0:
            return mid
        elif check_pick == 1:
            start = mid + 1
        else:
            end = mid - 1


import numpy as np
for max_num in np.random.randint(1,5**5,size=(25,)):
    guess_val = np.random.randint(1,max_num+1)
    print(max_num,guess_val, end = " ")
    op = guessNumber(max_num,guess_val)
    if (guess_val == op): print("Passed")
    else: print("Failed")
