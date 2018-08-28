#get's fib number up to n
#recursive example

def fib(n, memo = {})
  if n == 0 || n == 1
    return n
  end
  memo[n] ||= fib(n-1, memo) + fib(n-2, memo)
end