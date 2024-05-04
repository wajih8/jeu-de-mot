from PyQt5.uic import loadUi
from random import randint
from pickle import load,dump
from PyQt5.QtWidgets import QApplication,QMessageBox,QTableWidgetItem
m=1
def generate(x):
    ch=""
    for i in range(x):
        ch=ch+chr(randint(65,90))
    return ch
def chlot(x):
    ch=""
    for i in range(x):
            ch=ch+"-"
    return ch
def geta(x):
    k=randint(1,x)
    f=open("mot.txt","r")
    for i in range(k):
        ch=f.readline(-1)
    f.close()
    return ch[:-1]
def check():
    try:
        f=open("data.dat","rb")
        e=load(f)
        f.close()
        f=open("mot.txt","r")
        i=0
        tes=True
        while i<e["nbr"]and tes:
            i+=1
            ch=f.readline()
            tes=len(ch)==e["taille"]+1 
        f.close()
        return tes
    except:
        return False
def remp():
    global c,a,b,mot,pp
    pp=""
    mot=""
    a,b=ff.lem.text(),ff.letm.text()
    c=ff.lena.text()
    ff.res2.clear()
    if a.isdigit()==False or int(a)<1 or int(a)>100:
        QMessageBox.critical(ff,"error","nombre de mot invalid")
    elif b.isdigit()==False or int(b)<1 or int(b)>10 :
        QMessageBox.critical(ff,"error","taille de mot invalid")
    elif c.isdigit()==False or int(c)<1 or int(c)>20:
        QMessageBox.critical(ff,"error","nombre de attamt invalid")
    else:
        f=open("mot.txt","w")
        a=int(a)
        b=int(b)
        c=int(c)
        for i in range(a):
            f.write(generate(b)+"\n")
        f.close()
        ff.gb2.setEnabled(True)
        ff.gb1.setEnabled(False)
        mot=geta(a)
        pp=chlot(b)
        e=dict()
        e["nbr"],e["taille"],e["c"]=a,b,c
        ff.gb3.hide()
        with open("data.dat","wb") as f:
            dump(e,f)
            ff.fm.show()
def play():
    global m,pp 
    m+=1
    ff.lb5.setText('donner la lettre '+str(m)+' :')
    if mot=="":
        QMessageBox.critical(ff,"error","ther is un problem")
        return 0
    else:
        p=ff.lea.text().upper()
        if(p=="" or not("A"<=p<="Z")):
            QMessageBox.critical(ff,"error","le champ et vide ou incorrect")
            m-=1
            ff.lb5.setText('donner la lettre '+str(m)+' :')
            return 0
       
        if mot.find(p)!=-1:
            for i in range(b):
                if mot[i]==p:
                    pp=pp[:i]+p+pp[i+1:]
        ff.tw.setRowCount(m-1)
        ff.tw.setItem(m-2,0,QTableWidgetItem(str(m-1)))
        ff.tw.setItem(m-2,1,QTableWidgetItem(p))
        ff.tw.setItem(m-2,2,QTableWidgetItem(pp))
        if m>c:
            ff.gb2.setEnabled(False)
            ff.res.setText("Avec tout mon respect, tu n'as pas gagné appré "+str(m-1)+" fois")
            ff.res2.setText("le mot est : "+str(mot))
            
            
        if(mot==pp): 
            ff.gb2.setEnabled(False)
            ff.res.setText("vous étez gagnaié appré "+str(m-1)+" fois")
def joue():
    global m,pp,mot,b,c
    if not(check()):
        QMessageBox.critical(ff,"errour de fiché","verifié le fechié de configuration \nde jeu ou remlire niveau")
        return 0
    ff.bp.setEnabled(True)
    ff.res2.clear()
    with open("data.dat","rb")as f:
        try:
            e=load(f)
            ff.gb3.hide() 
            ff.gb1.setEnabled(False)
            ff.gb2.setEnabled(True)
            mot=geta(e["nbr"])
            pp=chlot(e["taille"])
            b=e["taille"]
            c=e["c"]
            m=1
            ff.lb5.setText('donner la lettre '+str(m)+' :')
            ff.tw.setRowCount(0)
            ff.fm.show()
        except:
            QMessageBox.critical(ff,"error","ther is an error")
def reremp():
    global m
    ff.res2.clear()
    m=1
    ff.gb1.setEnabled(True)
    ff.tw.setRowCount(0)
    ff.res.clear()
    ff.gb2.setEnabled(False)
def retake():
    global m,pp,mot,b,c
    ff.res.clear()
    if not(check()):
        QMessageBox.critical(ff,"errour de fiché","verifié le fechié de configuration \nde jeu ou remlire niveau")
        return 0
    with open("data.dat","rb")as f:
        try:
            e=load(f)
            ff.gb1.setEnabled(False)
            ff.gb2.setEnabled(True)
            mot=geta(e["nbr"])
            pp=chlot(e["taille"])
            b=e["taille"]
            c=e["c"]
            m=1
            ff.lb5.setText('donner la lettre '+str(m)+' :')
            ff.tw.setRowCount(0)
            
        except:
            QMessageBox.critical(ff,"error","erreur index ficher ")
app=QApplication([])
ff=loadUi("jeudemot.ui")
ff.show()
ff.fm.hide()
ff.gb2.setEnabled(False)
ff.bgo1.clicked.connect(remp)
ff.bgo2.clicked.connect(play)
ff.brj.clicked.connect(reremp)
ff.bp.clicked.connect(retake)
ff.bjs.clicked.connect(joue)
app.exec_()
