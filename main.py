import random
allTokens = int(input())
userTokens = []
n = [1] * allTokens
x = [0, 2]
n[random.randint(0, allTokens - 1)] = random.choice(x)
print(n)
nLen = len(n)
nPart1 = []
nPart2 = []
nPart3 = []
nPart4 = []


def toDivision4():
    global allTokens, userTokens, nLen
    while nLen % 4 != 0:
        index = random.randint(0, allTokens - 1)
        del n[index]
        nLen = len(n)
        userTokens.append(n[index])


toDivision4()
for i in range(int(nLen / 2)):
    nPart1.append(n[i])
    nPart2.append(n[int(i + nLen / 2)])

for i in range(int(len(nPart1) / 2)):
    nPart3.append(n[i])
    nPart4.append(n[int(i + len(nPart1) / 2)])
if sum(userTokens) == 0 or nPart1 != nPart2:
    if allTokens % 4 != 0:
        print("Число монет не кратно 4. Забираем монеты")
    print("Число монет кратно 4. Первый ход - делим монеты на 2 части, взвешиваем.")
    if sum(nPart1) > sum(nPart2) and nPart3 == nPart4:
        print("Первая часть тяжелее второй.")
        print("Второй ход - первую часть делим на еще две части.")
        print("Они равны")
        print("Фальшивая монета легче.")
    elif sum(nPart1) > sum(nPart2) and nPart3 != nPart4:
        print("Первая часть тяжелее второй.")
        print("Второй ход - первую часть делим на еще две части.")
        print("Они не равны")
        print("Фальшивая монета тяжелее.")
    elif sum(nPart1) < sum(nPart2) and nPart3 == nPart4:
        print("Первая часть легче второй.")
        print("Второй ход - первую часть делим на еще две части.")
        print("Они равны")
        print("Фальшивая монета тяжелее.")
    else:
        print("Первая часть легче второй.")
        print("Второй ход - первую часть делим на еще две части.")
        print("Они не равны")
        print("Фальшивая монета легче.")

else:
    print("Число монет не кратно 4. Забираем монеты. Число монет кратно 4. Первый ход - делим монеты на 2 части, взвешиваем.")
    if sum(userTokens) < len(userTokens):
        print("Части равны")
        print("Взвешиваем. Вес наших монет меньше, чем столько же настоящих.")
        print("Фальшивая монета легче.")
    else:
        print("Части равны")
        print("Взвешиваем. Вес наших монет больше, чем столько же настоящих.")
        print("Фальшивая монета тяжелее.")