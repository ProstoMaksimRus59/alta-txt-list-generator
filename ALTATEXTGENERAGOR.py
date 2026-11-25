#v7.0!!!

import os #Говно код сделанный быстро чтобы не обучать людей пользоватся консолью - умеет только показывать статистику подобие офф листов (например поинтеркрейта).
import re #+ может сама качать датабазу.
import shutil #Этот генератор уже не совместим начиная версии алты v5.1.. ТОК с v7.0
import sys #это формально обрезанная lite для вывода текста..
from tkinter.messagebox import showerror, showinfo
from urllib.error import URLError
import os,sys,re,shutil,urllib.request
def dbsplit(data):
    if data.find(":") != 1:
        return data[(data.find(":")+1):]
    else:
        return data
def urldata():
    return 'https://drive.google.com/uc?export=download&id=1VYq4Dok2iainqwLljWoAzDuzu6hz7zo2' #откуда качать будет датабазу.(тут пример ссылки)
def loaddb(folder):
    try:
        file = open(folder,'r',encoding='utf-8')
    except FileNotFoundError:
        print(("Не найденно"))
        return 0
    data = file.read()
    file.close()
    lvland = data.split("playrs:\n")
    files = os.listdir() #Проверка на наличие уже датабазы
    for scan in files:
        if scan == "Base": #если есть то -
            if 1 == 1:
                shutil.rmtree("Base")
                print(("Датабаза удаленна!"))
    os.mkdir("Base")
    file = open("Base/lvldatabase.altalvl",'w')
    file.write(lvland[0])
    file.close()
    for plar in lvland[1].split(".altapl\n"):
        filename = plar.split("\n")[0] + ".altapl"
        filedata = plar.split("\n")[:-1]
        if filename !=".altapl":
            player = open("Base/" +filename,'w')
            for data in filedata:
                if data == '0':
                    player.write(data)
                else:
                    player.write(data+"\n")
            player.close()
    print(("Датабаза загружена!"))
    return 1
def F1(): #А как аргументы пихать в tk??? я в этом не силен
    print("обновление дб")
    try:
        urllib.request.urlretrieve(urldata(), "Base.altadb")
        try:
            shutil.rmtree('Base')
        except FileNotFoundError:
            print
        if loaddb('Base.altadb') == 0:
            sys.exit()
        print("обновление дб - удачно!")
    except URLError:
        showinfo(title="Загрузка датабазы", message="ошибка")
print("консоль закладки))")
print("Загрузка/обновление датабазы...")

def Victors(lvl):
    try:
        files = os.listdir("Base") #В скобаках какой папке база.
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    all = []
    altapl = list(filter(lambda x: x.endswith('.altapl'), files)) #фильтр форматов(altapl - для игроков юзается)
    print("Лвл:" + str(lvl))
    print("Имеют его>", end=" ")
    
    for file in altapl:
        Scan = 1
        data = open("Base/" + file, 'r')
        while Scan != "0":
            Scan = data.readline().rstrip('\n')
            Scan = Scan.rsplit(":",1)[0]
            if Scan.lower() == lvl.lower():
                print(file.split(".altapl")[0] + ",", end=" ") #Вывод всех у кого есть лвл в пройденных
                all.append(file.split(".altapl")[0])
    print("\n")
    return all
def top(data,pp,target,idlvl): #Делает топ
    superdata = []
    datapp = ([])
    cont = 0
    for d in data:
        pp1 = float(pp[cont])
        if idlvl == '':
            datapp.append((d,pp1))
        else:
            datapp.append((d,pp1,idlvl[cont]))
        cont = cont + 1
    datapp = sorted(datapp, key=lambda datapp: datapp[1], reverse=True)
    cont = 1
    if idlvl != "":
        superdata.append("####Main list####\n\n")
    deco = [':first_place:',':second_place:',':third_place:',':medal:']
    decolen = len(deco) - 1
    print(decolen)
    for printtop in datapp:
        print(printtop)
        namenotid = printtop[0].split(":")
        namenotid = namenotid[-1]
        if printtop[1] != 0:
                print(printtop[0])
                if idlvl != "":
                    notvervict = " , ".join(Victors(printtop[0]))
                if target.lower() == printtop[0].lower():
                    superdata.append("топ-" + str(cont),end="\n")
                    return 1
                if cont == 11 and idlvl != "":
                    superdata.append("\n####Extended List####\n\n")
                elif cont == 16 and idlvl != "":
                    superdata.append("\n####Beyond list####\n\n")
                elif cont != 1:
                    superdata.append(".....................\n")
                if target == "0":
                    superdata.append("top-"+str(cont))
                    if cont <= decolen:
                        superdata.append('' + str(deco[cont-1]) + "**'" + str(namenotid) + "'**" + str(deco[cont-1]))
                    elif cont <= 10:
                        superdata.append(' ' + str(deco[decolen]) + "**'" + str(namenotid) + "'**" + str(deco[decolen]))
                    else:
                        superdata.append(" **'" + str(namenotid) + "'**")
                    if idlvl != "":
                        superdata.append("\nChallenge by **" + str(scanerpla(printtop[0],1)) + "**")
                        superdata.append("\nVerified by **" + str(scanerpla(printtop[0],2)) + "**")
                    else:
                        superdata.append("\nCompleted>**"+infoplavict(printtop[0])+"**")
                    superdata.append("\n pp:**" + str(printtop[1]) + '**\n')
                if idlvl != "":
                    superdata.append("All Victors (unsorted, and *all* of them—even the Verifiers are here):" '\n>***' + notvervict + "***\n")
                    superdata.append("id:**" + str(printtop[2]) + '**\n')
        cont = cont + 1
    return superdata

def scanallvl(): #Ищет все лвла
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    lvls.append("")
    data.close()
    scan = "0"
    cout = 0
    alllvl = []
    alllvl.append(lvls[0].rstrip("\n"))
    while scan != "":
        if (cout % 9) == 0:
            alllvl.append(scan.rstrip("\n"))
        cout = cout + 1
        scan = lvls[cout]
    return alllvl

def scanerpla(lvl,type):
    
    data = open("Base/lvldatabase.altalvl", 'r')
    lvls = data.readlines()
    data.close()
    cout = 0

    while lvls != "":
        try:
            if lvls[cout].split("\n")[0] == lvl:
                dl = dbsplit(lvls[cout + int(type)])
                return dl.rstrip('\n')
        except IndexError:
            return 0
        cout = cout + 1

def infolvl(lvl,setmode,custom):
    good = 0
    try:
        data = open("Base/lvldatabase.altalvl", 'r')
    except FileNotFoundError:
        print("Датабаза не найдена")
        return 0
    scan = 0
    while scan == 0:
        lvlscan = data.readline().rstrip('\n')
        if lvlscan.lower() == lvl.lower():
            info = 6 + custom
            while info != 0:
                info = info - 1
                lvlinfo = data.readline().rstrip('\n').lower()
                if setmode == "1":
                    print(lvlinfo)
                if info == 0:
                    return lvlinfo.split(":")[-1]
                scan = 1
                good = 1
        if lvlscan == "":
            scan = 1
    
    if good == 0:
        if setmode == "1":
            print("лвл не Найден в базе")
        return 0
    data.close()

def nikttop(name):
                Ramdonmane = os.listdir("Base/") #ищет в базе игроков
                Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
                pplvl = []
                alllvl = []
                for plaer in Ramdonmane:
                    wfr = plaer.split(".altapl")
                    alllvl.append(wfr[0])
                    pplvl.append(round(tophelper(plaer)[0]))
                print(pplvl)
                print(alllvl) 
                datapp = ([])
                cont = 0
                for d in alllvl:
                    pp1 = float(pplvl[cont])
                    datapp.append((d,pp1))
                    cont = cont + 1
                datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
                print(datapp)
                cout = 0
                for toper in datapp:
                    print(toper[0])
                    cout = cout + 1
                    if toper[0].lower() == name:
                        return cout
def toperlvl(name):
                alllvl = scanallvl() #Получает все лвла
                safelllvl = scanallvl()
                pplvl = []
                for lvl in safelllvl:
                    if scanerpla(lvl, '2') != "?":
                        pplvl.append(infolvl(lvl,"0",0)) #Получает пп
                    else:
                        alllvl.remove(lvl)
                datapp = ([])
                cont = 0
                for d in alllvl:
                    pp1 = float(pplvl[cont])
                    datapp.append((d,pp1))
                    cont = cont + 1
                datapp = sorted(datapp, key=lambda datapp: datapp[-1], reverse=True)
                print(datapp)
                cout = 0
                for toper in datapp:
                    print(toper[0])
                    cout = cout + 1
                    if toper[0].lower() == name:
                        return cout
def tophelper(plaer):
        
        hardest = 1 #по название доложно понятно быть)
        folder = "base/" + plaer.replace('"', '')
        file = open(folder, 'r')
        pp = 0
        Scan = 1
        plarr = []
        pparr = []
        plarr.append(file.readline().rstrip('\n')) #Показывает какой игрок
    
        while Scan == 1:
            pp1 = re.findall(r'\d+', file.readline().rstrip(' ').rstrip('\n').rstrip(':'))
            print(pp1)
            print("\\//")
            lvl = int(pp1[-1]) #для удобства (чтоб не по сто раз писать [0]) + все таки я написал -1 и теперь можно и арабские цифрами позоваться
    
            if lvl != 0:
                pp = pp + lvl * 0.85**(hardest-1) #Формула расчета пп
                hardest = hardest + 1
    
            if lvl == 0:
                Scan = 0
                pparr.append(pp)
        return pparr


def toppla():
    Ramdonmane = os.listdir("Base/") #ищет в базе игроков
    Ramdonmane = filter(lambda x: x.endswith('.altapl'), Ramdonmane)
    pplvl = []
    alllvl = []
    for plaer in Ramdonmane:
        wfr = plaer.split(".altapl")
        alllvl.append(wfr[0])
        pplvl.append(round(tophelper(plaer)[0])) #Получает пп
    dad = top(alllvl,pplvl,"0",'')
    print(dad)
    test = open("toppla.txt",'w')
    test.write(str(''.join(dad)))
    test.close()
def toplvl():
    alllvl = scanallvl() #Получает все лвла
    pplvl = []
    idlvl = []
    for lvl in alllvl:
        pplvl.append(infolvl(lvl,"0",0)) #Получает пп
        idlvl.append(infolvl(lvl,"0",1))
    dad = top(alllvl,pplvl,"0",idlvl)
    print(dad)

def topver():
    alllvl = scanallvl() #Получает все лвла
    safelllvl = scanallvl()
    pplvl = []
    idlvl = []
    for lvl in safelllvl:
        if scanerpla(lvl, '2') != "?":
            pplvl.append(infolvl(lvl,"0",0))#Получает пп
            idlvl.append(infolvl(lvl,"0",1))#id
        else:
            alllvl.remove(lvl)
    dad = top(alllvl,pplvl,"0",idlvl)
    print(dad)
    test = open("toplvl.txt",'w')
    test.write(str(''.join(dad)))
    test.close()
def infoplavict(plaer):
    print(plaer)    
    filespla = open("Base/"+plaer + ".altapl",'r')
    filespla.readline()
    fff = filespla.read().split("\n")
    filespla.close()
    l = ''
    fist = 0
    for lvl in fff:
        if lvl != "0" and fist == 1:
            if lvl != "":
                l = l + " , "
        print(lvl,len(lvl.split(":")))        
        if lvl != "0" and len(lvl.split(":")) == 2:
            l = l + lvl.split(":")[0]
        elif lvl != "0" and len(lvl.split(":")) == 3:
            l = l + lvl.split(":")[1]
        fist = 1
    return l
