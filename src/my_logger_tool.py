import logging
import sys

__author__ = 'doom'

class MyLogger:
    def __init__(self, name, set_level=logging.DEBUG):
        # 设置logger的name属性
        self._name = name
        self._logger = logging.getLogger(self._name)
        # 设置logger的等级
        self._set_level = set_level
        self._logger.setLevel(self._set_level)
        # 设置logger日志输出格式
        self._format = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
        # 日志文件输出
        self._file_handler = logging.FileHandler(self._name + '.log')
        # 输出格式
        self._file_handler.setFormatter(self._format)
        # 终端输出
        self._terminal_handler = logging.StreamHandler(sys.stdout)
        # 输出格式
        self._terminal_handler.setFormatter(self._format)
        # 将logger添加输出处理
        self._logger.addHandler(self._file_handler)
        self._logger.addHandler(self._terminal_handler)

    def write_log(self, info, level='debug'):
        if level == 'critical':
            self._logger.critical(info)
        elif level == 'error':
            self._logger.error(info)
        elif level == 'warning':
            self._logger.warning(info)
        elif level == 'info':
            self._logger.info(info)
        else:
            self._logger.debug(info)

    def remove_log(self):
        if self._logger:
            self._logger.removeHandler(self._file_handler)
            self._logger.removeHandler(self._terminal_handler)
