![cover](readme/cyberchat.png)
本项目继承自https://github.com/cjyaddone/ChatWaifu,支持了b站弹幕实时读取的功能.
# 使用ChatWaifu来回复你的b站直播弹幕
## b站设置直播相关(如果你不熟悉ChatWaifu项目,请先看后面的教程进行环境配置):
0.下载模型文件
> 前往 https://www.bilibili.com/read/cv21342054?from=search&spm_id_from=333.337.0.0 下载G_953000.pth和config.json,然后将文件拖入model/CN

1.在Start.py中设置直播间号
```python
# 直播间ID的取值看直播间URL
TEST_ROOM_IDS = [
    '25757456'
]
```
2.在Start.py中设置你的角色设定
```python
TEXT = '''
你现在是一个喝醉酒的醉汉,只会说胡话
'''
```
3.在AI.py中设置音色,注意由于使用到了原神的角色语音,请不要商用谢谢
```python
def __init__(self) -> None:
	session_token = get_token()
	self.api = ChatGPT(session_token)
	print(modelmessage)
	self.model_id = 0
	## 119 125 135 551
	## 这里输入AI的音色,执行python test.py 查看所有音色
	self.id = 551
	pass
```
4.启动程序
> python Start.py

5.启动之后按下面的教程复制你ChatGPT的Cookie到控制台.就OK了



[中文](README.md "中文") [English](eng-README.md "English") [日本語](jp-README.md "日本語")

<p align="center">
	<img alt="GitHub" src="https://img.shields.io/github/license/cjyaddone/ChatWaifu?color=red">
	<img src="https://img.shields.io/badge/Python-3.7|8|9|10-green" alt="PYTHON" >
  	<a href="https://app.fossa.com/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu?ref=badge_small" alt="FOSSA Status"><img src="https://app.fossa.com/api/projects/git%2Bgithub.com%2Fcjyaddone%2FChatWaifu.svg?type=small"/></a>
</p>

#

### 这是一个使用TTS+VITS的ChatGPT语音对话程序!

效果演示BiliBIli:[《青春猪头少年不会梦见赛博女友》](https://www.bilibili.com/video/BV1rv4y1Q7eT "BiliBili")

**当前支持功能：**
* [x] ChatGPT的对话聊天
* [x] 回答转语音
* [x] 多角色语音
* [x] 语音识别对话 (研发了一款真正人性化的智能语音Q宝
* [x] [对接Marai机器人](https://github.com/MuBai-He/ChatWaifu-marai)
* [x] [对接Live2D的UI版本](https://github.com/cjyaddone/ChatWaifuL2D)



# 目录
### 本项目均默认使用Chrome浏览器
* [1.安装环境：](#1.)
	* 1.1 [使用cd命令进入项目文件夹](#cd)
	* 1.2 [创建Python虚拟环境:](#99)
	* 1.3 [进入创建好的虚拟环境:](#venv)
	* 1.4 [pip安装项目所需要的库文件:](#pip)
* [2.导入模型到根目录model文件夹（如果没有自行创建):](#.model)
	* 2.1 [双击导入model](#cd1)
* [3.运行（快和我的老婆们对话吧:](#22)
	* 3.1 [获取ChatGPT Token](#333)
	* 3.2 [开始和CyberWaifu聊天](#444)
* [4.鸣谢](#915)
## <span id="1.">1.安装环境：</span>
> **安装anaconda环境或Python>=3.7**
> 
> **本例使用的环境名称是：chatWaifu**

### <span id="cd">1.1 使用cd命令进入项目文件夹</span>
`cd 你的项目路径`
![](readme/5.png)
### <span id="99">1.2 创建Python虚拟环境:</span>

Conda:`conda create --name chatWaifu python=3.10`
![](readme/1.png)
![](readme/2.png)
Python:`python -m venv chatWaifu`
![](readme/6.png)

### <span id="venv">1.3 进入创建好的虚拟环境:</span>
Conda:`conda activate chatWaifu`
![](readme/3.png)

Python:`.\chatWaifu\Scripts\activate.bat`
![](readme/7.png)

### <span id="pip">1.4 pip安装项目所需要的库文件:</span>
`pip install -r requirements.txt`
![](readme/4.png)

## <span id=".model">2.导入模型到根目录model文件夹:</span>
Google Drive:https://drive.google.com/file/d/1tMCafhnUoL7FbevVQ44VQi-WznDjt23_/view?usp=sharing

阿里云盘: https://www.aliyundrive.com/s/9JEj1mp1ZRv 提取码: m2y3

### <span id="cd1">2.1移动到项目根目录下双击导入model</span>

## <span id="22">3.运行（快和老婆们对话吧:</span>

打字输入版：`python ChatWaifu.py`

语音对话版（日语和英语输入默认日语输出）：`python ChatWaifuVoice.py`

### 以下也可以使用，每个文件只对应一种语音输出输入模式

打字日语版：`python ChatWaifuJP.py`

打字中文版：`python ChatWaifuCN.py`

日语语音对话版（使用中文）：`python ChatWaifuJPVoice.py`

中文语音对话版（使用中文）：`python ChatWaifuCNVoice.py`

日文语音对话版（使用英文）：`python ChatWaifuJPVoiceEN.py`

日语语音对话版（使用日文）：`python ChatWaifuJPVoiceJP.py`

### <span id="333">3.1 获取ChatGPT Token</span>
#### 在浏览器登入https://chat.openai.com
#### 按F12进入开发控制台
#### 找到 应用程序 -> cookie -> __Secure-next-auth.session-token
![](readme/token.png)
#### 将值复制进入终端并回车

### <span id="444">3.2 开始和CyberWaifu聊天！！！</span>

**语音对话版:** 当控制台提示"You:"时开始说话，说完并出现句子录音结束并发送到ChatGPT对话。

附赠:[ChatGPT 中文调教指南](https://github.com/PlexPt/awesome-chatgpt-prompts-zh)

## <span id="915">4.鸣谢：</span>
- [MoeGoe_GUI]https://github.com/CjangCjengh/MoeGoe_GUI
- [Pretrained models]https://github.com/CjangCjengh/TTSModels
- [PyChatGPT]https://github.com/terry3041/pyChatGPT
