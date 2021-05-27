from selenium import webdriver
from datetime import datetime, time
from calendar import day_name
from pandas import DataFrame
from os import system as sy
from utils.WST import WST
from time import sleep
from glob import glob
from getpass import getuser
import os.path
from  struct import calcsize
from time import ctime
from os import path  as pdoc
sy('mode con: cols=80 lines=30')

grade = DataFrame(
    data = {'Monday':['matematica','matematica','história',False,'história','química',"química",False],
            'Tuesday':['biologia','física','matematica',False,'matematica',"filosofia","português",False],
            'Wednesday':['matematica','geografia','biologia',False,"português","português",False,False],
            'Thursday':["espanhol",'química','geografia',False,"inglês","inglês","física",False],
            'Friday':["física",'português','artes',False,'literatura','literatura','sociologia',False],
            'Saturday':[False],
            'Sunday':[False]
        },
    index=['7:10','8:00','8:50',"9:30",'10:00','10:50',"11:40","12:30"]
)      
bonus = False
def clear(): sy("cls")

def download_zarchive(url):
    bits = calcsize("P") * 8
    
    wb = webdriver.Firefox(executable_path=f"utils/geckodriver{bits}")
    controller = WST()

    wb.get(url)

    sleep(2.5)

    controller.remotary(["#hkeytab","#time1","#hkeytab","#time1","#hkeyenter"])
    sleep(5)

    wb.close()

def get_zarchive():
    user = getuser()
    download_folder = glob(f"C:\\Users\\{user}\\Downloads\\*")
    zomm_arqs = []
    times = []
    for i in download_folder: 
        ctime1 = ctime(os.path.getctime(i)).split()[3].replace(":","")
        if "Zoom_cm_fo" in i: zomm_arqs.append([ctime1, i]);times.append(ctime1)
    
    times.sort()
    for i in zomm_arqs:
        if i[0] == times[0]: return i[1]

def join_meeting(url):
    download_zarchive(url)
    sy(get_zarchive())

def get_time_info():
        today = datetime.now()
        today_indx = today.weekday()
        
        a = datetime.now().time()
        subjects = False

        weekday = day_name[today_indx]
        lis_dif = []
        for time in grade.index:
            s = '{}:{}'.format(a.hour,a.minute)
            f = '%H:%M'
            dif = (datetime.strptime(s, f) - datetime.strptime(time, f)).total_seconds()
            dif /= 60
            lis_dif.append(dif)
            if dif >=0 and dif <=50:
                subjects = grade[weekday].loc[time]

        thetime = [time for time in lis_dif if time < 50]    
        return subjects,thetime

def print_prezomba():
    print("""
                                             _                _____    ___  
     _ __   _ __  ___  ____ ___   _ __ ___  | |__    __ _    |___ /   / _ \ 
    | '_ \ | '__|/ _ \|_  // _ \ | '_ ` _ \ | '_ \  / _` |     |_ \  | | | |
    | |_) || |  |  __/ / /| (_) || | | | | || |_) || (_| |    ___) |_| |_| |
    | .__/ |_|   \___|/___|\___/ |_| |_| |_||_.__/  \__,_|   |____/(_)\___/ 
    |_|                                             by: Gυilнєямє D. αlvєz
        """)

def is_time_between(begin_time, end_time, check_time=None):
    # If check time is not given, default to current UTC time
    check_time = check_time or datetime.now().time()
    if begin_time < end_time:
        return check_time >= begin_time and check_time <= end_time
    else: # crosses midnight
        return check_time >= begin_time or check_time <= end_time

def start():
    while True: 
        clear()
        print_prezomba()
        print("""
                             $€Ł€Cт тЋ€ ØρтIØи
    """)

        print("""
             1 - AUTO. PRESENCE           2- җҗҗҗҗҗҗҗҗҗҗ [LOCKED]

             3 - җҗҗҗҗҗҗҗҗҗҗ [LOCKED]     4- җҗҗҗҗҗҗҗҗҗҗ [LOCKED]
             
             5 - җҗҗҗҗҗҗҗҗҗҗ [LOCKED]
    """)

        option = input(">> ")
        if option == "1": menu();break
        else: clear()

def log_now(text):
    log_status = f"  {str(datetime.now().time())[0:8]} - $ {text}"
    print(log_status)
    return log_status

def menu():
    clear()
    print_prezomba()
    print("""
                           ρǺ$т€ zØØм iиviтǺтiØи (ÜяŁ):
    """)
    url = input(">> ")
    if url == "gdatest":
        url = "https://us04web.zoom.us/j/6699798856?pwd=UGlrUWowR3MxQ0VpdnVpWHU0Um5rUT09"
        bonus = True
    if url == "cas":
        url = "https://us05web.zoom.us/j/2857825539?pwd=QUd0cE9iSnBZaC8zdDJ1RENzNWZpUT09"
        bonus = True
    if "web.zoom.us" not in url: 
        print("€яяØя: IиVǺŁIÐ ÜяŁ!\nя€тÜяиiиǥ...");sleep(5);start()
    else: 
        clear()
        print_prezomba()
        if bonus: troc = """
                1- OK, I'LL SLEEP NOW
                2- NO, I'M A SUCKER
""";
        else: troc = """
                1- OK
                2- NO
""";
        print(f"""
            WaRnInG: yOu cAnNoT ChAnGe tHe sCrEeN DuRiNg tHe pRoCeSs!
               JuSt rElAx, LeAvE ThE ReSt wItH Us, UnDeRsTaNdInG?       
                             
                             $€Ł€Cт тЋ€ ØρтIØи
{troc}

""")
    answer = input(">> ")
    if answer != "1": print("€яяØя: $ÜCK€я!\nя€тÜяиiиg...");sleep(5);start()
    
    else:
        clear();print_prezomba()
        print("  ǺŁяIgЋт, ω€'я€ ωØяKIиg тØ ¥ØÜ...\n\n\n   LOG:\n\n")
        with open(f"{pdoc.expanduser('~/Documents')}/prezomba.log","w",encoding="utf8") as f:
            f.write("LOG:\n")

        log = open(f"{pdoc.expanduser('~/Documents')}/prezomba.log","a",encoding="utf8")
        
        if bonus:
            while True:
                _hours = []
                for i in grade.index: _hours.append(i.split(":"))
                for i in range(len(_hours)):
                    _hours[i][0] = int(_hours[i][0])
                    _hours[i][1] = int(_hours[i][1])

                pair_hours = list(zip(_hours,_hours[1:] + _hours[:1]))
             
                if len(get_time_info()[1]) == 0 or len(get_time_info()[1]) == 8:
                    log.write("\n"+log_now(f"waiting school time..."))
                    while not is_time_between(time(_hours[0][0],_hours[0][1]), time(_hours[-1][0],_hours[-1][1])): pass

                while is_time_between(time(_hours[0][0],_hours[0][1]),time(_hours[-1][0],_hours[-1][1])) and len(get_time_info()[1]) != 0:
                    for i in range(len(pair_hours)):
                        if is_time_between( time(pair_hours[i][0][0],pair_hours[i][0][1]), time(pair_hours[i][1][0],pair_hours[i][1][1])): 
                            info = get_time_info()
                            if info[0]:
                                log.write("\n"+log_now(f"joing at meeting: [{info[0]}]..."))
                                while True:
                                    try:
                                        join_meeting(url)
                                    except: 
                                        log.write("\n"+log_now("error connecting, retrying..."))
                                    else: break
                                log.write("\n"+log_now(f"joined"))
                            else:
                                log.write("\n"+log_now(f"there is no class at this time"))

                            log.write("\n"+log_now(f"waiting for next class..."))

                            while is_time_between(time(pair_hours[i][0][0],pair_hours[i][0][1]), time(pair_hours[i][1][0],pair_hours[i][1][1]) ):
                                info = get_time_info()

                            log.write("\n"+log_now("closing Zoom..."))
                            sy('taskkill /im Zoom.exe /F');sleep(2)
                            log.write("\n"+log_now("closed"))

        else:
            join_meeting(url)
if __name__ == '__main__':
    start()
    #