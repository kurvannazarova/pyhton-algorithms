import math

S, P = map(int, input().split())

D = S*S - 4*P

if D < 0:
    print(-1)
else:
    sqrtD = int(math.isqrt(D))

    if sqrtD * sqrtD != D:
        print(-1)
    else:
        a = (S + sqrtD) // 2
        b = (S - sqrtD) // 2
 
        if a + b == S and a * b == P:
            print(a, b)
        else:
            print(-1)