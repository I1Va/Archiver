import sys
import vige
import hapal


args = sys.argv[1:]

if len(args) == 3:
    ty, name, word = args[0], args[1], args[2]
    try:
        f = open(name)
    except FileNotFoundError:
        print(f"Не найден указанный файл (возможно вы имели в виду: sample/{name})")

    vige.action(name, word, ty)
else:
    ty, name = args[0], args[1]
    try:
        f = open(name)
    except FileNotFoundError:
        print(f"Не найден указанный файл (возможно вы имели в виду: sample/{name})")
    hapal.action(name, ty)
