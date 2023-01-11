#In this game, a user tries to guess a secret number that has already been predetermined. They get a particular number of trials. After each trial, they know if they're successful or failed. If their guess is higher than the secret number they'll know and likewise if it's lower. zthe game ends when the user gets their guess right or if they exhaust their trials.

secret_number = 45
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess_number = int(input("Guess a number between 1 - 100 "))
    if guess_number != secret_number:
        if guess_number < secret_number:
            print('Your guess is greater than the secret number')
            print(f'You have {guess_limit - guess_count - 1} trial left')

        if guess_number > secret_number:
            print('Your guess is greater than the secret number')
            print(f'You have {guess_limit - guess_count - 1} trial left')
    else:
        print("Yaay... You're right!!")
        break
    guess_count += 1

print("Play again")