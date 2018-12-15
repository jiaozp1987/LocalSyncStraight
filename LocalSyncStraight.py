#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/12/9 18:07
# @Author  : 焦仲平
# @File    : LocalSyncStraight.py
# @project : LocalSyncStraight
import datetime
import os
import threading
import time

from FileScan import FileScan


class LocalSyncStraight(FileScan):
    def __init__(self):
        super().__init__()

    def local_sync_straight_main(self):
        list_source = []
        for i in self.source:
            if os.path.exists(i):
                list_source.append(i)
            else:
                continue
        if len(list_source) > 0:
            i = 0
            thread_list = []
            while 0 <= i < len(list_source):
                thread_list.append(threading.Thread(target=self.file_scan_main, args=(list_source[i],)))
                i += 1
            for th in thread_list:
                # th.setDaemon(True)
                th.start()
            for th in thread_list:
                th.join()
        else:
            self.log.create("source folder is not exist")


if __name__ == '__main__':
    lss = LocalSyncStraight()
    while 1:
        lss.local_sync_straight_main()
        print(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + "  all is over")
