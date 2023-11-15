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

    def display_hint(self, color, position):
        print('*' * position, 'o' * (color - position), sep='')

    def get_hint(self, guess):
        correct_color = 0
        correct_position = 0
        set_guess = set(list(guess))
        for i in set_guess:
            n = min(self.answer.count(i), guess.count(i))
            correct_color += n
        for i in range(len(guess)):
            if guess[i] == self.answer[i]:
                correct_position += 1
        self.display_hint(correct_color, correct_position)

    def check_guess(self, guess):
        guess = list(set(list(guess)))
        check = 0
        for character in guess:
            if int(character) not in range(1,self.num_color+1):
                check = -1
        if check == -1:
            print('WARNING!!: There are colors out of range.')

    def determine_end(self, guess):
        return self.answer == guess

    def play_game(self):
        print()
        print('Input q if you want to exit.')
        print(f'Playing Mastermind with {self.num_color} colors and {self.num_position} positions')
        self.set_up_answer()
        round = 0
        name = input('Enter your name: ')
        while True:
            guess = input('What is your guess?: ')
            print('Your guess is', guess)
            if guess == 'q':
                self.menu()
            if len(guess) != self.num_position:
                print('WARNING!!: Incorrect position\n')
                continue
            self.get_hint(guess)
            self.check_guess(guess)
            print()
            round += 1
            if self.determine_end(guess):
                break
        print('Yeahh!! You WIN.')
        print(f'{name} solve it after {round} rounds')
        self.history.append({'name':name, 'score':round})

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




