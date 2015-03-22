#from django.shortcuts import render

from django.shortcuts import render_to_response
from django.views.decorators.cache import never_cache
from django.http import HttpResponse, HttpResponseForbidden
from django.utils import simplejson

from gallery.mode.photo_manager import PhotoManager
from gallery.common import getParam
from gallery.mode.constant import TAG_ERROR_CODE, TAG_ERROR_MSG
from gallery.mode.error_api import Err

@never_cache
def index(request):
    
    page = getParam(request, 'page', 1)
    prePage = getParam(request, 'prePage', 5)
    
    errcode, errmsg, data = PhotoManager.getPhotos(page, prePage)
                   
    return render_to_response("index.html",{"photos":data})


def photo(request, imageName):
    
    pointX = getParam(request, 'pointX', 0)
    pointY = getParam(request, 'pointY', 0)
    width = getParam(request, 'width', 10)
    
    errcode, errmsg, data = PhotoManager.getPhoto(imageName, pointX, pointY, width)
    
    if errcode == Err.NO_ERROR:
        image = data[0].getvalue()
        imgFormat = data[1]
        
        return HttpResponse(image, content_type = "image/%s" % imgFormat)
    

def addPhoto(request):
    json = {}
    title = getParam(request, 'title', "")
    comment = getParam(request, 'comment', "")
    isUrl = getParam(request, 'isUrl', "false")
    url = getParam(request, "url", "")
    
    if isUrl == "false":
        content = request.FILES.get("photo", None)
        errcode, errmsg, data = PhotoManager.addPhoto(content, title, comment, isUrl=False)
    else:
        errcode, errmsg, data = PhotoManager.addPhoto(url, title, comment, isUrl=True)

    json[TAG_ERROR_CODE] = errcode
    json[TAG_ERROR_MSG] = errmsg
        
    jsonStr = simplejson.dumps(json)
    return HttpResponse(jsonStr, content_type = "text/html")

def getPhotos(request):
    json = {}
    page = getParam(request, 'page', 1)
    prePage = getParam(request, 'prePage', 10)

    errcode, errmsg, data = PhotoManager.getPhotos(int(page), int(prePage))
    
    json[TAG_ERROR_CODE] = errcode
    json[TAG_ERROR_MSG] = errmsg
    json["photoList"] = data
    
    jsonStr = simplejson.dumps(json)
    return HttpResponse(jsonStr, content_type = "text/html")
    