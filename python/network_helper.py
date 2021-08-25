#!/usr/bin/env python
# -*- coding: utf-8 -*-ii m
import json_helper
import os

def download_url_list(url_list,path):
    for url in url_list:
        cmd = 'wget --content-disposition "%s" -P %s ' % (url, path)
        os.system(cmd)

if __name__ == '__main__':
    download_url_list(json_helper.read_split_comma_data_to_array('/Users/boyce/Desktop/runloop_source_code.txt'),'/Users/boyce/Desktop/runloop/')

