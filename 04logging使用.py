#!/usr/bin/env python3
# coding: utf-8

"""logging模块用法"""

import logging


def base():
    """logging模块的基本使用."""

    # 指定 filename 参数, 可将日志输出到指定文件, 同时屏幕上将不输出
    # format 参数可指定输出格式
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )
    s = '0'
    n = int(s)
    logging.info('n = %d' % n)
    print(10 / n)


def advance():
    """logging模块高级用法.
    
    既要把日志输出到控制台, 还要指定某个等级写入日志文件, 就要用这种方法.
    """

    # 第一步, 创建一个logger
    logger_name = 'test_log'
    logger = logging.getLogger(logger_name)  
    logger.setLevel(logging.INFO)  # 输出到屏幕的log级别
    
    # 第二步, 创建一个handler, 用于输出到控制台
    cmd_handler = logging.StreamHandler()  
    
    # 第三步, 再创建一个handler, 用于写入日志文件
    log_file = 'logger.log'
    # delay 决定是否立即创建log文件，
    # 设为True，等有内容写入时，才创建
    file_handler = logging.FileHandler(log_file, mode='w', delay=True)
    file_handler.setLevel(logging.WARNING)  # 输出到file的log等级的开关
    
    # 第四步, 定义handler的输出格式
    formatter = logging.Formatter(
        '[%(asctime)s] - %(name)s - %(filename)s:%(lineno)d - %(levelname)-8s: %(message)s'
    ) 
    file_handler.setFormatter(formatter)  
    cmd_handler.setFormatter(formatter)
    
    # 第五步, 将logger添加到handler里面  
    logger.addHandler(file_handler)  
    logger.addHandler(cmd_handler)
    
    # 测试, 级别从低到高
    logger.debug('this is a logger debug message')  
    logger.info('this is a logger info message')  
    logger.warning('this is a logger warning message')  
    #logger.error('this is a logger error message')  
    #logger.critical('this is a logger critical message')


if __name__ == '__main__':
    advance()
