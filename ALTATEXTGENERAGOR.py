import os #Говно код сделанный быстро чтобы не обучать людей пользоватся консолью - умеет только показывать статистику подобие офф листов (например поинтеркрейта).
import re #+ может сама качать датабазу.
import shutil #Этот недо gui уже не совместим начиная версии алты v3.4.. ТОК с v5.1
import sys #это формально обрезанная lite для вывода текста..
from tkinter.messagebox import showerror, showinfo
from urllib.error import URLError
import zipfile,os,sys,re,shutil,urllib.request

#Для нормального запуска надо создать ico(128x128) и png(680x720) и назвать так AL.ico(иконка на проге) и AL_BG.png(Фон)
# Еще они доложны быть в папке "Resources"
#
#
def urldata():
    return 'https://drive.google.com/uc?export=download&id=1z7XMeIXgCcbODcSNhrlzTJVypxPXaNTF' #откуда качать будет датабазу.(тут пример ссылки)
def F1(): #А как аргументы пихать в tk??? я в этом не силен
    print("обновление дб")
    try:
        urllib.request.urlretrieve(urldata(), "Base.zip")
        try:
            shutil.rmtree('Base')
        except FileNotFoundError:
            print
        try:
            zip = zipfile.ZipFile('Base.zip', 'r')
        except FileNotFoundError:
            sys.exit()
        zip.extractall('')
        print("обновление дб - удачно!")
    except URLError:
        showinfo(title="Загрузка датабазы", message="ошибка")
print("консоль закладки))")
no = 0
print("Загрузка/обновление датабазы...")
try:
    autocheck = open("plar.ALTAL", 'r')
    autoplar = autocheck.read()
    autocheck.close()
except FileNotFoundError:
     no = 1
#Настройка
 
try:
    shutil.rmtree("Base")
except FileNotFoundError:
    print
try:
    zip = zipfile.ZipFile('Base.zip', 'r')
except FileNotFoundError:
    sys.exit()
zip.extractall('')

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
            Scan = Scan.split(":")[0]
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
    for printtop in datapp:
        print(printtop)
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
                    superdata.append("\n####legacy list####\n\n")
                elif cont != 1:
                    superdata.append(".....................\n")
                if target == "0":
                    superdata.append("Топ-" + str(cont))
                    superdata.append(" **'" + str(printtop[0]) + "'**" )
                    if idlvl != "":
                        superdata.append("\nАвтор(ы)- **" + str(scanerpla(printtop[0],1)) + "**")
                        superdata.append("\nВерифер> **" + str(scanerpla(printtop[0],2)) + "**")
                    else:
                        superdata.append("\nПрошел>**"+infoplavict(printtop[0])+"**")
                    superdata.append("\n pp:**" + str(printtop[1]) + '**\n')
                if idlvl != "":
                    superdata.append("Те кто прошли(без сортировки и ВСЕ даже вериферы тут):" '\n>***' + notvervict + "***\n")
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
                dl = lvls[cout + int(type)].split(":")[-1]
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
    filespla = open("base/"+plaer + ".altapl",'r')
    filespla.readline()
    fff = filespla.read().split("\n")
    filespla.close()
    l = ''
    fist = 0
    for lvl in fff:
        if lvl != "0" and fist == 1:
            l = l + " , "
        if lvl != "0":
            l = l + lvl.split(":")[0]
        fist = 1
        print(fff)
    return l