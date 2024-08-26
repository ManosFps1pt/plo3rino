with open("gcode", "r") as f:
    file = f.read()
commands = file.split("\n")
instructions = []
for command in commands:
    splited = command.split(" ")
    func = splited[0]
    args = splited[1:]
    print(func, args)

