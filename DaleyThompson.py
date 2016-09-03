from microbit import *

r1 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    ' 9 9 \n'
    '9   9')
r2 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    ' 9 9 \n'
    '9  9 ')
r3 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    '  99 \n'
    ' 99  ')
r4 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    '  9  \n'
    '  9  ')
r5 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    '  99 \n'
    ' 9 9 ')
r6 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    ' 9 9 \n'
    '9  9 ')
r7 = Image(
    '  9  \n'
    ' 999 \n'
    '  9  \n'
    ' 9 9 \n'
    '9   9')

anim = [r1, r2, r3, r4, r5, r6, r7]
index = 0
delay = 500
while True:
    while index < len(anim):
        display.print(anim[index])
        sleep(delay)
        index += 1
    chance = 0
    success = False
    while chance < delay and not success:
        if button_a.is_pressed():
            delay -= 100
            chance = delay+1
            success = True
        else:
            sleep(10)
        chance += 10
    if not success:
        delay = 500
    index = 0
