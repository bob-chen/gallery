'''
Created on Mar 19, 2015

@author: root
'''
import unittest
import os
from PIL import Image

from gallery.models import Photo
from gallery.mode.photo_manager import PhotoManager
from gallery.mode.constant import PHOTO_DATA_ROOT

#import os,sys
#os.environ["DJANGO_SETTINGS_MODULE"] = "gallery_site.settings"
#sys.path.insert(0,r'/home/workspace/gallery_site')

class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def _testAddPhoto(self):
        # Test get photo from url
        url = "http://www.didao8.com:8080/static/44/thumb/nvLcHMu1JS3mepZPkQBqriG4ANthz2s5.jpg"
        title = "test1"
        comment = "Test get photo from url"
        errcode, errmsg, data = PhotoManager.addPhoto(url, title, comment, isUrl=True)
        self.assertEqual(errcode, 0, "return failed")
        
        item = Photo.objects.get(id=data)
        self.assertEqual(item.title, title, "title not match")
        self.assertEqual(item.comment, comment, "comment not match")
        
        imgPath = PHOTO_DATA_ROOT + item.imageName
        self.assertEqual(True, os.path.exists(imgPath), "image not saved")

        img = Image.open(imgPath)
        width, height = img.size
        self.assertEqual(item.width, width, "width not match")
        self.assertEqual(item.height, height, "comment not match")
        
    def _testGetPhotoList(self):
        
        errcode, errmsg, data = PhotoManager.getPhotos()
        print data
        self.assertEqual(errcode, 0, "return failed")
        self.assertTrue(len(data), "get photo list failed")
        
        # test pagination
        if len(Photo.objects.all()[0:4]) == 4:
            prePage = 2
            page = 1
            errcode, errmsg, data = PhotoManager.getPhotos(page = page, prePage = prePage)
            self.assertEqual(len(data), prePage, "pagination failed")
            errcode, errmsg, data = PhotoManager.getPhotos(page = page+1, prePage = prePage)
            self.assertEqual(len(data), prePage, "pagination failed")
        
        
    def testGetPhoto(self):
        id = 1
        photo = Photo.objects.get(id=1)
        imageName = photo.imageName
        print imageName
        errcode, errmsg, data = PhotoManager.getPhoto(imageName, 0, 0, 100)
        imageData = data[0]
        imageFormat = data[1]
        
        currImgName = "test."+imageFormat
        with open(currImgName, 'wb') as dest:
            dest.write(imageData.getvalue())
            dest.close()
            
        img = Image.open(currImgName)
        currWidth, currHeight = img.size
        self.assertEqual(100, currWidth, "get photo failed")
        
        
        orgScale = str(float(photo.height) / photo.width)
        currScale =  str(float(currHeight) / currWidth)

        self.assertEqual(orgScale[0:orgScale.index(".")+3], currScale[0:currScale.index(".")+3], "scale chagne")   



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()