from colorama import Fore, Back, Style


def returnError(message):
    print(Fore.BLACK + Back.RED + f'ERR: {message}')
    print(Style.RESET_ALL)


def returnWarning(message):
    print(Back.YELLOW + f'WARN: {message}')
    print(Style.RESET_ALL)
