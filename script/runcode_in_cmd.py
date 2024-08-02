import subprocess
import psutil
import time

# 定义所有需要执行的命令
commands = [
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a1.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a2.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a3.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a4.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a5.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a6.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a7.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a8.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a9.py",
    "activate env2 && python D:\project\July2024_textOpenAI\script\\a10.py"
]


#---------------------------------------------------------------------------------------------------------------#
## 直接在cmd中分别运行
# for command in commands:
#     subprocess.Popen(['cmd', '/c', 'start', 'cmd', '/k', command])
# print("所有命令已启动")




#---------------------------------------------------------------------------------------------------------------#
## 在编译器中一起运行
processes = []

# 启动所有进程
for command in commands:
    process = subprocess.Popen(command, shell=True)
    processes.append(process)

# 监控进程
while processes:
    for process in processes:
        if process.poll() is not None:  # 检查进程是否结束
            processes.remove(process)
            print(f"Process {process.pid} completed with return code {process.returncode}")
    time.sleep(10)  # 每秒检查一次

print("所有进程已完成")