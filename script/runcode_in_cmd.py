import subprocess
import psutil
import time
import json
import os

# 读取配置文件
with open('config/config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 获取全局配置
global_config = config["global"]
root_path = global_config["root_path"]
python_env = global_config["python_env"]
script_parallelism = global_config["script_parallelism"]

# 定义所有需要执行的命令
commands = [
    f"activate {python_env} && python {os.path.join(root_path, 'script', 'uu', f'a{i}.py')}"
    for i in range(1, script_parallelism + 1)
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


