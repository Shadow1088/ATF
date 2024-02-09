import pyautogui as pag
import time

index = 0
shift = False

keys = {"q": (691,793), "w":(740,793), "e":(789,793), "r":(838,793),
        "t":(887,793), "z":(936,793), "u":(985,793), "i":(1034,793),
        "o":(1083,793), "p":(1132,793), "a":(715,842), "s":(764,842),
        "d":(813,842), "f":(862,842), "g":(911,842), "h":(960,842),
        "j":(1009,842), "k":(1058,842), "l":(1107,842), "y":(739,891),
        "x":(788,891), "c":(837,891), "v":(886,891), "b":(935,891),
        "n":(984,891), "m":(1033,891), "space":(862,940),
        "backspace":(1304,752),"shift":(666,888), "ú":(1190,790), ".":(1130,888),}
# "shift2":(1300,890)

print("Welcome to my automatic ATF exploit. Please make sure you have the ATF Online open and ready to use before continuing.")
print("\nNOTICE!!\nThis program does not type other letters than from english alphabet. If other character occurs, write it manually.")
print("The program slow down drastically, when theres a uppercase letter. Its not stuck, its just slow.")
print("Only way to slow down this program is to wait before typing the manual characters.")
print("Are you ready? ('y' to continue)")
ready = input()

if ready == "y":

    print("You now have five seconds to swicth to the ATF Online")
    time.sleep(5)

    while ready:
        px = pag.screenshot()
        for key, value in keys.items():
            # is shift pressed?
            if px.getpixel((666,888))[2] > 150 and px.getpixel((666,888))[2] < 240 and px.getpixel((666,888))[1] < 200:
                pag.keyDown("shift")
                shift = True
            elif px.getpixel((1300,890))[2] > 150 and px.getpixel((1300,890))[2] < 240 and px.getpixel((1300,890))[1] < 200:
                pag.keyDown("shift")
                shift = True

            # if the pixel is blue, press the key
            if px.getpixel(value)[2] > 150 and px.getpixel(value)[2] < 240 and px.getpixel(value)[1] < 200:
                pag.press(key)

            # if shift was pressed, release it
            if shift:
                pag.keyUp("shift")
                shift = False

                
        
