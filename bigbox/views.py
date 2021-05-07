from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
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
    boxes = get_object_or_404(Box, id=box_id)
    activity_list = boxes.activities.all().order_by('id')
    #----
    page = request.GET.get('page', 1)
    # ----
    paginator = Paginator(activity_list, 20)
    try:
        activities = paginator.page(page)
    except PageNotAnInteger:
        activities = paginator.page(1)
    except EmptyPage:
        activities = paginator.page(paginator.num_pages)
    return render(request, "bigbox/activity_list.html", {'activities': activities})

def relation(request, box_id, activity_id):
    activity_detail = get_object_or_404(Activity, id=activity_id)
    return render(request, "bigbox/activity_detail.html", {'relation': activity_detail})

def label(request, box_slug):
    box_label_detail = get_list_or_404(Box)
    return render(request, "bigbox/sample.html", {'label': box_label_detail})