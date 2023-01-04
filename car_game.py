end_command = "quit"
run_command = input('> ')
while run_command != end_command:
    if run_command == "help" or run_command == "HELP":
        print("start - to start the car")
        print("stop - to stop the car")
        print("start - to exit")
        run_command = input('> ')
    elif run_command == "START" or run_command == "start":
        print("Car started... Ready to go" )
        run_command = input('> ')
    elif run_command == "STOP" or run_command == "stop":
        print("Car stopped" )
        run_command = input('> ')
    else:
        print("I don't understand")
        run_command = input('> ')
