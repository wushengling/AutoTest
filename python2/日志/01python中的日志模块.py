#coding:utf-8
"""
日志:

python代码中如何去记录日志?
python内置模块:logging模块

logging模块中,有一个内置的日志收集器:root
root这个日志收集器:默认只收集WARNING以上的日志

"""
import logging
"""
python中的日志等级:
debug:输出详情的运行情况,主要用于调试
INFO:确认一切按预期运行,一般用于输出重要运行情况
WARNING:一些意想不到的事情发生了(比如:"警告内存空间不足"),但这个软件
        还能按预期工作,在不久的将来会出现问题
ERROR:发生了错误,软件没能执行一些功能,还可以继续执行
CRITICAL:一个严重的错误,表明程序本身可能无法继续运行
"""
logging.debug("这个是debug等级的日志")
logging.info("这个是info等级的日志")
logging.warning("这个是warning等级的日志")
logging.error("这个是error等级的日志")
logging.critical("这个是critical等级的日志")

#修改日志收集器的收集等级
