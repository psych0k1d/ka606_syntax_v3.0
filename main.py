from distutils.command.check import check
import keyboard as kb
from time import sleep


#oleg....
key = ("f10")


def deley(fps=0.01):
    sleep(fps)


def prog(var1="", var2=2):
    for x in range(1, var2):
        kb.press("backspace")
        print("r")
    kb.write(f"{var1}")

def waiter():
    deley(0.5)
    run = True
    while run:
        print("waiter")
        deley()
        if kb.is_pressed(key):
            deley(0.5)
            break


def main():
    run = True
    checker = 0
    while run:
        deley()

        #switcher
        if kb.is_pressed(key):
            print("switch")
            waiter()

        if kb.is_pressed("backspace"):
            prog(var2=checker)
            checker = 0
        if kb.is_pressed("q"):
            checker = 1
            prog("u")
        if kb.is_pressed("w"):
            checker = 2
            prog("U,")
        if kb.is_pressed("e"):
            checker = 1
            prog("Y")
        if kb.is_pressed("r"):
            checker = 1
            prog("K")
        if kb.is_pressed("t"):
            checker = 1
            prog("e")
        if kb.is_pressed("y"):
            checker = 1
            prog("H")
        if kb.is_pressed("u"):
            checker = 1
            prog("r")
        if kb.is_pressed("i"):
            checker = 3
            prog("LLI")
        if kb.is_pressed("o"):
            checker = 4
            prog("LLI,")
        if kb.is_pressed("p"):
            checker = 1
            prog("3")
        if kb.is_pressed("["):
            checker = 1
            prog("x")
        if kb.is_pressed("]"):
            checker = 2
            prog("`b")
        if kb.is_pressed("a"):
            checker = 2
            prog("qp")
        if kb.is_pressed("s"):
            checker = 2
            prog("bl")
        if kb.is_pressed("d"):
            checker = 1
            prog("B")
        if kb.is_pressed("f"):
            checker = 1
            prog("a")
        if kb.is_pressed("g"):
            checker = 2
            prog("I7")
        if kb.is_pressed("h"):
            checker = 1
            prog("P")
        if kb.is_pressed("j"):
            checker = 1
            prog("o")
        if kb.is_pressed("k"):
            checker = 2
            prog("Jl")
        if kb.is_pressed("l"):
            checker = 1
            prog("D")
        if kb.is_pressed(";"):
            checker = 3
            prog("}I{")
        if kb.is_pressed("'"):
            checker = 1
            prog("E")
        if kb.is_pressed("z"):
            checker = 2
            prog("9l")
        if kb.is_pressed("x"):
            checker = 1
            prog("4")
        if kb.is_pressed("c"):
            checker = 1
            prog("c")
        if kb.is_pressed("v"):
            checker = 1
            prog("M")
        if kb.is_pressed("b"):
            checker = 1
            prog("u")
        if kb.is_pressed("n"):
            checker = 1
            prog("T")
        if kb.is_pressed("m"):
            checker = 1
            prog("b")
        if kb.is_pressed(","):
            checker = 1
            prog("6")
        if kb.is_pressed("."):
            checker = 3
            prog("I-0")
        if kb.is_pressed("`"):
            checker = 1
            prog("e")

if __name__ == "__main__":
    main()