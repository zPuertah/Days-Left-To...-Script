from dataclasses import replace
import datetime
from pystyle import Anime, System, Colorate, Colors, Center
from time import sleep
from alive_progress import alive_bar




#art Zone


logo = '''
#################################################################
#  ███████╗██████╗ ██╗   ██╗███████╗██████╗ ████████╗ █████╗    #
#  ╚══███╔╝██╔══██╗██║   ██║██╔════╝██╔══██╗╚══██╔══╝██╔══██╗   #
#    ███╔╝ ██████╔╝██║   ██║█████╗  ██████╔╝   ██║   ███████║   #
#   ███╔╝  ██╔═══╝ ██║   ██║██╔══╝  ██╔══██╗   ██║   ██╔══██║   #
#  ███████╗██║     ╚██████╔╝███████╗██║  ██║   ██║   ██║  ██║   #
#  ╚══════╝╚═╝      ╚═════╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝   #
#################################################################
'''

tree = '''
                                   .
                                  . .
                                 .' 0.
                                .' * '.
                               .' * 0 '.
                              .' *   * '.
                             .' #  * 0  '.
                            .'  *  0   * '.
                           .'  *   *    0 '.
                          .' 0  * 0    * # '.
                         .'  *   HAPPY    * '.
                        .' 0    CRISTMAS   * '.
                       .'     *   AND   *   0 '.
                      .'  *    PROSPEROUS  *   '.
                     .' 0      NEW   YEAR    0  '.
                    .'  0  * 0    *      *    *  '.
                   .' #    #  *  *  0 #   *  0    '.
                  .'   *    0    *    *   0    *   '.
                 .'0 #     *    #  *  0    *  0     '.
                .'    *  0  #  *      0  #       *   '.
               .'________________#   #________________'.
                                 #   #
                                 #   #
                                 #   #
     ------------------------------------------------------------ 
'''[1:]
Heart = '''
 XOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOX
O:::::::::::::::::::::::::::::::::::::::::::::::::::::::O
X:::::::::::::::::::::::::::::::::::::::::::::::::::::::X
O::::::::::::           :::::::::           ::::::::::::O
X:::::::::                :::::                :::::::::X
O:::::::       *********    :    *********       :::::::O
X:::::      *****     *****   *****     *****      :::::X
O::::     ****           *******           ****     ::::O
X:::     ****              ***              ****     :::X
O:::     ****               *               ****     :::O
X::::     ****      HAPPY VALENTINE´S      ****     ::::X
O:::::     ****            DAY            ****     :::::O
X:::::::     ****                       ****     :::::::X
O:::::::::     ****                   ****     :::::::::O
X:::::::::::     ****               ****     :::::::::::X
O::::::::::::::     ****         ****     ::::::::::::::O
X:::::::::::::::::     ****   ****     :::::::::::::::::X
O::::::::::::::::::::     *****     ::::::::::::::::::::O
X:::::::::::::::::::::::    *    :::::::::::::::::::::::X
O:::::::::::::::::::::::::     :::::::::::::::::::::::::O
X::::::::::::::::::::::::::: :::::::::::::::::::::::::::X
O:::::::::::::::::::::::::::::::::::::::::::::::::::::::O
X:::::::::::::::::::::::::::::::::::::::::::::::::::::::X
OXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXOXO 
'''[1:]

Pumpkin = '''
                  ___                                           ___
               ___)__|_                                      ___)__|_
          .-*'          '*-,                             .-*'          '*-,
         /      /|   |\     \                           /      /|   |\     \ 
        ;      /_|   |_\     ;                         ;      /_|   |_\     ; 
        ;   |\           /|  ;  HAPPY HALLOWEEN! :)    ;   |\           /|  ; 
        ;   | ''--...--'' |  ;                         ;   | ''--...--'' |  ;
         \  ''---.....--''  /                           \  ''---.....--''  / 
          ''*-.,_______,.-*'                             ''*-.,_______,.-*'
'''[1:]

Fireworks = '''
#                               HAPPY NEW YEAR
#                                       . 
#              . .                     -:-             .  .  . 
#            .'.:,'.        .  .  .     ' .           . \ | / . 
#            .'.;.`.       ._. ! ._.       \          .__\:/__. 
#             `,:.'         ._\!/_.                     .';`.      . ' . 
#             ,'             . ! .        ,.,      ..======..       .:. 
#           ,                 .         ._!_.     ||::: : | .        ', 
#    .====.,                  .           ;  .~.===: : : :|   ..===. 
#     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====| 
#  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :| 
# |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::| 
# |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|::F|:====:|::_:|: :|::__:| 
# !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]! 
'''


#Functions zone

def Left_to(day: int, month: int):
    yearXD = datetime.date.today()
    year = yearXD.year
    Hoy = datetime.datetime.today()
    destino = datetime.datetime(year, month, day)
    diferencia = Hoy - destino
    splt1 = str(diferencia).split(',')
    splt2 = str(splt1[1]).split(':')
    splt4 = str(splt1[0]).split(None)
    relpace = splt4[0].replace("-", " ")
    
    return relpace
    
def charge_bar(time:int):
    with alive_bar(time) as bar:
        for fase in range(time):
            if fase < time / 6:
                print("Getting Handlers")
                bar()
                sleep(1)
                System.Clear()
                
            elif fase < time / 3:
                print("So close...")
                bar()
                sleep(1)
                System.Clear()

            elif fase == time:
                sleep(1)
                return System.Clear()


def main2():
    System.Clear()
    print(Colorate.Vertical(Colors.rainbow,Center.XCenter(logo)))
    print("\n"*3)
    print(Colorate.Horizontal(Colors.green_to_cyan, "You want know how many days left to... \n\n"))
    print(Colorate.Horizontal(Colors.green_to_white, "[1]-Christmas"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "[2]-Halloween"))
    print(Colorate.Horizontal(Colors.red_to_white, "[3]-Valentin´s Day"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "[4]-New Year (Solar Calendar)"))
    print(Colorate.Horizontal(Colors.white_to_red, "[5]-New Year (Lunar Calendar)"))
    Select = input(Colorate.Horizontal(Colors.rainbow, "[?]:"))
    if Select == '1':
        christmas()
    elif Select == '2':
        Halloween()
    elif Select == '3':
        Valentines()
    elif Select == '4':
        NY_Solar()
    elif Select == '5':
        NY_Lunar()


def main():
    System.Size(150, 50)
    System.Title("Days left to... - by zPuerta")
    print("\n"*2)
    Anime.Fade(Center.Center(logo), Colors.rainbow,
           Colorate.Vertical, enter=True)
    print("\n"*3)
    System.Clear()
    print(Colorate.Vertical(Colors.rainbow,Center.XCenter(logo)))
    print("\n"*3)
    print(Colorate.Horizontal(Colors.green_to_cyan, "You want know how many days left to... \n\n"))
    print(Colorate.Horizontal(Colors.green_to_white, "[1]-Christmas"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "[2]-Halloween"))
    print(Colorate.Horizontal(Colors.red_to_white, "[3]-Valentin´s Day"))
    print(Colorate.Horizontal(Colors.red_to_yellow, "[4]-New Year (Solar Calendar)"))
    print(Colorate.Horizontal(Colors.white_to_red, "[5]-New Year (Lunar Calendar)"))
    Select = input(Colorate.Horizontal(Colors.rainbow, "[?]:"))
    if Select == '1':
        christmas()
    elif Select == '2':
        Halloween()
    elif Select == '3':
        Valentines()
    elif Select == '4':
        NY_Solar()
    elif Select == '5':
        NY_Lunar()








def christmas():
    System.Clear()
    System.Title("Days left to... [Cristmas] - by zPuerta")
    charge_bar(6)
    System.Clear()
    print(Colorate.DiagonalBackwards(Colors.green_to_red, Center.XCenter(tree)))
    days = Left_to(25, 12) 
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"    Now left{days} days to cristmas :)")))
    Back = input("Get Back [Y/N]")
    if Back == 'y' or Back == 'Y':
        main2()
    else:
        exit()

def Halloween():
    System.Clear()
    System.Title("Days left to... [Halloween] - by zPuerta")
    charge_bar(6)
    System.Clear()
    print(Colorate.DiagonalBackwards(Colors.green_to_red, Center.XCenter(Pumpkin)))
    days = Left_to(31, 10)
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"    Now left{days} days to Halloween :)")))
    Back = input("Get Back [Y/N]")
    if Back == 'y' or Back == 'Y':
        main2()
    else:
        exit()

def Valentines():
    System.Clear()
    System.Title("Days left to... [Valentine Day] - by zPuerta")
    charge_bar(6)
    print(Colorate.DiagonalBackwards(Colors.green_to_red, Center.XCenter(Heart)))
    days = Left_to(14, 2)
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"    Now left{days} days to Valentine´s Day :)")))
    Back = input("Get Back [Y/N]")
    if Back == 'y' or Back == 'Y':
        main2()
    else:
        exit()

def NY_Solar():
    System.Clear()
    System.Title("Days left to... [New Year In Solar calendar] - by zPuerta")
    charge_bar(6)
    System.Clear()
    days = Left_to(31, 12)
    print(Colorate.DiagonalBackwards(Colors.green_to_red, Center.XCenter(Fireworks)))
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"    Now left{days} days to New Year [in Solar Calendar]:)")))
    Back = input("Get Back [Y/N]")
    if Back == 'y' or Back == 'Y':
        main2()
    else:
        exit()

def NY_Lunar():
    System.Clear()
    System.Title("Days left to... [New Year In Lunar calendar] - by zPuerta")
    charge_bar(6)
    System.Clear()
    print(Colorate.DiagonalBackwards(Colors.green_to_red, Center.XCenter(Fireworks)))
    days = Left_to(22, 1)
    print(Colorate.Horizontal(Colors.rainbow, Center.XCenter(f"    Now left{days} days to New Year [in lunar Calendar]:)")))
    Back = input("Get Back [Y/N]")
    if Back == 'y' or Back == 'Y':
        main2()
    else:
        exit()

main()





