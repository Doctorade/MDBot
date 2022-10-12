# MDBot

使用从MuseDash.moe摸来的数据及api开发的喵斯查分bot，可以实现绑定qq和md账号、查询b30、查询曲目信息、查询难度排行等功能（第一次开发qq机器人，难免会有不少bug，见谅ヽ(✿ﾟ▽ﾟ)ノ

## 部署

本插件基于Graia-Saya开发，详细部署细节（如环境配置）参见[社区文档](https://graiax.cn/)。

如果你没有部署过机器人，可以使用以下开箱即用的部署方式（linux系统为例）：

1.按照社区文档安装mcl并登录运行。

2.git clone https://github.com/Doctorade/MDBot.git

3.cd MDBot

4.修改main-saya.py中qq号与机器人qq一致

5.poetry install

6.poetry run python ./main-saya.py

如果你部署过机器人并且也是基于Graia-Saya，那么将mdbot文件夹整个复制进你的modules目录下即可

如果你部署过机器人并且可以调用python接口，那么将字符型qq号和消息传入MDBot.mdbot(str(qq), message)即可
