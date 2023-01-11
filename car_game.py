command = input('> ')
is_started = False
while command != "quit":
    if command == "help":
        print('''
        start - to start the engine
        stop - to stop the engine
        quit - to exit   
        ''')
    elif command == "start":
        if is_started:
            print('car is already started!')
        else:
            is_started = True
            print("Car started... Ready to go")

    elif command == "stop":
        if not is_started:
            print('car is already stopped')
        else:
            is_started = True
            print("Car stopped")

    else:
        print("I don't understand")
    command = input('> ')




