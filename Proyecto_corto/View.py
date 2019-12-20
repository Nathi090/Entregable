import tkinter as tk
from tkinter import *
from tkinter import ttk
from winsound import *
import winsound
from threading import *
import time
import random
import sys








class View:

    def __init__(self, raiz):

        self.raiz=raiz
        self.actual=0
        self.aux=int(self.leeScore("ganador.txt"))
        self.user0=self.leeUser("ganador.txt")
        self.puntaje=0
        self.lista= []
        self.var= tk.IntVar()
        self.b_aux = Button(self.raiz, command=lambda: self.var.set(1))
        self.b_aux.place()
    def juego(self):

        def play1():
            p=lambda: PlaySound('sounds/l.wav', winsound.SND_ASYNC)
            p()
            self.actual=0
            self.b_aux.invoke()

        def play2():
            p=lambda: PlaySound('sounds/r.wav', winsound.SND_ASYNC)
            p()
            self.actual=1
            self.b_aux.invoke()

        def play3():
            p = lambda: PlaySound('sounds/a.wav', winsound.SND_ASYNC)
            p()
            self.actual=2
            self.b_aux.invoke()

        def play4():
            p=lambda: PlaySound('sounds/x.wav', winsound.SND_ASYNC)
            p()
            self.actual=3
            self.b_aux.invoke()

        def play5():
            p=lambda: PlaySound('sounds/y.wav', winsound.SND_ASYNC)
            p()
            self.actual=4
            self.b_aux.invoke()

        def principal():
            p = lambda: PlaySound('sounds/principal.wav', winsound.SND_ASYNC)
            p()

        def start():
            p = lambda: PlaySound('sounds/start.wav', winsound.SND_ASYNC)
            p()

        def winner():
            gg = lambda: PlaySound('sounds/winner.wav', winsound.SND_ASYNC)
            gg()

        def gameover():
            gg = lambda: PlaySound('sounds/gameover.wav', winsound.SND_ASYNC)
            gg()

        def play():
            self.var = tk.IntVar()
            b.destroy()
            player_thread = Thread(target=start)
            player_thread.start()
            stop=False

            menubar = Menu(self.raiz)
            self.raiz.config(menu=menubar)
            inst = Menu(menubar)
            menubar.add_cascade(label="Instrucciones", menu=inst)
            inst.add_command(label="El juego consiste en seguir la secuencia "
                                   "de notas que se van tocando en la ocarina "
                                   "y superar el record " + str(self.aux) + " de " + self.user0 + "."
                                    "En cada turno se va agregando una nota")
            def usuario():

                root= Tk()
                root.geometry('50x110')
                texto = Text(root, height=5, width=20)
                texto.pack()

                def cerrar():
                    self.user0=texto.get("1.0",END)
                    print (self.user0)
                    root.destroy()
                broot=Button(root, height=2, width=10, text="Aceptar", bg="green", command=cerrar)
                broot.pack()
                root.mainloop()

            user = Menu(menubar)
            menubar.add_cascade(label="Usuario", menu=user)
            user.add_command(label="ingresar", command=usuario)
            self.raiz.update()
            b.destroy()

            self.raiz.geometry('503x427')
            self.raiz.configure(bg = 'black')
            self.raiz.title('Simón')


            b1=Button(self.raiz,height=2, width=5, bg="lightgreen", command=play1, border=10, text="L",font=("Helvetica", 8,"bold"))
            b1.place(relx=0.3, rely=0.25)


            b2=Button(self.raiz,height=2, width=5, bg="pink", command=play2, border=10 , text="R",font=("Helvetica", 8,"bold"))
            b2.place(relx=0.6, rely=0.25)

            b3=Button(self.raiz,height=2, width=5, bg="cyan", command=play3, border=10 , text="A",font=("Helvetica", 8,"bold"))
            b3.place(relx=0.6, rely=0.5)

            b4=Button(self.raiz,height=2, width=5, bg="beige", command=play4, border=10, text="X",font=("Helvetica", 8,"bold") )
            b4.place(relx=0.45, rely=0.37)

            b5=Button(self.raiz,height=2, width=5, bg="lightblue", command=play5, border=10 , text="Y",font=("Helvetica", 8,"bold"))
            b5.place(relx=0.3, rely=0.5)

            def jugar():
                thread(self.lista, b1, b2, b3, b4, b5, bb)
                bb.destroy()





            bb=Button(self.raiz, height=2, width=10,bg="yellow", text="Play", command=jugar,border=10)
            bb.place(relx=0.4, rely=0.8)


        def t0(lista,b1,b2,b3,b4,b5):
            for x in lista:
                if x == 0:
                    playable(b1)
                if x == 1:
                    playable(b2)
                if x == 2:
                    playable(b3)
                if x == 3:
                    playable(b4)
                if x == 4:
                    playable(b5)
                time.sleep(0.5)

        def t1(lista):

            for x in range(len(lista)):
                self.b_aux.wait_variable(self.var)
                if self.actual!=lista[x]:

                    if self.puntaje>self.aux:
                        print(self.user0)
                        self.escribeArchivo("ganador.txt",self.puntaje, self.user0)

                        ganador= tk.PhotoImage(file="sounds/ganador.png")
                        self.raiz.geometry('1200x675')
                        bg = Button(self.raiz, height=ganador.height(), width=ganador.width(),
                                   command=self.salir, image=ganador, border=10)
                        bg.pack()
                        player_thread = Thread(target=winner)
                        player_thread.start()


                    else:
                        perdedor = tk.PhotoImage(file="sounds/perdedor.png")
                        self.raiz.geometry('750x544')
                        bp = Button(self.raiz, height=perdedor.height(), width=perdedor.width(),
                                    command=self.salir, image=perdedor, border=10)
                        bp.pack()
                        player_thread = Thread(target=gameover)
                        player_thread.start()






        def thread(lista,b1,b2,b3,b4,b5, bb):
            while True:
                lista.append(random.randint(0, 4))
                t0(lista,b1,b2,b3,b4,b5)
                t1(lista)
                self.puntaje+=1
                time.sleep(1)




        def playable(b):
            b.flash()
            b.invoke()

        player_thread = Thread(target=principal)
        player_thread.start()
        image = tk.PhotoImage(file="sounds/ocarina.png")
        label = tk.Label(image=image)
        label.place( x=0, y=0, relwidth=1, relheight=1)
        self.raiz.geometry('503x427')
        boton=tk.PhotoImage(file="sounds/boton.png")


        b = Button(self.raiz, height=boton.height(), width=boton.width(),
                   command=play, image=boton,border=10, bg="black")
        b.pack()
        self.raiz.configure(bg = 'beige')
        self.raiz.title('Simón')

        self.raiz.mainloop()

    def leeScore(self, txt):
        archivo = open(txt, "r")
        res=archivo.readline()
        archivo.close()
        return res
    def leeUser(self, txt):
        res=""
        archivo = open(txt, "r")
        f=archivo.readlines()
        for x in f:
            res=x
        archivo.close()
        return res

    def escribeArchivo(self, txt, puntaje, user):
        archivo = open(txt, "w")
        archivo.write(str(puntaje)+"\n")
        archivo.write(user)
        archivo.close()

    def salir(self):
        self.raiz.destroy()










if __name__=='__main__':
    raiz = Tk()
    coso=View(raiz)
    coso.juego()





