"""
PyInstaller是一个十分有用的Python第三方库，
它能够在Windows、Linux、Mac OS X等操作系统下将Python源文件打包，变成直接可运行的可执行文件。
通过对源文件打包Python程序可以在没有安装Python的环境中运行，也可以作为一个独立文件方便传递和管理。
"""

"""
PyInstaller 有一些常用参数
参数                      功能
-h, --help               查看帮助
--clean                  清理打包过程中的临时文件
-D, --onedir             默认值，生成dist目录
-F, --onefile            在dist文件夹中只生成独立的打包文件
-i <图标文件名.ico >       指定打包程序使用的应用图标(icon)文件
"""
# 打包一个程序（游戏目录可以实操）
# pyinstaller -F -i 温馨提示.ico  温馨提示_早点休息.py
