from colorama import Fore, Back, Style

state = True
def returnError(message):
    print(Fore.BLACK + Back.RED + f'ERR: {message}')
    print(Style.RESET_ALL)


def returnWarning(message):
    print(Back.YELLOW + f'WARN: {message}')
    print(Style.RESET_ALL)


def reset():
    state = 0

def errorUpdate(severity, Errortype):
    severity = state
    if severity == 0:
        returnWarning(Errortype)
    else:
        returnError(Errortype)


def errorCheck():
    if state == 0:
        return True
    else:
        return False
