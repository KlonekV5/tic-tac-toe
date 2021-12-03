import random

def gra():
    o = ''
    w = 0
    linia = '───┼───┼───\n'
    znaki = []
    runda = int(random.randint(0, 1))
    koniec = 9 + runda
    print(globals())

    def pisz(p):
        while True:
            d = int(input('GRACZU ' + p + ' \n wybierz pole ktore chcesz zaznaczyc! '))
            if znaki[d-1] == '   ':
                znaki[d-1] = ' ' + p + ' '
                return
            else:
                print('to pole jest zajete!')

    def druk():
        print('----------------------')
        trzy(7)
        print(linia, end='')
        trzy(4)
        print(linia, end='')
        trzy(1)
        print('----------------------')

    def trzy(j):
        print(znaki[j-1] + '|' + znaki[j] + '|' + znaki[j+1])

    def wygrana():
        trzypola(7, 1)
        trzypola(4, 1)
        trzypola(1, 1)
        trzypola(3, 3)
        trzypola(4, 3)
        trzypola(5, 3)
        trzypola(4, 4)
        trzypola(4, 2)

    def trzypola(r, t):
        nonlocal w
        if znaki[r - t] == znaki[r] == znaki[r + t] != '   ':
            w = 1

    print(' 7 │ 8 │ 9 \n'
          + linia +
          ' 4 │ 5 │ 6 \n'
          + linia +
          ' 1 │ 2 │ 3 \n')

    for i in range(9):
        znaki.append('   ')

    while w == 0:
        if runda % 2 == 0:
            pisz('X')
            o = 'X'
        else:
            pisz('O')
            o = 'O'
        druk()
        wygrana()
        runda += 1
        if runda == koniec:
            w = 2

    if w == 1:
        print('Gratulacje graczu ' + o + ' wygrales!!!')
    elif w == 2:
        print('Remis!!')

while True:
    gra()
    input('enter aby kontynuowac')
