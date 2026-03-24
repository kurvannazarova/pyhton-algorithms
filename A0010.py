a, b, c = map(int, input().split())

desks = (a + 1) // 2 + (b + 1) // 2 + (c + 1) // 2

print(desks)

#2-usul
import math
a, b, c = map(int, input().split())
print(math.ceil(a / 2) + math.ceil(b / 2) + math.ceil(c / 2))