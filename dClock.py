import tkinter as tk
from time import strftime

# 创建主窗口
root = tk.Tk()
root.title("桌面时钟")
root.configure(bg='SystemButtonFace')  # 设置系统默认背景色
root.overrideredirect(True)  # 隐藏标题栏
root.attributes('-topmost', True)  # 始终置顶
root.attributes('-alpha', 0.8)  # 设置窗口透明度
root.attributes('-transparentcolor', 'SystemButtonFace')  # 设置透明色

# 获取屏幕尺寸
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 创建标签控件
time_label = tk.Label(root, 
                     font=('Consolas', 40, 'bold'),
                     foreground='#0099FF',
                     background='SystemButtonFace',
                     relief='flat',
                     bd=0)
time_label.pack(anchor='center')

# 首次更新时间显示
current_time = strftime('%H:%M:%S')
current_date = strftime('%m-%d %a')
time_label.config(text=f"{current_date}\n{current_time}")

# 设置初始窗口位置（右上角）
root.update()  # 更新窗口信息以获取实际大小
window_width = root.winfo_width()
window_height = root.winfo_height()
x = screen_width - window_width - 20  # 距离右边缘20像素
y = 20  # 距离顶部20像素
root.geometry(f"+{x}+{y}")  # 设置窗口位置

# 拖拽功能变量
drag_data = {"x": 0, "y": 0}

def start_drag(event):
    drag_data["x"] = event.x
    drag_data["y"] = event.y

def do_drag(event):
    deltax = event.x - drag_data["x"]
    deltay = event.y - drag_data["y"]
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry(f"+{x}+{y}")

# 绑定鼠标事件
time_label.bind("<Button-1>", start_drag)
time_label.bind("<B1-Motion>", do_drag)

# 时间更新函数
def update_time():
    current_time = strftime('%H:%M:%S')  # 时间格式
    current_date = strftime('%m-%d %a')  # 日期格式
    time_label.config(text=f"{current_date}\n{current_time}")
    time_label.after(1000, update_time)  # 每秒更新

# 首次调用
update_time()

# 运行主循环
root.mainloop()