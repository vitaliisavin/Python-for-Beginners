msg_ = ["Enter an equation",
        "Do you even know what numbers are? Stay focused!",
        "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
        "Yeah... division by zero. Smart move...",
        "Do you want to store the result? (y / n):",
        "Do you want to continue calculations? (y / n):",
        " ... lazy",
        " ... very lazy",
        " ... very, very lazy",
        "You are",
        "Are you sure? It is only one digit! (y / n)",
        "Don't be silly! It's just one number! Add to the memory? (y / n)",
        "Last chance! Do you really want to embarrass yourself? (y / n)"]

x, oper, y = '', '', ''
memory = 0.0
result = 0.0


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == '*':
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == '*' or v3 == '+' or v3 == '-'):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)


while True:
    print(msg_[0])
    x, oper, y = input().split()

    if x == "M":
        x = memory
    if y == "M":
        y = memory

    try:
        x = float(x)
        y = float(y)
    except ValueError:
        print(msg_[1])
        continue

    if oper == '+' or oper == '-' or oper == '*' or oper == '/':
        check(x, y, oper)
        if oper == '+':
            result = x + y
            print(result)
        elif oper == '-':
            result = x - y
            print(result)
        elif oper == '*':
            result = x * y
            print(result)
        elif oper == '/':
            try:
                result = x / y
                print(result)
            except ZeroDivisionError:
                print(msg_[3])
                continue
    else:
        print(msg_[2])

    while True:
        print(msg_[4])
        answer = input()
        if answer == 'y':
            if is_one_digit(result):
                msg_index = 10
                while True:
                    print(msg_[msg_index])
                    answer_digit = input()
                    if answer_digit == 'y':
                        if msg_index < 12:
                            msg_index += 1
                            continue
                        else:
                            memory = result
                            break
                    elif answer_digit == 'n':
                        break
            else:
                memory = result
            break
        elif answer == 'n':
            break

    while True:
        print(msg_[5])
        answer = input()
        if answer == 'y':
            break
        elif answer == 'n':
            exit()
