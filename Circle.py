M = int(input())

count = 0
d = 10
step = 20
while d <= M:
    count += 1
    d += step
    #Чергуємо кроки: 20, 10, 20, 10, ...
    step = 10 if step == 20 else 20

print(count)
