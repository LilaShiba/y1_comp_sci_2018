# naive recursive algorithm
# exponetial time
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
#fib(18)

#                  fn
#           fn-1        fn-2
#      fn-2  fn-3     fn-3  fn-4

# dynamic programming
# memoized dp alogrithm

# nth fib num
def fib(n):
    # whenever we computer a fib num, put it in the dict
    # then as we move along we check this dict to stop repeating
    memo = {}
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        f = fib(n-1) + fib(n-2)
        memo[n] = f
        print(f)
        return f
fib(6)
