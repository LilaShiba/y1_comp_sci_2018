def fib(start, previous):
    if start <= 1:
        return start
    if start > 1 and start < 50:
        start_new = start + previous
        print(start_new)
        fib(start_new, start)
    if start > 50:
        return start

fib(3,2)
