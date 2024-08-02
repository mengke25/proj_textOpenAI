import pandas as pd
import os

# 定义文件路径
input_dir = r'D:\project\July2024_textOpenAI\output'
output_file_path = os.path.join(input_dir, 'a.xlsx')

# 定义合并文件的数量
Num_file = 10  # 你可以根据需要更改这个值

# 读取第一个文件以获取标题行
df = pd.read_excel(os.path.join(input_dir, 'a1.xlsx'))
header = df.iloc[0].to_frame().T

# 合并数据
data_frames = [df[1:]]  # 去除标题行

# 读取剩余文件并合并
for i in range(2, Num_file + 1):
    file_path = os.path.join(input_dir, f'a{i}.xlsx')
    df = pd.read_excel(file_path)
    data_frames.append(df[1:])  # 去除标题行

# 纵向合并所有数据
merged_data = pd.concat(data_frames)

# 将标题行与数据合并
final_df = pd.concat([header, merged_data])

# 保存合并后的数据到新的Excel文件
final_df.to_excel(output_file_path, index=False)

print("文件合并完成！")
