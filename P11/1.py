import tkinter as tk
root = tk.Tk()

#latihan 1 membuat widget dasar

# WidgetDasarku = tk.Tk()
# WidgetDasarku.mainloop()

#Latihan 2 membuat canvas

# Kanvasku = tk.Canvas(root, height = 1000, width = 1920)
# Kanvasku.pack()

Frameku = tk.Frame(root, bg = 'pink')
Frameku.place(relwidth= 0.5, relheight= 0.75)

#Latihan 4a : membuat button di root

# Tombolku = tk.Button(root, text = "Tes Tombol", bg = 'gray', fg = 'red')
# Tombolku.pack

#Latihan 4b : Membuat Button di frame

Tombolku = tk.Button(Frameku, text = "Test Tombol", bg = 'gray', fg = 'red')
Tombolku.pack()

Entryku = tk.Entry(Frameku, bg = 'green')
Entryku.pack()



root.mainloop()