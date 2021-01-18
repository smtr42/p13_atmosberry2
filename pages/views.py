from django.shortcuts import render


def frontpage(request):
    return render(request, "pages/index.html")


def dashboard(request):
    return render(request, "pages/dashboard.html")
