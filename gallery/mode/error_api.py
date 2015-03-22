# -*- coding: utf-8 -*-
'''
Created on Mar 19, 2015

@author: Bob.Chen
'''

#from django.utils.translation import gettext
from common import Logger

class Err:
    '''
    class for message error code
    '''
    def __init__(self):
        '''
        Init function
        '''
        pass
    
    NO_ERROR = 0
    
    #error codes of GUI  
    ERR_ADD_PHOTO_FAIL = 700
    ERR_GET_PHOTO_LIST_FAIL = 701
    ERR_GET_PHOTO_DATA_FAIL = 702

    
    REG_EXP = 'REGULAR_EXP'
    MSG_KEY = 'MESSAGE_KEY'
    
    ERR_MESSAGES = { 
                    ERR_ADD_PHOTO_FAIL: 'Failed to add photo.',
                    ERR_GET_PHOTO_LIST_FAIL: 'Failed to get photo list.',
                    ERR_GET_PHOTO_DATA_FAIL: 'Failed to get photo data.'
                    }
    
        
    @staticmethod
    def genOK(data = None):
        Logger.SaveLogDebug(data, Logger.LEVEL_ERROR, "NoteManager")
        return Err.NO_ERROR, "", data
        
    @staticmethod
    def genErr(errCode, parameters = [], data = None):
        Logger.SaveLogDebug(data, Logger.LEVEL_ERROR, "NoteManager")
        return errCode, Err.getErrMessage(errCode, parameters), data

    @staticmethod
    def getErrMessage(errorcode, parameters = []):
        '''
        Method for get the localized error message by error code
        '''
        msg = ""
        if Err.ERR_MESSAGES.has_key(errorcode):
            msg = Err.ERR_MESSAGES[errorcode]
        else:
            Logger.SaveLogDebug('Error code (%d). No messages found', Logger.LEVEL_ERROR, 'Localization')
        
        try:        
            for i in range(0, len(parameters)):
                msg = msg.replace("{" + str(i) + "}", str(parameters[i]))
        except Exception, ex:
            Logger.SaveLogDebug("Unknow error for passing errorcode " + str(errorcode) + ":" + ex.str())
        return msg
    