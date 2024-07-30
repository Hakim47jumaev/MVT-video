from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
    path('',VideoListView.as_view(),name='home'),
    
    path('cat-s',CatListView.as_view(),name='cat-list'),
    path('cr-cat',CatCreateView.as_view(),name='cr-cat'),
    path('up/<int:pk>',CatUpdateView.as_view(),name='cat-up'),
    path('del/<int:id>',cat_del,name='del-cat'),

    path('vid-s',VidListView.as_view(),name='video-list'),
    path('cr-vid',VideoCreateView.as_view(),name='cr-vid'),
    path('update/<int:pk>/', VidUpdateView.as_view(), name='video-update'),
    path('del/<int:id>',vid_del,name='del-vid'),

    path('video/<int:pk>',VideoDetailView.as_view(),name='hello'), 
    path('det/video/<int:pk>',VideoDetailView.as_view(),name='hello'), 

    path('about-us',open,name='open'),

    path('det/<int:pk>',CategoryDetailView.as_view(),name='hi')
]




if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)