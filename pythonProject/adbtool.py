import os
import platform
import re
import time


class AdbTools(object):
    def __init__(self, device_id=''):
        self.__system = platform.system()
        self.__find = ''
        self.__command = ''
        self.__device_id = device_id
        self.__get_find()
        self.__check_adb()
        self.__connection_devices()

    def __get_find(self):
        if self.__system == 'Windows':
            self.__find = 'findstr'
        else:
            self.__find = 'grep'

    def __check_adb(self):
        if "ANDROID_HOME" in os.environ:
            if self.__system == "Windows":
                path = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb.exe")
                if os.path.exists(path):
                    self.__command = path
                else:
                    raise EnvironmentError(
                        "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
            else:
                path = os.path.join(os.environ["ANDROID_HOME"], "platform-tools", "adb")
                if os.path.exists(path):
                    self.__command = path
                else:
                    raise EnvironmentError(
                        "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
        else:
            raise EnvironmentError(
                "Adb not found in $ANDROID_HOME path: %s." % os.environ["ANDROID_HOME"])
    def get_check(self):
        return self.__check_adb()

    def __connection_devices(self):
        pass
