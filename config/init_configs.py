# coding = utf-8

import os
from config import gol
import configparser


# 寻找file.ini绝对路径
def find_file_path():
    return os.path.dirname(os.path.abspath(__file__))


# 初始化配置函数
def init_config():
    # 初始化全局变量的字典
    gol._init()
    # 读取路径的配置文件(**原本是ConfigParser,但是读取%号会有异常**)
    cf = configparser.RawConfigParser()
    # 邮箱配置文件
    cf.read([os.path.join(find_file_path(), 'mail_settings.ini')], encoding='utf-8')
    mail_host = cf.get('mail-server', 'mail_host')  # 邮箱服务器
    mail_port = int(cf.get('mail-server', 'mail_port'))  # 邮箱服务器端口
    mail_user = cf.get('mail-client', 'mail_user')  # 邮箱用户名
    mail_pwd = cf.get('mail-client', 'mail_pwd')  # 邮箱密码
    mail_receivers = cf.get('mail-receivers', 'mail_receivers')  # 收件人邮箱
    # 放入全局dict中对应变量
    gol.set_value('mail_host', mail_host)
    gol.set_value('mail_port', mail_port)
    gol.set_value('mail_user', mail_user)
    gol.set_value('mail_pwd', mail_pwd)
    gol.set_value('mail_receivers', mail_receivers)
    print('===加载mail_settings.ini配置文件完毕=== ...')

    # 加载linux配置文件相关信息
    cf.read([os.path.join(find_file_path(), 'linux_config.ini')], encoding='utf-8')
    ip = cf.get('server-ip', 'ip')
    login_info = cf.get('server-login', 'login_info')
    gol.set_value('ip', ip)
    gol.set_value('login_info', login_info)
    # 读取不同ip对应不同的命令
    cmd_list = cf.items('cmd')
    gol.set_value('cmd_list', cmd_list)
    print('===加载linux_config.ini配置文件完毕===...')

    # 加载cron时间配置文件相关信息
    cf.read([os.path.join(find_file_path(), 'time_config.ini')], encoding='utf-8')
    year = cf.get('cron','year')
    month = cf.get('cron','month')
    day = cf.get('cron','day')
    week = cf.get('cron','week')
    day_of_week = cf.get('cron','day_of_week')
    hour = cf.get('cron','hour')
    minute = cf.get('cron','minute')
    second = cf.get('cron','second')
    gol.set_value('year', year)
    gol.set_value('month', month)
    gol.set_value('day', day)
    gol.set_value('week', week)
    gol.set_value('day_of_week', day_of_week)
    gol.set_value('hour', hour)
    gol.set_value('minute', minute)
    gol.set_value('second', second)
    print('===time_config.ini配置文件完毕===...')


def get_linux_config():
    ''' 获取linux 配置文件相关ip对应user,password 放入dict中'''
    linux_dict = {}
    ip_list = gol.get_value('ip').split(',')  # ip列表
    login_info_list = gol.get_value('login_info').split(';')  # 登录列表
    ''' zip打包用法,同时遍历两个list '''
    for ip, login_info in zip(ip_list, login_info_list):
        linux_dict[ip] = login_info
    return linux_dict


if __name__ == '__main__':
    ''' 以下为测试,忽略 '''
    init_config()
