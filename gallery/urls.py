'''
Created on Feb 15, 2015

@author: root
'''
from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()



urlpatterns = patterns('gallery.views',
    # Examples:
    # url(r'^$', 'gallery_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    #url(r'^admin/', include(admin.site.urls)),
    
    url(r'^$','photo_view.index'),
    url(r'^(?i)index/$', 'photo_view.index'),
    
    url(r'^(?i)photo/(?P<imageName>.*)$', 'photo_view.photo'),
    url(r'^(?i)addPhoto/$', 'photo_view.addPhoto'),
    url(r'^(?i)getPhotos/$', 'photo_view.getPhotos'),
)

from gallery_site.settings import DEBUG
if DEBUG:
    urlpatterns += patterns('gallery.views.test', 
        url(r'^(?i)test/$', 'test_view.test'),
    )

