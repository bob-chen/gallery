# -*- coding: utf-8 -*-

"""
Author:       Bob Chen
 
Copyright (c)  2015
"""

def getParam(request, key, defaultValue=None):
    '''This method is used for getting 
            parameter from web client request'''
    value = defaultValue
    if request.GET.has_key(key):
        value = request.GET[key]
    elif request.POST.has_key(key):
        value = request.POST[key]
    else:
        pass

    return value

#def checkFolder(userId):
#    try:
#        targetDir = (USER_DATA_AVATAR %  userId)
#        imageDir = (USER_DATA_IMAGES %  userId)
#        thumbDir = (USER_DATA_THUMB %  userId)
#        coverDir = (USER_DATA_COVER % userId)
#        if not os.path.exists(targetDir):
#            cmd = "mkdir -p %s %s %s %s 1>/dev/null 2>/dev/null" % (targetDir, imageDir, thumbDir, coverDir)
#            ret = os.system(cmd)
#            if ret != 0:
#                Logger.SaveLogDebug("Failed to create user folder ", Logger.LEVEL_ERROR, "COMMON")
#    except Exception, ex:
#        print ex
#        return False
#    return True



    
    