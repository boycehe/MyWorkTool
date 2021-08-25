#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import os
import sys

def read_split_comma_data_to_array(data_path):
    with open(data_path,'r') as datafile:
        content = datafile.read()
        content = content.replace('\n','')
        return content.split(',')

if __name__ == '__main__':
    list = read_split_comma_data_to_array('/Users/boyce/Desktop/runloop_source_code.txt')
