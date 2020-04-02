# !/usr/bin/python
# coding=utf-8
# importing the necessary packages
import os
import platform
import sys
import time
import webbrowser

a = ("""" \033[1;34m 
                                         
                                    -+dHJ5aGFyZGVyIQ==+-                                                                                                          
                                  `:sm⏣~~Destroy.No.Data~~s:`                                                                                                       
                                 -+h2~~Maintain.No.Persistence~~h+-                                                                                                   
                             `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`                                                                                                
                          ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.                                                                                            
                       -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+-                                                                                         
                      -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-                                                                                        
                      :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:                                                                                        
                      :we're.all.alike'`                     The.PFYroy.No.D7:                                                                                        
                      :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:                                                                                        
                      :msf>exploit -j.                       :Ns.BOB&ALICEes7:                                                                                        
                      :---srwxrwx:-.`                        `MS146.52.No.Per:                                                                                        
                      :<script>.Ac816/                        sENbove3101.404:                                                                                        
                      :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:                                                                                        
                      :09.14.2011.raid                       /STFU|wall.No.Pr:                                                                                        
                      :hevnsntSurb025N.                      dNVRGOING2GIVUUP:                                                                                        
                      :#OUTHOUSE-  -s:                       /corykennedyData:                                                                                        
                      :$nmap -oS                              SSo.6178306Ence:                                                                                        
                      :Awsm.da:                            /shMTl#beats3o.No.:                                                                                        
                      :Ring0:                             `dDestRoyREXKC3ta/M:                                                                                        
                      :23d:                               sSETEC.ASTRONOMYist:                                                                                        
                       /-                        /yo-    .ence.N:(){ :|: & };:                                                                                        
                                                 `:Shall.We.Play.A.Game?tron/                                                                                         
                                                 ```-ooy.if1ghtf0r+ehUser5`                                                                                           
                                               ..th3.H1V3.U2VjRFNN.jMh+.`                                                                                             
                                              `MjM~~WE.ARE.se~~MMjMs                                                                                                  
                                               +~KANSAS.CITY's~-`                                                                                                     
                                                J~HAKCERS~./.`                                                                                                        
                                                .esc:wq!:`                                                                                                            
                                                 +++ATH`\033[0m
 ______________________________________________________________________________
|                                                                              |
|\033[32m coded By : Abdullah Al-hajj | github : www.facebook.com/torgodly | @torgodly \033[0m|
|______________________________________________________________________________|""")
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
s = '\033[0m' #stop

print(g + "[+] Please enter a target ID or username (e.g. 10000xxxxxxxxx).\n" + s)
fp_id_1 = str(raw_input(g + 'FBI' + s + '' + r + '>>' + s + '' + g + 'infoG' + s + '' + r + '>>' + s))
if " " in fp_id_1:
    os.system(clear)
    print('')
    print(br + 'ERROR 406 Not Acceptable\n' + s) # put sqyar
    exit(0)
os.system(clear)
while True:
    try:
        print(a)

        print('''
%s1) target profile 
2) Overview
3) Work and Education
4) Places
5) Contact and Basic Info
6) Family and Relationships
7) Details About target
8) Life Events
9) target frinds
10) target photos
11) target Videos
12) target Check-Ins
13) Apps and Games 
14) target Instagram
15) likes %s
        ''') % (g, s)

        target = int(input(g + 'FBI' + s + '' + r + '>>' + s + '' + g + 'infoG' + s + '' + r + '>>' + s + g + fp_id_1 + s + r + '>>' + s))
        print('')
        if target == 1:
            load_animation("loading it might take 5s ... ")
            webbrowser.open_new_tab('www.facebook.com/'+fp_id_1)
            os.system(clear)


        elif target == 2:
            load_animation("loading it might take 5s ... ")
            webbrowser.open_new_tab('www.facebook.com/'+ fp_id_1 +'/about?section=overview&lst=100006524050777%3A100006524050777%3A1585746104')
            os.system(clear)


        elif target == 3:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('https://www.facebook.com/'+ fp_id_1 +'/about?section=education&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)

        elif target == 4:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+ fp_id_1 +'/about?section=living&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)


        elif target == 5:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/about?section=contact-info&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)


        elif target == 6:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/about?section=relationship&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)


        elif target == 7:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/about?section=bio&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)


        elif target == 8:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/about?section=year-overviews&lst=100006524050777%3A100006524050777%3A1585746104', new=2)
            os.system(clear)


        elif target == 9:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/friends?lst=100006524050777%3A100006524050777%3A1585746712&source_ref=pb_friends_tl', new=2)
            os.system(clear)


        elif target == 10:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/photos?lst=100006524050777%3A100006524050777%3A1585746829', new=2)
            os.system(clear)

        elif target == 11:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/videos?lst=100006524050777%3A100006524050777%3A1585747147', new=2)
            os.system(clear)


        elif target == 12:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/' + fp_id_1 +'/map?lst=100006524050777%3A100006524050777%3A1585747147', new=2)
            os.system(clear)


        elif target == 13:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/'+fp_id_1+'/games?lst=100006524050777%3A100006524050777%3A1585747147', new=2)
            os.system(clear)

        elif target == 14:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/' + fp_id_1 +'/app_instapp?lst=100006524050777%3A100006524050777%3A1585746992', new=2)
            os.system(clear)

        elif target == 15:
            load_animation("loading it might take 5s ... ")
            webbrowser.open('www.facebook.com/' + fp_id_1 +'/likes_all', new=2)
            os.system(clear)
        else:
            os.system(clear)
            print(br + 'ERROR 404 Not Found \n' + s)
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
        exit()

