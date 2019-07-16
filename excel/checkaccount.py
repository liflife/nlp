import tkinter.filedialog
from tkinter import *
import tkinter as tk
from readExcel import read_excel
from readExcel import evencut3
import os


def selectLeftPath():
    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()
    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
    # 注意：\\转义后为\，所以\\\\转义后为\\
    path_ = path_.replace("/", "\\\\")
    global leftFilePath, leftData
    leftFilePath.set(path_)
    leftData = read_excel(path_, 1)
    global lb
    for i in leftData:
        leftb.insert(END, i.to_string())


def selectRightPath():
    # 选择文件path_接收文件地址
    path_ = tkinter.filedialog.askopenfilename()
    # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
    # 注意：\\转义后为\，所以\\\\转义后为\\
    path_ = path_.replace("/", "\\\\")
    global rightFilePath, rightData, rightb
    rightFilePath.set(path_)
    rightData = read_excel(path_, 2)
    for i in rightData:
        rightb.insert(END, i.to_string())


listok = []
alistnull = []
listerror = []


def selectEven():
    global listok, listerror, alistnull  #
    listok, listerror, alistnull,countTotal = evencut3(leftData, rightData)
    text='总条数'+str(countTotal)
    listokStr='对账一致:'+str(len(listok))
    listerrorStr='对账不一致:'+str(len(listerror))
    alistnullStr='对账名为null:'+str(len(alistnull))
    tk.Label(main_box, text=text).grid(row=5, column=0)
    tk.Label(main_box, text=listokStr).grid(row=5, column=1)
    tk.Label(main_box, text=listerrorStr).grid(row=5, column=2)
    tk.Label(main_box, text=alistnullStr).grid(row=5, column=4)

    global resultb  # type:tkinter.Listbox
    resultb.delete(0, END)
    # resultb.insert(END, '对账一致')
    # for i in listok:
    #     resultb.insert(END, i)
    resultb.insert(END, '对账不一致')
    for i in listerror:
        resultb.insert(END, i)
    resultb.insert(END, '对账名为null')
    for i in alistnull:
        resultb.insert(END, i)





def save():
    dir='D:\对账'
    if not os.path.exists(dir):
        os.makedirs(dir)
    saveFile('D:\对账\对账一致.txt', listok)
    saveFile('D:\对账\对账不一致.txt', listerror)
    saveFile('D:\对账\对账名为null.txt', alistnull)


def saveFile(filePath, data: list):
    with open(filePath, 'a+') as f:
        for a in data:
            f.write(a + '\n')


leftData = []
rightData = []

main_box = tk.Tk()
main_box.columnconfigure(0, weight=1)
main_box.title('对账工具')  # 设置窗体的标题栏

# 变量path
path = tk.StringVar()

leftFilePath = tk.StringVar()
rightFilePath = tk.StringVar()

# 输入框，标记，按键
tk.Label(main_box, text="银行路径:", width=10, height=3).grid(row=0, column=0)
# 输入框绑定变量path
tk.Entry(main_box, textvariable=leftFilePath, width=50).grid(row=0, column=1)
tk.Button(main_box, text="选择", command=selectLeftPath).grid(row=0, column=2)

# 输入框，标记，按键
tk.Label(main_box, text="目标路径:", width=10, height=3).grid(row=0, column=4)
# 输入框绑定变量path
tk.Entry(main_box, textvariable=rightFilePath, width=50).grid(row=0, column=5)
tk.Button(main_box, text="选择", command=selectRightPath).grid(row=0, column=6)

# 输入框，标记，按键
tk.Button(main_box, text="分析", command=selectEven).grid(row=1, column=6)

# 输入框，标记，按键
tk.Button(main_box, text="保存", command=save).grid(row=2, column=3)

tk.Label(main_box, text="银行").grid(row=3, column=0)
leftsb = tk.Scrollbar(main_box)  # 垂直滚动条组件
leftb = tk.Listbox(main_box, yscrollcommand=leftsb.set, width=100, height=20)  # Listbox组件添加Scrollbar组件的set()方法
leftb.grid(row=4, column=0, columnspan=3)
leftsb.config(command=leftb.yview)  # 设置Scrollbar组件的command选项为该组件的yview()方法

tk.Label(main_box, text="明细").grid(row=3, column=4)
rightsb = tk.Scrollbar(main_box)  # 垂直滚动条组件
rightb = tk.Listbox(main_box, yscrollcommand=rightsb.set, width=100, height=20)  # Listbox组件添加Scrollbar组件的set()方法
rightb.grid(row=4, column=4, columnspan=3)
rightsb.config(command=rightb.yview)  # 设置Scrollbar组件的command选项为该组件的yview()方法



resultsb = tk.Scrollbar(main_box)  # 垂直滚动条组件
resultb = tk.Listbox(main_box, yscrollcommand=resultsb.set, width=200, height=20)  # Listbox组件添加Scrollbar组件的set()方法
resultb.grid(row=9, column=0, columnspan=6)
resultsb.config(command=resultb.yview)  # 设置Scrollbar组件的command选项为该组件的yview()方法

main_box.mainloop()
