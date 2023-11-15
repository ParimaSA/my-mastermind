check_password = '3336'
num_color = 6
num_position = 4
round = 0

print(f'Playing Mastermind with {num_color} colors and {num_position} positions')
while True:
    password = input('What is your guess?: ')
    print('Your guess is', password)
    set_pass = list(set(list(password)))
    position = 0
    color = 0
    for i in set_pass:
        # print(i)
        n = min(check_password.count(i), password.count(i))
        color += n
    for i in range(len(password)):
        if password[i] == check_password[i]:
            position += 1
    print('*' * position, 'o' * (color - position), sep='')
    print()
    round += 1

    if password == check_password:
        break

print(f'You solve it after {round} rounds')

