import time
import platform,os
clear = ""
if "Windows" in platform.system():
    clear = ("cls")
if "Linux" in platform.system():
    clear = ("clear")
os.system(clear)
#collers
g = '\033[1;32m' #green
r = '\033[1;31m' #red
br = '\033[1;5;31m' #blinking red
s = '\033[0m'

try:
    from dbs import banners
    print('''
%s1) information gathering 
2) report links
3) information about yourself%s
    ''') % (g, s)

    type_of_info = int(input(g + 'FBI' + s + '' + r + '>>' + s))


    if type_of_info == 1:
        os.system(clear)
        from dbs import infoG

    elif type_of_info == 2:
        os.system(clear)
        from dbs import reportlinks

    elif type_of_info == 3:
        os.system(clear)
        from dbs import comingsoon

    else:
        os.system(clear)
        print('')
        print(br + 'ERROR 404 Not Found \n' + s) # put sqayr
        exit()
except SyntaxError:
    print(br + 'ERROR 404 Not Found \n' + s)
    exit()
except NameError:
    print(br + 'ERROR 404 Not Found \n' + s)
    exit()
except KeyboardInterrupt:
    print('\n')
    print(br + 'Exit ... \n' + s)
    time.sleep(1)
    exit()





