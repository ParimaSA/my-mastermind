import random
import random
import sys


class Mastermind:
    def __init__(self, num_color=6, num_position=4):
        self.num_color = num_color
        self.num_position = num_position
        self.__set_up_answer()
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

    def __set_up_answer(self):
        new_answer = ''
        for i in range(self.num_position):
            n = random.randint(1,self.num_color)
            new_answer += str(n)
        self.answer = new_answer

    def __display_hint(self, color, position):
        print('*' * position, 'o' * (color - position), sep='')

    def __get_hint(self, guess):
        correct_color = 0
        correct_position = 0
        set_guess = set(list(guess))
        for i in set_guess:
            n = min(self.answer.count(i), guess.count(i))
            correct_color += n
        for i in range(len(guess)):
            if guess[i] == self.answer[i]:
                correct_position += 1
        self.__display_hint(correct_color, correct_position)

    def __check_guess(self, guess):
        guess = list(set(list(guess)))
        check = 0
        for character in guess:
            if int(character) not in range(1,self.num_color+1):
                check = -1
        if check == -1:
            print('WARNING!!: There are colors out of range.')

    def determine_end(self, guess):
        return self.answer == guess

    def play_game(self, name = ''):
        print()
        print('Input q if you want to exit.')
        print(f'Playing Mastermind with {self.num_color} colors(1-{self.num_color}) and {self.num_position} positions')
        self.__set_up_answer()
        round = 0
        if name == '':
            name = input('Enter your name: ')
        while True:
            guess = input('What is your guess?: ')
            print('Your guess is', guess)
            if guess == 'q':
                self.menu()
            if len(guess) != self.num_position:
                print('WARNING!!: Incorrect position\n')
                continue
            self.__get_hint(guess)
            self.__check_guess(guess)
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
            self.play_game(name)
        else:
            self.menu()

    def display_history(self):
        print()
        print('History')
        if len(self.history) == 0:
            print('There is no history')
            self.menu()
        rank1 = ''
        min_score = 1000000000000000000000000
        for person in self.history:
            print(f'Player {person["name"]} \tfinished in {person["score"]} round')
            if person['score'] < min_score:
                rank1 = person['name']
                min_score = person['score']
        print()
        print(f'Rank#1st Player {rank1} finished in {min_score} round')
        self.menu()

    def display_rule(self):
        print()
        print('How to play Mastermind?')
        print('The objective of the game is to guess the exact positions of the numbers in the sequence.')
        print('Hint:')
        print('    A star * indicates that there is a color that is positioned correctly.')
        print('    A letter o indicates that there is a color that is positioned incorrectly.')
        print('The game is played on until a player successfully solves the puzzle')
        self.menu()

    def menu(self):
        print()
        print('Mastermind Game')
        print('1.Play Game')
        print('2.Set up Game')
        print('3.Show History')
        print('4.Rules')
        print('0.Exit Game')
        ans_list = ['1', '2', '3', '4', '0']
        ans = input('Your Choice: ')
        while ans not in ans_list:
            ans = input('Your Choice: ')
        if ans == '1':
            self.play_game()
        elif ans == '2':
            self.set_up_game()
        elif ans == '3':
            self.display_history()
        elif ans == '4':
            self.display_rule()
        else:
            sys.exit()


my_game = Mastermind()
my_game.menu()




