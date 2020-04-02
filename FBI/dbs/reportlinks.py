# !/usr/bin/python
# coding=utf-8
# importing the necessary packages
import time
import sys
import os
import webbrowser
import platform

a = ("""\033[0;36m

                                 

                    █████▒    ▄▄▄▄       ██▓
                  ▓██   ▒    ▓█████▄    ▓██▒
                  ▒████ ░    ▒██▒ ▄██   ▒██▒
                  ░▓█▒  ░    ▒██░█▀     ░██░
                  ░▒█░       ░▓█  ▀█▓   ░██░
                   ▒ ░       ░▒▓███▀▒   ░▓  
                   ░         ▒░▒   ░     ▒ ░
                   ░ ░        ░    ░     ▒ ░
                              ░          ░  
                                   ░        

  
\033[0m                                                     
                                                     
 ______________________________________________________________________________
|                                                                              |
|\033[32m coded By : Abdullah Al-hajj | github : www.facebook.com/torgodly | @torgodly \033[0m|
|______________________________________________________________________________|                                                     
                                                     
                                                 

""")

# Function for implementing the loading animation
def load_animation(load_str):

    #collers
    YE = '\033[1;33m'  # blinking green
    s = '\033[0m'

    # String to be displayed when the application is loading
    ls_len = len(load_str)

    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
    counttime = 0
    i = 0
    while (counttime != 18):

        time.sleep(0.075)

        load_str_list = list(load_str)

        x = ord(load_str_list[i])

        y = 0

        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa
        if x != 32 and x != 46:
            if x > 90:
                y = x - 32
            else:
                y = x + 32
            load_str_list[i] = chr(y)

        # for storing the resultant string
        res = ''
        for j in range(ls_len):
            res = res + load_str_list[j]

        # displaying the resultant string
        sys.stdout.write("\r" + YE + res + s + animation[anicount])
        sys.stdout.flush()

        # Assigning loading string
        # to the resultant string
        load_str = res

        anicount = (anicount + 1) % 4
        i = (i + 1) % ls_len
        counttime = counttime + 1

#clear command
if 'Windows' in platform.system():
    clear = ('cls')
if 'Linux' in platform.system():
    clear = ('clear')

#collers
g = '\033[1;32m' #green
r = '\033[1;31m' #red
b = '\033[5m' #blimking
br = '\033[1;5;31m' #blinking red
s = '\033[0m'

while 1:
    try:
        print(a)
        print('\n'
              '%s1) Report dead person \n'
              '2) Report An inmate\'s\n'
              '3) Report an underage user\n'
              '4) Report an Impostor\n'
              '5) Child Data Request\n'
              '6) Requesting Content From a Deceased Person\n'
              '7) Account Removal Request for a Medically Incapacitated Person\n'
              '8) Give Us Feedback About a Facebook Feature%s\n'
              '        ') % (g, s)
        target = int(input(g + 'FBI' + s + '' + r + '>>' + s + '' + g + 'reportlinks' + s + '' + r + '>>' + s))
        print('')
        if target == 1:
            load_animation("loading ... ")
            webbrowser.open('http://www.facebook.com/help/contact/228813257197480', new=2)
            os.system(clear)


        elif target == 2:
            load_animation("loading ... ")
            webbrowser.open('http://www.facebook.com/help/contact/564493676910603', new=2)
            os.system(clear)


        elif target == 3:
            load_animation("loading ... ")
            webbrowser.open('http://www.facebook.com/help/contact/209046679279097', new=2)
            os.system(clear)

        elif target == 4:
            load_animation("loading ... ")
            webbrowser.open('https://www.facebook.com/help/contact/169486816475808', new=2)
            os.system(clear)


        elif target == 5:
            load_animation("loading ... ")
            webbrowser.open('http://wwww.facebook.com/help/contact/174263416008051', new=2)
            os.system(clear)


        elif target == 6:
            load_animation("loading ... ")
            webbrowser.open('https://www.facebook.com/help/contact/398036060275245', new=2)
            os.system(clear)


        elif target == 7:
            load_animation("loading ... ")
            webbrowser.open('https://www.facebook.com/help/contact/191122007680088', new=2)
            os.system(clear)


        elif target == 8:
            load_animation("loading ... ")
            webbrowser.open('https://www.facebook.com/help/contact/268228883256323', new=2)
            os.system(clear)

        else:
            print (br + 'ERROR 404 Not Found \n' + s) # put arun it sqayr
            exit()
    except SyntaxError:
        print(br + 'ERROR 404 Not Found \n' + s)
        exit()
    except NameError:
        print(br + 'ERRrOR 404 Not Found \n' + s)
        exit()
