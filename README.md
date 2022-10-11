# MDBot

使用MuseDash.moe数据及api开发的喵斯查分bot，可以实现绑定qq和md账号、查询b30、查询曲目信息、查询难度排行等功能（第一次开发qq机器人，难免会有不少bug，见谅ヽ(✿ﾟ▽ﾟ)ノ

## 部署

本插件基于Graia-Saya开发，部署方式见https://graiax.cn/社区文档 。部署完成后将mdbot整个文件夹放入modules，使用pip install -r requirements.txt安装依赖后运行即可，实测使用社区文档提供的样例代码可以正常运行。如果没有使用Graia-Saya，可以直接调用MDBot.py中的函数mdbot(qq, message)，传入字符型qq号和消息内容，将返回的字符串发出即可。
