m = -1
p = -1
q = -1
s = -1


def score(m, s, p, q, i):
    if i % 2 != 0:
        at = "|Воины золотого штата |"
    else:
        at = "|Востон Келтикс       |"
    if s <= 10:
        print("|", i, at, m, ":", s, " |", p, ":", q, "|")
    else:
        print("|", i, at, m, ":", s, "|", p, ":", q, "|")


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
i = 2
a = 1

if s > 0:
    m = 47 - m
    s = 60 - s

else:
    m = 48 - m

print(m, s)

print("|#  |Атакующая команда    |Время   |Счёт       |")
run = True
while run:
    if i % 2 == 0:  # атака Воины золотого штата p
        print("ВЗС")
        if s >= 24 and m > 0:
            s -= 24
            p += 3
            i += 1
            score(m, s, p, q, i)
        if m > 0 and s < 24:
            m -= 1
            s = s + 60 - 24
            p += 3
            i += 1
            score(m, s, p, q, i)
        if m == 0 and s < 24:
            break
    if i % 2 != 0:  # атака Востон Келтикс_q
        print("ВК")
        if a % 2 != 0:  # удача
            if s >= 24 and m > 0:
                s -= 24
                q += 2
                i -= 1
                score(m, s, p, q, i)
            if m > 0 and s < 24:
                m -= 1
                s = s + 60 - 24
                q += 2
                i -= 1
                score(m, s, p, q, i)
            if m == 0 and s < 24:
                break
        if a % 2 == 0:  # поражение
            if s >= 24 and m > 0:
                s -= 24
                q += 2
                i -= 1
                score(m, s, p, q, i)
            if m > 0 and s < 24:
                m -= 1
                s = s + 60 - 24
                q += 2
                i -= 1
                score(m, s, p, q, i)
            if m == 0 and s < 24:
                break
