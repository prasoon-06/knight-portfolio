from django.shortcuts import render
from .models import SiteProfile, Project, ChapterImage

def home(request):
    profile = SiteProfile.objects.order_by("-updated_at").first()
    projects = Project.objects.order_by("sort_order", "title")

    c2 = ChapterImage.objects.filter(chapter="philosophy").order_by("sort_order").first()
    c3 = ChapterImage.objects.filter(chapter="teen").order_by("sort_order").first()
    c4 = ChapterImage.objects.filter(chapter="adult").order_by("sort_order").first()
    c5 = ChapterImage.objects.filter(chapter="battles").order_by("sort_order").first()
    c6 = ChapterImage.objects.filter(chapter="old").order_by("sort_order")[:4]


    return render(request, "portfolio/home.html", {
        "profile": profile,
        "projects": projects,
        "c2_img": c2,
        "c3_img": c3,
        "c4_img": c4,
        "c5_img": c5,
        "c6_imgs": c6,
    })
