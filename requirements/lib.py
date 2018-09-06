#-*- coding: utf-8 -*-
#
# Author:: Jonny
# Date:: 2018/9/6
import os


def get_pip_list_dict():
    pip_list_str = os.popen("pip list").read()
    pip_list = pip_list_str.split("\n")[:-1][2:]
    pip_list_dict = {}
    for item in pip_list:
        item_list = item.strip(" ").split(" ")
        pip_list_dict[item_list[0]] = item_list[len(item_list) - 1]
    return pip_list_dict


def get_requirements_dict(file):
    requir_dict = {}
    f = open(file, "r+", encoding="utf-8")
    f_list = f.readlines()
    for item in f_list:
        item_list = item.strip("==").split("==")
        try:
            value_tmp = item_list[1].replace("\n", "")
            requir_dict[item_list[0]] = value_tmp
        except:
            pass
    return requir_dict