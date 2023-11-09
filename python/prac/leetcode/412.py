# Given an integer n, return a string array answer (1-indexed) where:

# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = [None]*n
        for i in range(1,n+1):
            div_3,div_5 = i%3 == 0,i%5 == 0
            if div_3 and div_5 :
                ans[i - 1] = "FizzBuzz"
            elif div_3:
                ans[i - 1] = "Fizz"
            elif div_5:
                ans[i - 1] = "Buzz"
            else:
                ans[i - 1] = str(i) 
        return ans