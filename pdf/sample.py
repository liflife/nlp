import tkinter as tk
import RenderPage

RenderPage.CreateImageFromPdf("test.pdf", "page.png")

root = tk.Tk()
logo = tk.PhotoImage(file="page.png")

tk.Label(root, image=logo).pack(side="right")

root.mainloop()