"""
Viikko 12 Vaativat
Miika Toivanen
miika.toivanen@edu.sasky.fi
"""

from datetime import datetime
import os

clear = lambda: os.system('clear')

def t1():
    aineet = [
        ['APPELSIINI', '2', '1.99'],
        ['OLIIVIÖLJY', '1', '10.99'],
        ['TOMAATTIOS', '2.6', '1.29'],
        ['MAITO ', '1', '3.45'],
        ['VOI ', '1', '2.99'],
        ['LOHI ', '1', '1.69'],
        ['JUUSTO 500 g ', '2', '4.99']
    ]
    pvm = datetime(2026, 11, 12, 16, 56)
    hinta_yht = 0

    print('\n'+pvm.strftime("%d.%m.%y @ %H:%M"))
    print('--------------------------------')

    i = 1
    for t in aineet:
        tp = float(t[1]) * float(t[2])
        hinta_yht += tp
        print(f'{i} - {t[0]}'.ljust(18) + f'€ {round(tp, 2)}')
        print(f'{"":<3}'+f'{float(t[1])} @ € {t[2]}')
        i += 1

    print('--------------------------------')
    print(f'{"":<9}'+f'YHTEENSÄ € {round(hinta_yht, 2)}')

    
def t2():
    vuoro = ['X', 'O']
    vi = 0
    board = [
        [7, 8, 9],
        [4, 5, 6],
        [1, 2, 3]
    ]
    X_score = []
    O_score = []


    def print_game():
        print('o-----------------------------o')
        print('|       RISTINOLLAPELI        |')
        print('o-----------------------------o')
        print('o-----------------------------o')
        for b in board:
            print(f'{"":<10}'+f'{b[0]} | {b[1]} | {b[2]}')
            if board.index(b) < 2:
                print(f'{"":<10}----------')    
        print('o-----------------------------o')


    while True:
        clear() # kommentoi tämä rivi jos ei toimi..
        print_game()
        num = input(f'{vuoro[vi]} vuoro, valitse numero (1, 9): ').strip()

        if num.isdigit():
            num = int(num)
            if num > 0 and num < 10:
                for i in range(0, 3):
                    for o in range(0, 3):
                        if board[i][o] == num:

                            if vuoro[vi] == 'X':
                                X_score.append(board[i][o])
                            else:
                                O_score.append(board[i][o])

                            board[i][o] = vuoro[vi]
                            if vi == 0:
                                vi = 1
                            else:
                                vi = 0

        for score in [X_score, O_score]:
            game_end = False
            if 1 in score and 2 in score and 3 in score:
                game_end = True
            elif 4 in score and 5 in score and 6 in score:
                game_end = True
            elif 7 in score and 8 in score and 9 in score:
                game_end = True

            elif 1 in score and 5 in score and 9 in score:
                game_end = True
            elif 7 in score and 5 in score and 3 in score:
                game_end = True

            elif 1 in score and 4 in score and 7 in score:
                game_end = True
            elif 2 in score and 5 in score and 8 in score:
                game_end = True
            elif 3 in score and 6 in score and 9 in score:
                game_end = True

            if game_end:
                print_game()
                if vi == 0:
                    vi = 1
                else:
                    vi = 0

                print('o-----------------------------o')
                print('|         PELI LOPPUI!        |')
                print('|          VOITTAJA:          |')
                print(f'|              {vuoro[vi]}              |')
                print('o-----------------------------o')
                exit()



            


        


def main():
    # vaativa tehtävä 1
    # t1()
    # vaativa tehtävä 2
    t2()

if __name__ == "__main__":
    main()