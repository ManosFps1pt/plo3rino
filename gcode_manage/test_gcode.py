def decode_gcode(functions: tuple):
    with open("../gcode", "r") as f:
        file = f.read()
    commands = file.split("\n")
    for command in commands:
        split = command.split(" ")
        func = split[0]
        args = split[1:]
        for function in functions:
            if func == function.__name__:
                function(*args)
                break
        else:
            print(f"Invalid function: {func}")




