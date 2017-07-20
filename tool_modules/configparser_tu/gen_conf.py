#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jul 19, 2017

@author: Jack

tool_modules.configparser_tu.gen_conf is a configuration file generator
'''
from pathlib import Path
import configparser


static_path = Path('static')
try:
    static_path.mkdir(exist_ok=True)
except Exception as exc:
    print("Python version less than 3.5, you need to mkdir static manually.")

config = configparser.ConfigParser()

config['DEFAULT'] = {'ServerAliveInterval': 45,
                     'Compression': 'yes',
                     'CompressionLevel': 9}

config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
config['topsecret.server.com'] = {
    'Port': 50022
}
# topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('static/example.ini', 'w') as configfile:
    config.write(configfile)

if __name__ == '__main__':
    pass
