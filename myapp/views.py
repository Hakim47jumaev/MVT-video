from typing import Any
from django.shortcuts import render,redirect
from .models import Video,Category
from django.views.generic import ListView,CreateView,UpdateView,DetailView

class VideoListView(ListView):
    model = Video
    template_name = "home.html"
    context_object_name='videos'


class CategoryListView(ListView):
    model = Category
    template_name = "home.html"
    context_object_name = 'catss' 

class CatListView(ListView):
    model = Category
    template_name = "list2.html"
    context_object_name='cats'

class VidListView(ListView):
    model = Video
    template_name = "list1.html"
    context_object_name='videos'



class CatCreateView(CreateView):
    model = Category
    template_name = "cr_cat.html"
    fields='__all__'
    success_url='cat-s'


class CatUpdateView(UpdateView):
    model = Category
    template_name = "up2.html"
    fields='__all__'
    success_url='cat-s'

class VidUpdateView(UpdateView):
    model = Video
    template_name = "up1.html"
    fields='__all__'
    success_url='vid-s'

def cat_del(request,id):
    mem=Category.objects.get(id=id)
    mem.delete()
    return redirect('cat-list')


def vid_del(request,id):
    mem=Video.objects.get(id=id)
    mem.delete()
    return redirect('video-list')


class VideoCreateView(CreateView):
    model = Video
    template_name = "cr_video.html"
    fields='__all__'
    success_url='vid-s'


class VideoDetailView(DetailView):
    model = Video
    template_name = "det.html"
    success_url='vid-s'
    context_object_name='video'

def open(mm):
    return render(mm,'about_us.html')


class CategoryDetailView(DetailView):
    model = Category
    template_name = "detail.html"
     

    def get_context_data(self, **kwargs) :
            context = super().get_context_data(**kwargs)
            context["videos"] = Video.objects.filter(category=kwargs['object'])
            return context
        
         
