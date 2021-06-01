
import time


def duzGit(x):
    print(str(x)+" düz gidiliyor")
def sagaGit(x):
    print(str(x)+" sağa gidiliyor")
def solaGit(x):
    print(str(x)+" sola gidiliyor")
def asagiGit(x):
    print(str(x)+" asagi gidiliyor")
def yukariGit(x):
    print(str(x)+" yukari gidiliyor")

def communicateMotor(x,y):
    if x>-50 and x<50 and y<50 and y>-50:
        duzGit(7)
    elif x>50:
        if y>50:
            sagaGit(7)
            yukariGit(7)
        elif y<-50:
            sagaGit(7)
            asagiGit(7)
    elif x<-50:
        if y>50:
            solaGit(7)
            yukariGit(7)
        elif y<-50:
            solaGit(7)
            asagiGit(7)

        
        
