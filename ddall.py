m = -1
p = -1
q = -1
s = -1

while m < 0 or m > 48:
    m = int(input("минуты: "))
    if m < 0 or m > 48:
        print("введите значение(0-48).")
    else:
        break

while s < 0 or s > 59:
    s = int(input("секунды: "))
    if s < 0 or s > 59:
        print("введите значение(0-59).")
    else:
        break

while p < 0 or p > 1000:
    p = int(input("Воины золотого штата: "))
    q = int(input("Востон Келтикс: "))
    if p < 0 or p > 1000:
        print("введите значение от 0 до 1000.")
    else:
        break

while q < 0 or q > 1000:
    q = int(input("Востон Келтикс "))
    if q < 0 or q > 1000:
        print("введите значение от 0 до 1000.")
    else:
        break

t = 2880 - m * 60 - s
print("до конца матча осталось", t, "секунд")

if t % 48 >= 24:
    p += (t // 48 + 1) * 3
else:
    p += (t // 48) * 3

if (t - 24) % 96 >= 24:
    q += ((t - 24) // 96 + 1) * 2
else:
    q += ((t - 24) // 96) * 2

print("Итоговый счёт:")
print("Воины золотого штата:", p)
print("Востон Келтикс:", q)
# excite
