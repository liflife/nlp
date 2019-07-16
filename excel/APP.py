import tkinter as tk;
import tkinter.filedialog

class APP:  # 声明类
    def __init__(self, master):
        frame = master;  # 创建一个框架(就是容器) 并且指明父容器
        # 创建一个按钮 指明其属于feame框架 设置内容 fg为前景色 command表示点击按钮后调用那个函数
        # 变量path
        path = tk.StringVar()
        # 输入框，标记，按键
        tk.Label(frame, text="目标路径:").grid(row=0, column=0)
        # 输入框绑定变量path
        tk.Entry(frame, textvariable=path).grid(row=0, column=1)
        tk.Button(frame, text="路径选择", command=self.selectPath).grid(row=0, column=2)
        self.Hi = tk.Button(frame, text="我为什么是一个按钮", fg="blue", command=self.say);
        self.Hi.pack();
    # 下面这个就是一个回调函数
    def say(self):
        print("Hello");


    def selectPath(self):

        # 选择文件path_接收文件地址
        path_ = tkinter.filedialog.askopenfilename()
        # 通过replace函数替换绝对文件地址中的/来使文件可被程序读取
        # 注意：\\转义后为\，所以\\\\转义后为\\
        path_ = path_.replace("/", "\\\\")
        # path设置path_的值
        # path.set(path_)


root = tk.Tk();  # 实例化一个主窗口
app = APP(root);  # 实例化 并且把上面初始化的窗口传递进去

root.mainloop();  # 显示窗口