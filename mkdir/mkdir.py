#encoding:utf-8
r"""
创建文件目录，从命令行接收url
"""

import sys
import os


def mkdir(path):
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("\\")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print path+' "create success"'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' already exit'
        return False
 
# 定义要创建的目录
mkpath=r"E:\test\WWW1\mobile\components"
try:
  input_path = r'' + sys.argv[1]
except IndexError, e:
  input_path = ''
if(input_path):
  mkpath = input_path
# 调用函数
mkdir(mkpath)