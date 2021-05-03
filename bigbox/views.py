from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Box, Activity

def home(request):
    return render(request, "bigbox/challenge.html")

def boxes(request):
    box_list = Box.objects.all()
    return render(request, "bigbox/box_list.html", {'boxes': box_list})

def information(request, box_id):
    box_detail = get_object_or_404(Box, id=box_id)
    return render(request, "bigbox/box_detail.html", {'information': box_detail})

def activities(request, box_id):
    activity_list = Activity.objects.all().order_by("id")
    paginator = Paginator(activity_list, 20)
    page = request.GET.get('page')
    activities_pagination = paginator.get_page(page)
    return render(request, "bigbox/activity_list.html", {'activities': activities_pagination})

def relation(request, box_id, activity_id):
    activity_detail = get_object_or_404(Activity, id=activity_id)
    return render(request, "bigbox/activity_detail.html", {'relation': activity_detail})

# def label(request, slug):
    # label_detail = get_object_or_404(Box, slug=slug)
    # return render(request, "bigbox/label_detail.html", {'label': label_detail})