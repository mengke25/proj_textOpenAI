import os
import shutil
import subprocess
import json

#-----------------------------------------------------------------------------------------------#
# 读取配置文件
with open('config\config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 获取全局配置
global_config = config["global"]
root_path = global_config["root_path"]
chat_file = global_config["chatfile"]
script_parallelism = global_config["script_parallelism"]

#-----------------------------------------------------------------------------------------------#
def copy_and_rename(source_file, target_folder):
    """
    将来源文件复制到目标文件夹，并重命名为a（保留原文件后缀）。
    如果目标文件夹已经存在名为a的文件，则覆盖它。
    
    :param source_file: 来源文件的路径
    :param target_folder: 目标文件夹的路径
    """
    if not os.path.isfile(source_file):
        raise FileNotFoundError(f"来源文件 {source_file} 不存在")
    
    if not os.path.isdir(target_folder):
        raise NotADirectoryError(f"目标文件夹 {target_folder} 不存在")
    
    # 获取文件扩展名
    _, file_extension = os.path.splitext(source_file)
    
    # 定义目标文件路径
    target_file = os.path.join(target_folder, f'a{file_extension}')
    
    # 复制并重命名文件
    shutil.copy2(source_file, target_file)
    print(f"文件“ {source_file} ”已经被复制到“ {target_file}”")

source_file = os.path.join(root_path, chat_file)
target_folder = os.path.join(root_path, 'file')

#-----------------------------------------------------------------------------------------------#
copy_and_rename(source_file, target_folder)

#-----------------------------------------------------------------------------------------------#
script_to_run = os.path.join(root_path, 'script', 'split_xlsx.py')
subprocess.run(['python', script_to_run], check=True)

#-----------------------------------------------------------------------------------------------#
script_to_run = os.path.join(root_path, 'script', 'parallelism_pyscript.py')
subprocess.run(['python', script_to_run], check=True)

#-----------------------------------------------------------------------------------------------#
script_to_run = os.path.join(root_path, 'script', 'runcode_in_cmd.py')
subprocess.run(['python', script_to_run], check=True)

#-----------------------------------------------------------------------------------------------#
script_to_run = os.path.join(root_path, 'script', 'append_xlsx.py')
subprocess.run(['python', script_to_run], check=True)

#-----------------------------------------------------------------------------------------------#
# 将处理后的文件复制回 orig_file 文件夹并重命名
processed_file = os.path.join(root_path, 'output', 'a.xlsx')
if not os.path.isfile(processed_file):
    raise FileNotFoundError(f"处理后的文件 {processed_file} 不存在")

orig_folder = os.path.join(root_path, 'output')
orig_filename, orig_extension = os.path.splitext(os.path.basename(chat_file))
target_filename = f"{orig_filename}_AIextract{orig_extension}"
target_file = os.path.join(orig_folder, target_filename)

shutil.copy2(processed_file, target_file)
print(f"处理后的文件 {processed_file} 已经被复制到 {target_file}")

#-----------------------------------------------------------------------------------------------#
# 删除临时脚本文件
deletescript_directory = os.path.join(root_path, 'script', 'uu')
files_in_directory = os.listdir(deletescript_directory)
file_directory = os.path.join(root_path, 'file')
output_directory = os.path.join(root_path, 'output')

for file in files_in_directory:
    file_path = os.path.join(deletescript_directory, file)
    # 检查文件是否是.py文件且不是template.py
    if file.endswith(".py") and file != "template.py":
        try:
            os.remove(file_path)
            print(f"删除临时脚本: {file_path}")
        except Exception as e:
            print(f"删除临时脚本 {file_path} 失败: {e}")

print("临时脚本删除完成")

# 删除 file_directory 路径下的所有文件，除了 a.xlsx
files_in_file_directory = os.listdir(file_directory)
for file in files_in_file_directory:
    file_path = os.path.join(file_directory, file)
    if file != "a.xlsx":
        try:
            os.remove(file_path)
            print(f"Deleted: {file_path}")
        except Exception as e:
            print(f"Failed to delete {file_path}: {e}")

print("临时文件删除完成")

