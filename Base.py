#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 16:24
# @Author  : 焦仲平
# @File    : base.py
# @project : LocalSyncStraight
import os
import hashlib


class Base (object):
    def __init__(self):
        self.source = [
                        "E:\\wwwroot_release\\ddmsa-site\\upload\\resources\\image",
                        "E:\\wwwroot_release\\dlmsa-site\\upload\\resources\\image",
                        "E:\\wwwroot_release\\hldmsa-site\\upload\\resources\\image",
                        "E:\\wwwroot_release\\jzmsa-site\\upload\\resources\\image",
                        "E:\\wwwroot_release\\ykmsa-site\\upload\\resources\\image"
                       ]
        self.target = "E:\\wwwroot_release\\lnmsa-site\\upload\\resources\\image"
        self.lnmsa = "lnmsa-site"
        self.ddmsa = "ddmsa-site"
        self.dlmsa = "dlmsa-site"
        self.ykmsa = "ykmsa-site"
        self.hldmsa = "hldmsa-site"
        self.jzmsa = "jzmsa-site"

    def traversal_files(self, root_dir):
        _files = []
        list_files = os.listdir(root_dir)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list_files)):
            path = os.path.join(root_dir, list_files[i])
            if os.path.isdir(path):
                _files.extend(self.traversal_files(path))
            if os.path.isfile(path):
                _files.append(path)
        return _files

    @staticmethod
    def md5file(dir_file):
        md5file = open(dir_file, 'rb')
        md5 = hashlib.md5(md5file.read()).hexdigest()
        md5file.close()
        return md5
