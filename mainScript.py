import pyautogui as pag
import time
from pynput.keyboard import Controller

keyboard = Controller()

keys = {"e":(789,793), "a":(715,842), "r":(838,793), "i":(1034,793), "o":(1083,793),
        "t":(887,793), "n":(984,891), "s":(764,842), "l":(1107,842), "c":(837,891),
        "u":(985,793), "d":(813,842), "p":(1132,793), "m":(1033,891), "h":(960,842),
        "g":(911,842), "b":(935,891), "f":(862,842), "y":(739,891), "w":(740,793),
        "k":(1058,842), "v":(886,891), "x":(788,891), "z":(936,793), "j":(1009,842),
        "q": (691,793), " ":(862,940), ",":(1180,888), ".":(1130,888),
        "á":(1010,740), "í":(1066,747), "é":(1115,741), "ú":(1190,790),
        "ý":(966,741), "ů":(1168,841), "č":(812,741), "š":(760,741),
        "ě":(709,741), "ř":(865,741), "ž":(911,741)}


# keys = {"q": (691,793), "w":(740,793), "e":(789,793), "r":(838,793),
#         "t":(887,793), "z":(936,793), "u":(985,793), "i":(1034,793),
#         "o":(1083,793), "p":(1132,793), "a":(715,842), "s":(764,842),
#         "d":(813,842), "f":(862,842), "g":(911,842), "h":(960,842),
#         "j":(1009,842), "k":(1058,842), "l":(1107,842), "y":(739,891),
#         "x":(788,891), "c":(837,891), "v":(886,891), "b":(935,891),
#         "n":(984,891), "m":(1033,891), " ":(862,940), ",":(1180,888),
#         "ú":(1190,790), ".":(1130,888), "á":(1010,740), "í":(1066,747),
#         "č":(812,741), "š":(760,741), "ě":(709,741), "ř":(865,741),
#         "ž":(911,741), "ý":(966,741), "é":(1115,741), "ů":(1168,841),}

def is_blue_pixel(px, coords):
    return px.getpixel(coords)[2] > 150 and px.getpixel(coords)[2] < 240 and px.getpixel(coords)[1] < 200

def press_shift_if_needed(px):
    if is_blue_pixel(px, (666,888)) or is_blue_pixel(px, (1300,890)):
        pag.keyDown("shift")
        return True
    return False

print("Welcome to my automatic ATF exploit. Please make sure you have the ATF Online open and ready to use before continuing.")
print("\nNOTICE!!\nThis program does not type other letters than from english alphabet. If other character occurs, write it manually.")
print("The program slow down drastically, when theres a uppercase letter. Its not stuck, its just slow.")
print("Only way to slow down this program is to wait before typing the manual characters.")
print("Are you ready? ('y' to continue)")
ready = input()

if ready.lower() == "y":
    print("You now have five seconds to switch to the ATF Online")
    time.sleep(5)

    while True:
        px = pag.screenshot()
        shift_pressed = False
        for key, value in keys.items():
            shift_pressed = press_shift_if_needed(px)
            if is_blue_pixel(px, value):
                keyboard.type(key)
            if shift_pressed:
                pag.keyUp("shift")
        time.sleep(0.2)
        
