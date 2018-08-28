def solution(n):
    i, d = divmod(n, 1)
    if d >= .21 and d < .75:
        d = .5
        n = int(n)
        return(round(n+d,2))
    elif d < .21:
        return i
    elif d <= 0:
        return i - .5
    else:
        return(i + 1)

# or

def sol(n):
    return round(2 * n) / 2

solution(4.3)
solution(4.5)
solution(4.75)
solution(4.8)
