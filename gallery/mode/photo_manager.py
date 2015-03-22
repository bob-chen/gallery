# -*- coding: utf-8 -*-
'''
Created on Mar 19, 2015

@author: Bob.Chen
'''
import sys
import urllib2
import time
from PIL import Image
from constant import PHOTO_DATA_ROOT
from common import Logger, RandomID, getPhotoUrl, getPhotoPath
from error_api import Err
from gallery.models import Photo
from StringIO import StringIO


class PhotoManager(object):

    @staticmethod
    def addPhoto(content, title = "", comment = "", isUrl=False):
        Logger.LogParameters(funcname = sys._getframe().f_code.co_name, func_vars = vars(), module = "PhotoManager")
        try:
            imageName = RandomID.gen()
            
            if not isUrl:
                fileObj = StringIO(content.read())
            else:
                #url = "http://www.didao8.com:8080/static/44/thumb/nvLcHMu1JS3mepZPkQBqriG4ANthz2s5.jpg"
                fileObj = StringIO(urllib2.urlopen(content).read())
                
            img = Image.open(fileObj)
            width, height = img.size
            fileName = "%s%s%s" % (imageName, ".", img.format)
            filePath = (PHOTO_DATA_ROOT + "%s") % fileName
            img.save(filePath)
            
            photo = Photo(title=title, comment=comment, datetime = time.time(),
                          imageName=fileName, width = width, height = height)
            photo.save()
            
            return Err.genOK(photo.id)
        except Exception, ex:
            print ex
            Logger.SaveLogDebug(ex, level=Logger.LEVEL_ERROR, module = "PhotoManager")
            return Err.genErr(Err.ERR_ADD_PHOTO_FAIL)
            
    @staticmethod
    def getPhotos(page=1, prePage=5):
        Logger.LogParameters(funcname = sys._getframe().f_code.co_name, func_vars = vars(), module = "PhotoManager")
        try:
            photos = []
            intPage = int(page)
            intPrePage = int(prePage)
            
            photoItems = Photo.objects.all()[(intPage-1)*intPrePage:intPage*intPrePage]
            
            attrList = ["id", "title", "comment", "datetime", "width", "height", "imageName"]
            for item in photoItems:
                photo = {key:getattr(item, key) for key in attrList}
                photo["imageUrl"] = getPhotoUrl(item.imageName)
                photos.append(photo)
                
            return Err.genOK(photos)
        except Exception, ex:
            print ex
            Logger.SaveLogDebug(ex, level=Logger.LEVEL_ERROR, module = "PhotoManager")
            return Err.genErr(Err.ERR_GET_PHOTO_LIST_FAIL)

        
    @staticmethod
    def getPhoto(imageName, pointX=0, pointY=0, needWidth=0):
        '''
        Return a StringIO obj, use StringIO.getvalue() to get the content
        '''
        Logger.LogParameters(funcname = sys._getframe().f_code.co_name, func_vars = vars(), module = "PhotoManager")
        try:
            imagePath = getPhotoPath(imageName)
            needWidth, pointX, pointY = int(needWidth), int(pointX), int(pointY)
            
            im = Image.open(imagePath)
            width, height = im.size
            imgFormat = im.format
            scale = float(height)/width
            box = (0, 0, width, height)
            
            if needWidth > 0 and pointX < width and pointY < height:
                if needWidth + pointX > width:
                    needWidth = width - pointX
                needHeight = needWidth * scale
                if needHeight + pointY > height:
                    needHeight = height - pointY
                    needWidth = needHeight / scale
        
                if needHeight < 1:
                    needHeight = 1
                if needWidth < 1:
                    needWidth = 1
                print needHeight, needWidth    
                #print needWidth, needHeight, scale
                box = (pointX, pointY, int(pointX + needWidth), int(pointY + needHeight))
            
            region = im.crop(box)
            container = StringIO()
            region.save(container, imgFormat)
            
            return Err.genOK([container, imgFormat])
        except Exception, ex:
            print ex
            Logger.SaveLogDebug(ex, level=Logger.LEVEL_ERROR, module = "PhotoManager")
            return Err.genErr(Err.ERR_GET_PHOTO_DATA_FAIL)
        
            
            
            
        
        
        
        
        
    
                
        
        
        
        