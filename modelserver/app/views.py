from django.shortcuts import render


def Home(request):
    return render(request,"app/Home.html")
