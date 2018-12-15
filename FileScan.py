#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 16:40
# @Author  : 焦仲平
# @File    : FileScan.py
# @project : LocalSyncStraight
import datetime
import os
import shutil
from LogWrite import LogWrite
from Base import Base


class FileScan(Base):
    def __init__(self):
        super().__init__()
        self.log = LogWrite()

    def _get_files(self, rootdir):
        lisr_file = self.traversal_files(rootdir)  # list_file=所有文件列表
        return lisr_file

    def _get_father_folder(self, rootdir):
        if rootdir.find(self.ddmsa) >= 0:
            re_str = self.ddmsa
        elif rootdir.find(self.dlmsa) >= 0:
            re_str = self.dlmsa
        elif rootdir.find(self.jzmsa) >= 0:
            re_str = self.jzmsa
        elif rootdir.find(self.ykmsa) >= 0:
            re_str = self.ykmsa
        elif rootdir.find(self.hldmsa) >= 0:
            re_str = self.hldmsa
        else:
            re_str = self.lnmsa
        return re_str

    def file_scan_main(self, rootdir):
        list_file = self._get_files(rootdir)
        re_str = self._get_father_folder(rootdir)
        for file in list_file:
            file_lnmsa = file.replace(re_str, self.lnmsa)
            if os.path.exists(file_lnmsa):  # lnmsa-site 文件夹中已有该文件，对比md5，若不同删除再传
                if self.md5file(file_lnmsa) == self.md5file(file):
                    continue
                else:
                    try:
                        # os.remove(file_lnmsa)
                        shutil.copyfile(file, file_lnmsa)
                        self.log.create("modify file succeed:"+file_lnmsa)
                    except:
                        self.log.create("modify file failed:"+file_lnmsa)
                        continue
            else:  # lnmsa-ste 文件夹中无该文件，直接传
                try:
                    # os.makedirs(os.path.dirname(file_lnmsa))
                    shutil.copyfile(file, file_lnmsa)
                    self.log.create("create file succeed:" + file_lnmsa)
                except:
                    self.log.create("create file failed:" + file_lnmsa)
                    continue
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  scan is over:" + rootdir)



