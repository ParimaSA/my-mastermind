import random
import random
import sys


class Mastermind:
    def __init__(self, num_color=4, num_position=6):
        self.num_color = num_color
        self.num_position = num_position
        self.set_up_answer()
        self.history = []

    def set_up_game(self):
        print()
        print(f'Now there are {self.num_color} colors and {self.num_position} position')
        check = input('You want to change colors or position (c/p)?: ')
        while check not in ['c', 'p']:
            check = input('You want to change colors or position (c/p)?: ')

        if check == 'c':
            n = input('Change colors to(1-8): ')
            while n not in list('12345678'):
                n = input('Change colors to(1-8): ')
            self.num_color = int(n)
        else:
            n = input('Change positions to(1-10): ')
            while n not in list('123456789') + ['10']:
                n = input('Change positions to(1-10): ')
            self.num_position = int(n)

        print(f'Now there are {self.num_color} colors and {self.num_position} position')

        again = input('Do you want to change more (y/n)?: ')
        while again not in ['y', 'n']:
            again = input('Do you want to change more (y/n)?: ')
        if again == 'y':
            self.set_up_game()
        else:
            self.menu()

    def set_up_answer(self):
        new_answer = ''
        for i in range(self.num_position):
            n = random.randint(1,self.num_color)
            new_answer += str(n)
        self.answer = new_answer

    def play_game(self):
        print()
        print(f'Playing Mastermind with {self.num_color} colors and {self.num_position} positions')
        self.set_up_answer()
        round = 0
        while True:
            position = 0
            color = 0
            password = input('What is your guess?: ')
            print('Your guess is', password)
            set_pass = list(set(list(password)))
            for i in set_pass:
                n = min(self.answer.count(i), password.count(i))
                color += n
            for i in range(len(password)):
                if password[i] == self.answer[i]:
                    position += 1
            print('*' * position, 'o' * (color - position), sep='')
            print()
            round += 1
            if self.answer == password:
                break
        print(f'You solve it after {round} rounds')

        again = input('Do you want to play again (y/n)?: ')
        while again not in ['y', 'n']:
            again = input('Do you want to play again (y/n)?: ')
        if again == 'y':
            self.play_game()
        else:
            self.menu()

    def display_history(self):
        pass

    def menu(self):
        print()
        print('Mastermind Game')
        print('1.Play Game')
        print('2.Set up Game')
        print('3.Show History')
        print('4.Exit Game')
        ans_list = ['1', '2', '3', '4']
        ans = input('Your Choice: ')
        while ans not in ans_list:
            ans = input('Your Choice: ')
        if ans == '1':
            self.play_game()
        elif ans == '2':
            self.set_up_game()
        elif ans == '3':
            self.display_history()
        else:
            sys.exit()

my_game = Mastermind()
my_game.menu()
# print(list('123456789'))




