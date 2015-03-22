# -*- coding: utf-8 -*-
'''
Created on Mar 19, 2015

@author: Bob.Chen
'''

import inspect    
import traceback 
import os
#import time
import re
#import subprocess
#import logging
import logging.config
#import socket
import threading
#import fcntl
import random
import string
import types
from pipes import quote
from constant import PHOTO_URL_ROOT, PHOTO_DATA_ROOT

logPath = os.path.join(os.path.dirname(__file__), "../../logging.conf")
#print logPath
logging.config.fileConfig(logPath)


def QuoteString(src):
    return quote(src)

def randomNameFile(orgName, digit=32):
    return RandomID.gen(digit) + os.path.splitext(orgName)[1]

def getPhotoUrl(itemName):
    return PHOTO_URL_ROOT + itemName

def getPhotoPath(itemName):
    return PHOTO_DATA_ROOT + itemName
    
class Logger:
    """  Class for saving logs
    """
    LEVEL_DEBUG = logging.DEBUG
    LEVEL_INFO = logging.INFO
    LEVEL_WARNING = logging.WARNING
    LEVEL_ERROR = logging.ERROR
    LEVEL_CRITICAL = logging.CRITICAL
    levelMsg = {}
    levelMsg[LEVEL_DEBUG] = "DEBUG"
    levelMsg[LEVEL_INFO] = "INFO"
    levelMsg[LEVEL_WARNING] = "WARNING"
    levelMsg[LEVEL_ERROR] = "ERROR"
    levelMsg[LEVEL_CRITICAL] = "CRITICAL"
    
    def __init__(self):
        '''Init function'''
        pass
        
    @staticmethod
    def SaveLogDebug(msg, level = LEVEL_ERROR, module = "root", fileLine = None):
        """ Function to save logs  
        """
        try:            
            logger = logging.getLogger(module)            
            
            logMessage = str(msg)
            if fileLine != None:
                logMessage += "[FILE]: %s  [LINE]:%d" % fileLine
            
            if level == Logger.LEVEL_CRITICAL or level == Logger.LEVEL_ERROR:
                logMessage += traceback.format_exc()
            
            logger.log(level, logMessage)
        except Exception:
            pass
        
    @staticmethod
    def LogParameters(level = LEVEL_DEBUG, module = "root", fileLine = None, **parameters):
        try:
            message = ""
            for p in parameters:
                strMsg = ""
                try:
                    strMsg = str(p) + ":" + str(parameters[p]) + "   "
                except Exception, ex:
                    pass
                message = message + strMsg
            Logger.SaveLogDebug(message, level, module, fileLine)
        except Exception, ex:
            print str(ex)
        
    @staticmethod
    def getInspect():
        """  get debug line info
        """
        try:
            return inspect.stack()[1][1:3]
        except Exception:
            return None    
    
class RegEx:
    """  class provides regular expression match function 
    """
    def __init__(self):
        '''Init function'''
        pass
        
    @staticmethod
    def match(pattern = "", data = "", flags = 0):
        """  regular expression match  
        """
        try:
            p = re.compile(pattern, flags)
            if p != None:
                m = p.match(data)
                return m
            return None
        except Exception:
            return None

class RandomID:
    """  class provides regular random letters&digits function 
    """
    def __init__(self):
        '''Init function'''
        pass
        
    @staticmethod
    def gen(bit = 8):
        """  regular random letters&digits method  
        """
        try:
            p = ''.join(random.sample(string.ascii_letters + string.digits, bit))
            if p != None:
                return p
            return None
        except Exception:
            return None
        
    @staticmethod
    def genDigit(bit = 8):
        """ regular random digits method
        """ 
        try:
            p = ''.join(random.sample(string.digits, bit))
            if p != None:
                return p
            return None
        except Exception:
            return None
        
    @staticmethod
    def randomNameFile(orgName, digit=32):
        return RandomID.gen(digit) + os.path.splitext(orgName)[1]
    
    
class Singleton(object):
    __init = None        
    def __new__(cls):
        if cls.__init is None:
            cls.__init = object.__new__(cls)
        return cls.__init
    
class Lock:
    def __init__(self):
        self._lock = threading.Lock()
        
    def Lock(self):
        self._lock.acquire()
        
    def UnLock(self):
        self._lock.release()
        
