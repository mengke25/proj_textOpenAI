# 调用大模型接口批量处理文本

# readme.md

author:  mengke25 <br />
个人主页：[personal website](https://mengke25.github.io); <br />
教程：[视频](https://b23.tv/QQ54Vux)


## 1. project简介

### （1）概况

用于在excel中调用chatGPT、Claude等AI，帮忙进行自然语言处理，并输出相应的内容。它是一个专门做dirty work的RA

### （2）主要功能

我们把自然语言放到excel的某一列，比如是一段文本
我们可以在promot中说‘请帮我提炼关键词’，‘请帮我总结’，‘请帮我翻译’，‘请判断是积极还是消极’，‘请帮我做相应的处理’
AI会根据我们输入的文本，给出相应的处理结果，并输出到excel的某一列

（为了提高运行速度，我将每个`xlsx`拆成了10个，同时运行。）

### （3）应用场景

1. 文本分析：对文本进行分析，提取关键词，判断情感倾向等
2. 文本处理：对文本进行清洗，去除无用信息，提取关键信息等
3. 文本翻译：将文本翻译成另一种语言
4. 文本分类：对文本进行分类，比如新闻、评论、微博等
5. 文本生成：根据输入文本，生成相应的文本
6. 文本推荐：根据用户的兴趣，推荐相关的文本
7. 文本摘要：对文本进行摘要，生成简短的文本
8. 文本风格迁移：将文本风格迁移到另一种风格
9. 文献综述撰写：根据文献，生成综述

<br /> <br />



## 2.本地部署教程

第一步，将项目下载到本地

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s1.png)

或者在cmd中可直接clone

```python
d:
git clone https://github.com/mengke25/proj_textOpenAI.git
```

比如在这里，我直接将项目整体放在了D盘中

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s2.png)



第二步，安装依赖

在cmd中安装需用到的packages

```python
# 首先，将路径切换到根目录下
d: 
cd d:\proj_textOpenAI-main


# 选择1：使用python安装，requirements.txt中的包
python -m pip install -r requirements.txt


# 选择2：如果是conda用户，安装requirements.txt中的包方式如下（附虚拟环境）
conda create -n env2 python=3.11    # 创建anaconda环境
conda activate env2                 # 激活anaconda环境
python -m pip install -r requirements.txt
```





用编译器打开该项目的文件夹，此处我用vscode来演示

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s3.png)

打开文件夹后，请找到`config`路径下的`json`文件，以及`script`路径下的`main.py`

这两个文件是本项目的核心文件

其中`config.json`中定义了宏变量，`main.py`则是主脚本

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s4.png)

至此，本地部署已完成。下面我来介绍该如何使用。



## 3. 使用方法

使用方法非常简单，分两步——修改宏变量+运行主脚本

### （1）step1：改宏变量

第一步，修改`config`路径下的`json`配置文件，prompt改成自己的需求，其中：   

* `root_path`： 项目路径，即本地路径，例如打包下载到D盘，那项目路径就应该是`D:\\proj_textOpenAI-main`，注意这里是双斜杠
* `chatfile`：待处理文件，也即要读取的文件
* `apikey`：是openai的api key，需要自己申请
* `apiurl`：是openai的api url，需要自己申请
* `model_name`：是AI模型的名称，支持 "gpt-3.5-turbo"等
* `input_col`：是输入文本所在的列，也即想输入给AI的列
* `output_col`：是输出结果所在的列，也即想让AI输出在excel的哪一列
* `python_env`：所使用的python环境，一般情况下应该是"base"
* `script_parallelism`：是脚本并行度，即运行几个脚本，一般设置为10，最多不超过30
* `prompt_template`：是AI的提示模板，可以自己修改
* `system_message`：是系统提示语，可以自己修改

***一个示例：***

```json
{
    "global": {
        "root_path": "D:\\proj_textOpenAI-main",
        "chatfile": "D:\\proj_textOpenAI-main\\orig_file\\targetfile.xlsx", 
        "apikey": "sk-aUF5e29*****************8f6SeLz",
        "apiurl": "https://api.gptsapi.net/v1",
        "model_name": "gpt-3.5-turbo",
        "input_col": 4,
        "output_col": 10,
        "python_env": "env2", 
        "script_parallelism": 20, 
        "prompt_template": "请根据我输入给你的文本，帮我判断一下这段文本是否属于abc。",
        "system_message": "你是一个帮助判断是否未规制的助手"
    }
}
```

<br /> <br />



### （2）step2：运行

第二步，修改好配置文件后，运行`main.py`。

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s5.png)

等运行完，去`output`文件夹将`'****_AIextract.xlsx'`找出来，即可。再生成最终文件的同时，还会生成若干个子文件，用于备份。如果不需要的话，可以直接删掉。

![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s6.png)

### （3）补充

对于pycharm用户，可能会遇到找不到相对路径的问题，

此时需要您去配置run config

具体步骤如下
![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s7.png)
![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s8.png)
![image](https://github.com/mengke25/proj_textOpenAI/blob/main/orig_file/s9.png)

至此，整个项目就已经部署好且已经完成运行。



--------------------------



欢迎star，打赏渠道

![image](https://github.com/mengke25/mengke25.github.io/blob/main/images/dashang.png)







