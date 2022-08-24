from random import randrange


def func(n, change):
    ans = randrange(1, 4)
    if ans == n:
        if change:
            return False
        return True
    else:
        if change:
            return True
        return False


countTrue = 0
countFalse = 0
tentativas = 100000

for i in range(tentativas):
    if func(randrange(1, 4), True):
        countTrue += 1
    if func(randrange(1, 4), False):
        countFalse += 1

print(f'Соотношение выигрышей к проигрышу при смене выбора двери - {countTrue / (tentativas - countTrue)}\n'
      f'Соотношение выигрышей к проигрышу без смены выбора двери - {countFalse / (tentativas - countFalse)}')
