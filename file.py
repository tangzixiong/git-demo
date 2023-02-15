"""
 open() 方法

Python open() 方法用于打开一个文件，并返回文件对象，在对文件进行处理过程都需要使用到这个函数，如果该文件无法被打开，会抛出 OSError。 
"""

# open() 函数常用形式是接收两个参数：文件名(file)和模式(mode)。

#               open(file, mode='r')

#完整的语法格式为
#                    open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)

# 参数说明:
                            # file: 必需，文件路径（相对或者绝对路径）。
                            # mode: 可选，文件打开模式
                            # buffering: 设置缓冲
                            # encoding: 一般使用 utf8
                            # errors: 报错级别
                            # newline: 区分换行符
                            # closefd: 传入的file参数类型
                            # opener: