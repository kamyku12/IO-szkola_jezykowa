import logowanie
import menu

def main():
    logged = False
    typ = None
    while 1:
        if logged:
            menu.menu(typ)
            break
        else:
            logged, typ = logowanie.logowanie()


if __name__ == '__main__':
    main()
