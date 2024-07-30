'''
 =======================================================================
 ····Y88b···d88P················888b·····d888·d8b·······················
 ·····Y88b·d88P·················8888b···d8888·Y8P·······················
 ······Y88o88P··················88888b·d88888···························
 ·······Y888P··8888b···88888b···888Y88888P888·888·88888b·····d88b·······
 ········888······"88b·888·"88b·888·Y888P·888·888·888·"88b·d88P"88b·····
 ········888···d888888·888··888·888··Y8P··888·888·888··888·888··888·····
 ········888··888··888·888··888·888···"···888·888·888··888·Y88b·888·····
 ········888··"Y888888·888··888·888·······888·888·888··888··"Y88888·····
 ·······························································888·····
 ··························································Y8b·d88P·····
 ···························································"Y88P"······
 =======================================================================

 -----------------------------------------------------------------------
Author       : 焱铭
Date         : 2023-07-25 10:15:12 +0800
LastEditTime : 2024-07-30 15:14:20 +0800
Github       : https://github.com/YanMing-lxb/
FilePath     : /YM-CFD-Automatic-Simulation-Software/Functional_modules/SearchRemove.py
Description  : 
 -----------------------------------------------------------------------
'''

import os

#  搜索并删除文件
def SearchRemove(window,path, suffix, key_word):
    for root, dirs, files, in os.walk(path):
        for i in files:
            if os.path.isfile(path + '/' + i):
                if i.endswith(suffix):
                    if key_word == "任意":
                        os.remove(os.path.join(root, i))
                        window['state_print'].print('已删除：' + i + ' 文件', text_color='blue')
                    if key_word in i:
                        os.remove(os.path.join(root, i))
                        window['state_print'].print('已删除：' + i + ' 文件', text_color='blue')