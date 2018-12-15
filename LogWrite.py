#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime
import os
from Base import Base


class LogWrite(Base):
    def __init__(self):
        super().__init__()
        self.dt = datetime.datetime.now()
        self.da = self.dt.strftime('%Y-%m-%d')

        # self.directory = "./log"
        # self.os.chdir(self.directory)  # 切换到directory目录
        self.cwd = os.getcwd()  # 获取当前目录即log目录下

    def create(self, record):
        '''
        根据本地时间创建新文件，如果已存在则不创建
        '''
        # os.chdir(self.directory)  # 切换到directory目录
        self.cwd = os.getcwd()  # 获取当前目录即log目录下
        suffix = ".txt"
        new_file = self.da+suffix
        dtt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        record = dtt + "  "+record
        print(record)
        f = open(new_file, 'a')
        f.writelines(record+"\n")
        f.close()
        # os.chdir("../")
