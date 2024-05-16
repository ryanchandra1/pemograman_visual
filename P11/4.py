print('===================================================')
print('===Mengambil Data dan Menampilkan Data (Part2)===')
print('===================================================')
from tkinter import *
import tkinter.messagebox

class DataInOut:
    
    def __init__(self, root):
        self.root = root
        self.root.title('Penjumlahan')
        self.root.geometry('300x150+0+0')
        
        frame1 = Frame(self.root)
        frame1.grid()
        
        frame2 = Frame(frame1)
        frame2.grid(row=0, column=0)
        
        frame3 = Frame(frame1)
        frame3.grid(row=2, column=0)
        
        frame4 = Frame(frame1)
        frame4.grid(row=2, column=1)
        
        FirstNum    = StringVar()
        SecondNum   = StringVar()
        Hasil       = StringVar()
        
        self.lblFirstnum = Label(frame2, text='Enter First Number')
        self.lblFirstnum.grid(row=0, column=0)
        self.lblFirstnum = Entry(frame2, textvariable=FirstNum)
        self.lblFirstnum.grid(row=0, column=1)
        
        self.lblSecondnum = Label(frame2, text='Enter Second Number')
        self.lblSecondnum.grid(row=1, column=0)
        self.lblSecondnum = Entry(frame2, textvariable=SecondNum)
        self.lblSecondnum.grid(row=1, column=1)
        
        self.lblHasil = Label(frame2, text='Hasil')
        self.lblHasil.grid(row=2, column=0)
        self.lblHasil = Entry(frame2, textvariable=Hasil)
        self.lblHasil.grid(row=2, column=1)
        
        def JUMLAHKAN():
            pertama = float(FirstNum.get())
            kedua = float(SecondNum.get())
            hasil = pertama + kedua
            Hasil.set(hasil)
            
        def reset():
            FirstNum.set('')
            SecondNum.set('')
            Hasil.set('')
            
        def keluar():
            root.destroy()
            
        self.btnJumlahkan = Button(frame3, text='Jumlahkan', command=JUMLAHKAN).grid(row=2, column=0)
        self.btnReset = Button(frame3, text='Reset', command=reset).grid(row=2, column=1)
        self.btnKeluar = Button(frame3, text='Keluar', command=keluar).grid(row=2, column=2)
        
if __name__ == '__main__':
    root = Tk()
    application = DataInOut(root)
    root.mainloop()
            