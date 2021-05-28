def sagaGit():
    print("Sağa Git")
def solaGit():
    print('Sola git')
def yukariGit():
    print('yukari git')
def asagiGit():
    print('asagi git')
def duzGit():
    print('Hedefe ana avrat gidiliyor.')

def communicateMotor(x,y):
    if x<-20 :
        if y<-20:
            sagaGit()
            asagiGit()
        elif y>20:
           sagaGit()
           yukariGit()

    elif x>20:
        if y<-20:
            solaGit()
            asagiGit()
        elif y>20:
           solaGit()
           yukariGit()
    
    else:
        duzGit()
