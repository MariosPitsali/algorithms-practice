def factor(n):
    q = n
    r = 0
    while (q % 2)==0 :
        r += 1
        q /= 2
    return r, q

print factor(8)
2^3 * 1