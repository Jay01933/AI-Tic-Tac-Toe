import gameBoard
import player
import os
import datetime
import csv


def save_game_data(play1, play2=None, winner=None):
    date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    if play2 is None:
        play2_name = 'Computer'
        play2_number = ''
        play2_symbol = ''
    else:
        play2_name = play2.name
        play2_number = play2.no
        play2_symbol = play2.sym

    if winner is None:
        winner_name = ''
    else:
        winner_name = winner.name

    with open('gameData.csv', mode='a') as game_data_file:
        game_data_writer = csv.writer(game_data_file)
        game_data_writer.writerow([date_time, play1.name, play1.no, play1.sym, play2_name, play2_number, play2_symbol, winner_name])


def main():
    name = input("Enter your name: ")
    no = input('Enter your number: ')
    symbol = input("Enter your symbol: ")

    play1 = player.Player(name, no, symbol)
    again = 'YES'

    while again == 'YES':
        gb = gameBoard.Board(3, 3)

        print("\tOPTION")
        print("1: Check your SCORE\n2: Play with friend\n3: Play with computer( level Easy)\n4: Play with computer( level Hard)\n")
        print("Please chose 1 out of 4 option above:")
        choice = int(input())
        if choice == 1:
            print(play1.name + "'s Score: " + str(play1.score))
            again = input("You want to PLAY AGAIN? <yes/no> ").upper()
        if choice == 2:

            name2 = input("Enter the player 2 name: ")
            no2 = input('Enter the player 2 number: ')
            symbol2 = input("Enter the player 2 symbol: ")
            play2 = player.Player(name2, no2, symbol2)
            order = (input(play1.name + " want to play FIRST? < Yes/No>")).upper()
            if order == 'YES':
                while len(gb.emptySpot()) != 0:
                    print(play1.name + "'s turn")
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())

                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    print(play2.name + "'s turn")
                    t = play2.get_move(gb)
                    gb.makePlay(t[0], t[1], play2.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play2.sym):
                        print(play2.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play2.update_score(gb)
                        break
            else:
                while len(gb.emptySpot()) != 0:
                    print(play2.name + "'s turn")
                    t = play2.get_move(gb)
                    gb.makePlay(t[0], t[1], play2.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play2.sym):
                        print(play2.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play2.update_score(gb)
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    print(play1.name + "'s turn")
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break

        if choice == 3:
            c = player.WeakComputer()
            order = (input(play1.name + " want to play FIRST? < Yes/No>")).upper()
            if order == 'YES':

                while len(gb.emptySpot()) != 0:
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    pos = c.get_move(gb)
                    gb.makePlay(pos[0], pos[1], c.sym)
                    print(gb.printBoard())
                    if gb.checkWin(c.sym):
                        print(play1.name + ' lose !')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
            else:
                while len(gb.emptySpot()) != 0:
                    pos = c.get_move(gb)
                    gb.makePlay(pos[0], pos[1], c.sym)
                    print(gb.printBoard())
                    if gb.checkWin(c.sym):
                        print(play1.name + ' lose !')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break

        if choice == 4:
            c = player.SmartComputer(play1)
            order = (input(play1.name + " want to play FIRST? < Yes/No>")).upper()
            if order == 'YES':
                while len(gb.emptySpot()) != 0:
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    pos = c.get_move(gb)
                    print(pos)
                    gb.makePlay(pos[0], pos[1], c.sym)
                    print(gb.printBoard())
                    if gb.checkWin(c.sym):
                        print(play1.name + ' lose !')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
            else:
                while len(gb.emptySpot()) != 0:
                    pos = c.get_move(gb)
                    print(pos)
                    gb.makePlay(pos[0], pos[1], c.sym)
                    print(gb.printBoard())
                    if gb.checkWin(c.sym):
                        print(play1.name + ' lose !')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    if gb.checkTie():
                        print('Draw')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        break
                    t = play1.get_move(gb)
                    gb.makePlay(t[0], t[1], play1.sym)
                    print(gb.printBoard())
                    if gb.checkWin(play1.sym):
                        print(play1.name + ' won!')
                        again = input("You want to PLAY AGAIN? <yes/no> ").upper()
                        play1.update_score(gb)
                        break
    date_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    with open('gameData.csv', mode='a') as game_data_file:
        game_data_writer = csv.writer(game_data_file)
        game_data_writer.writerow([date_time, play1.name, play1.no, play1.sym, gb.checkWin(play1.sym)])





if __name__ == '__main__':
    main()