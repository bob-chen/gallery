'''
Created on Mar 20, 2015

@author: Bob.Chen
'''


from django import template

register = template.Library()

import random

@register.filter
def imageFilter(imageName):  
    
    # just for test
    pointX = random.randint(1, 100)
    pointY = random.randint(1, 100)
    width = random.randint(1, 100)
       
    return "/photo/%s?pointX=%s&pointY=%s&width=%s" % (imageName, pointX, pointY, width)


