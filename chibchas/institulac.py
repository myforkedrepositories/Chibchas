from tools import *
if __name__=='__main__':
    s=time.time()
    user=input('usuario: ')
    password=getpass.getpass('Contraseña: ')
    main(user,password,headless=False,start=1,end=2)
