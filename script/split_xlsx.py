import pandas as pd
import numpy as np
import os
import json

#-----------------------------------------------------------------------------------------------#
# 读取配置文件
with open('config\config.json', 'r', encoding='utf-8') as config_file:
    config = json.load(config_file)

# 获取全局配置
global_config = config["global"]
root_path = global_config["root_path"]
input_dir = os.path.join(root_path, 'file')
input_file_path = os.path.join(input_dir, 'a.xlsx')

# 定义拆分文件的数量
Num_file = 10  # 你可以根据需要更改这个值

# 读取Excel文件
df = pd.read_excel(input_file_path)

# 获取标题行和数据行
header = df.iloc[0]
data = df[1:]

# 计算每个文件的行数
num_rows = len(data)
rows_per_file = num_rows // Num_file

# 拆分数据并保存到不同的文件中
for i in range(Num_file):
    start_row = i * rows_per_file + 1
    if i == Num_file - 1:  # 确保最后一个文件包含所有剩余行
        end_row = num_rows + 1
    else:
        end_row = (i + 1) * rows_per_file + 1

    split_data = data[start_row - 1:end_row - 1]
    split_df = pd.concat([header.to_frame().T, split_data])
    
    output_file_path = os.path.join(input_dir, f'a{i+1}.xlsx')
    split_df.to_excel(output_file_path, index=False)

print("文件拆分完成！")
