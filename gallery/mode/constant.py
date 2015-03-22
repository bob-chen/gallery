# -*- coding: utf-8 -*-
'''
Created on Mar 19, 2015

@author: Bob.Chen
'''

from gallery_site.settings import MEDIA_ROOT, MEDIA_URL

# session key
#SESSION_LOGIN_KEY = "user"


TAG_ERROR_CODE = "errorcode" # error code
TAG_ERROR_MSG = "errormsg" # error message

RS_SUCCESS = "0"
RS_FAILURE = "1"

INT_RS_SUCCESS = 0
INT_RS_FAILURE = 10

INT_401_Unauthorized = 11


PHOTO_DATA_ROOT = MEDIA_ROOT + "images/"
PHOTO_URL_ROOT = MEDIA_URL + "images/"




