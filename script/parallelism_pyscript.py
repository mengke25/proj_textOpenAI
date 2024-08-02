import json
import os
import shutil

# 读取配置文件
with open('config/config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 获取全局配置
global_config = config["global"]
root_path = global_config["root_path"]
script_parallelism = global_config["script_parallelism"]

# 定义文件路径
template_file = os.path.join(root_path, 'script\\uu', 'template.py')
destination_dir = os.path.join(root_path, 'script', 'uu')

# 确保目标目录存在
os.makedirs(destination_dir, exist_ok=True)

# 复制并重命名文件
for i in range(1, script_parallelism + 1):
    destination_file = os.path.join(destination_dir, f'a{i}.py')
    shutil.copy(template_file, destination_file)

print(f"并行脚本共生成 {script_parallelism} 个")
