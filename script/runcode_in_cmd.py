import subprocess
import psutil
import time
import json


# 读取配置文件
with open('config/config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 获取全局配置
global_config = config["global"]
root_path = global_config["root_path"]
python_env = global_config["python_env"]


# 定义所有需要执行的命令
commands = [
    f"activate {python_env} && python {root_path}\\script\\a1.py",
    f"activate {python_env} && python {root_path}\\script\\a2.py",
    f"activate {python_env} && python {root_path}\\script\\a3.py",
    f"activate {python_env} && python {root_path}\\script\\a4.py",
    f"activate {python_env} && python {root_path}\\script\\a5.py",
    f"activate {python_env} && python {root_path}\\script\\a6.py",
    f"activate {python_env} && python {root_path}\\script\\a7.py",
    f"activate {python_env} && python {root_path}\\script\\a8.py",
    f"activate {python_env} && python {root_path}\\script\\a9.py",
    f"activate {python_env} && python {root_path}\\script\\a10.py"
]

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
    time.sleep(10)  # 每10秒检查一次

print("所有进程已完成")


