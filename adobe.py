import tkinter as tk

import os
# IMAGEM 250x250

class Tela:

    def __init__(self, master):


        du = tk.Label(janela, text="By: Eduardo CJ")
        du["font"] = ("Arial black", "10")
        du.config(bg="#1C1C1C", foreground="red")
        du.place(x=790, y=610)

        
        cab = tk.PhotoImage(file="cab.png")
        img = tk.Label(janela, image=cab)
        img.cab = cab
        img.config(bg="#1C1C1C")
        img.place(x=0,y=0)

        cabecalho = tk.PhotoImage(file="cabecalho.png")
        imgg = tk.Label(janela, image=cabecalho)
        imgg.cabecalho = cabecalho
        imgg.config(bg="#1C1C1C")
        imgg.place(x=315, y=45)

        antivirus = tk.PhotoImage(file="antivirus.png")
        imgg = tk.Label(janela, image=antivirus)
        imgg.antivirus = antivirus
        imgg.config(bg="#1C1C1C")
        imgg.place(x=430, y=585)

        


####################################################################
        #Labels com as imagens
        
        illustrator = tk.PhotoImage(file="illustrator.png")
        img1 = tk.Label(janela, image=illustrator)
        img1.illustrator = illustrator
        img1.config(bg="black")
        img1.place(x=300,y=150)
        img1.bind("<Button-1>", self.illustrator)
        img1.bind("<Enter>", self.illustrator2)
        img1.bind("<Leave>", self.illustrator3)

        photoshop = tk.PhotoImage(file="photoshop.png")
        img2 = tk.Label(janela, image=photoshop)
        img2.photoshop = photoshop
        img2.config(bg="black")
        img2.place(x=500,y=150)
        img2.bind("<Button-1>", self.photoshop)
        img2.bind("<Enter>", self.photoshop2)
        img2.bind("<Leave>", self.photoshop3)

        premiere = tk.PhotoImage(file="premiere.png")
        img3 = tk.Label(janela, image=premiere)
        img3.premiere = premiere
        img3.config(bg="black")
        img3.place(x=700,y=150)
        img3.bind("<Button-1>", self.premiere)
        img3.bind("<Enter>", self.premiere2)
        img3.bind("<Leave>", self.premiere3)

        animate = tk.PhotoImage(file="animate.png")
        img4 = tk.Label(janela, image=animate)
        img4.animate = animate
        img4.config(bg="black")
        img4.place(x=300,y=350)
        img4.bind("<Button-1>", self.animate)
        img4.bind("<Enter>", self.animate2)
        img4.bind("<Leave>", self.animate3)

        muse = tk.PhotoImage(file="muse.png")
        img5 = tk.Label(janela, image=muse)
        img5.muse = muse
        img5.config(bg="black")
        img5.place(x=500,y=350)
        img5.bind("<Button-1>", self.muse)
        img5.bind("<Enter>", self.muse2)
        img5.bind("<Leave>", self.muse3)

        xd = tk.PhotoImage(file="xd.png")
        img6 = tk.Label(janela, image=xd)
        img6.muse = xd
        img6.config(bg="black")
        img6.place(x=700,y=350)
        img6.bind("<Button-1>", self.xd)
        img6.bind("<Enter>", self.xd2)
        img6.bind("<Leave>", self.xd3)


       
       
        
    #Eventos

    def illustrator(self, event):

        
        os.popen("explorer https://download1493.mediafire.com/gop4pvt196bg/2pt1y37e07mnjyw/illustrator+cc+2020+-+Player+Noob-20211006T015721Z-001.zip")
        

    def illustrator2(self, event):

        self.lb = tk.Label(text="Adobe Illustrator")
        self.lb["font"] = ("Arial","17")
        self.lb.config(bg="#8A4B08", foreground="black")
        self.lb.place(x=293,y=120)


    def illustrator3(self, event):

        self.lb.destroy()


    def photoshop(self, event):

        
        os.popen("explorer https://download1655.mediafire.com/dk6gut10n4ig/stdi3fn7sk7kz79/Adobe+Photoshop+CC+2020-20211006T013819Z-001.zip")
        


    def photoshop2(self, event):

        self.lb1 = tk.Label(text="Adobe Photoshop")
        self.lb1["font"] = ("Arial","17")
        self.lb1.config(bg="#2E9AFE", foreground="black")
        self.lb1.place(x=487,y=120)

    def photoshop3(self, event):

        self.lb1.destroy()

    def premiere(self, event):

        
        os.popen("explorer https://download1498.mediafire.com/2ebxx7ppa7bg/39iqqokqik2yfcn/Adobe+Premiere+Pro+CC+2020.rar")


    def premiere2(self, event):

        self.lb1 = tk.Label(text="Adobe Premiere")
        self.lb1["font"] = ("Arial","17")
        self.lb1.config(bg="#B404AE", foreground="black")
        self.lb1.place(x=690,y=120)

    def premiere3(self, event):

        self.lb1.destroy()

    def animate(self, event):

        
        os.popen("explorer https://download1323.mediafire.com/26dbjukq6fmg/vhyl0svu3rnoscd/Adobe+Animate+2021+-+Flavorzinho-20211006T020846Z-001.zip")

    def animate2(self, event):

        self.lb1 = tk.Label(text="Adobe Animate")
        self.lb1["font"] = ("Arial","17")
        self.lb1.config(bg="#DF3A01", foreground="black")
        self.lb1.place(x=300,y=320)

    def animate3(self, event):

        self.lb1.destroy()

    def muse(self, event):

    
        os.popen("explorer https://download944.mediafire.com/ulcf03voubig/fwclqwap2hqs1em/Adobe+Muse+CC.rar")
        

    def muse2(self, event):

        self.lb1 = tk.Label(text="Adobe Muse")
        self.lb1["font"] = ("Arial","17")
        self.lb1.config(bg="#AEB404", foreground="black")
        self.lb1.place(x=510,y=320)

    def muse3(self, event):

        self.lb1.destroy()

    def xd(self, event):

        
        os.popen("explorer https://download1655.mediafire.com/g2c4ykpqdxgg/uklgqv7f21y558a/Adobe+XD+34.3.12.rar")


    def xd2(self, event):

        self.lb1 = tk.Label(text="Adobe XD")
        self.lb1["font"] = ("Arial","17")
        self.lb1.config(bg="#8A0886", foreground="black")
        self.lb1.place(x=720,y=320)

    def xd3(self, event):

        self.lb1.destroy()


janela = tk.Tk()
Tela(janela)
janela.title("Pacote Adobe")
janela.geometry("930x650+130+20")

janela.resizable(width=False, height=False)
janela.config(cursor="hand2", bg="#1C1C1C")
janela.iconbitmap("adobe.ico")
janela.mainloop()
