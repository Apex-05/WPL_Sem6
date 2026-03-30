from django.shortcuts import render, redirect
from django.http import HttpResponse


def index(request):
    manufacturers = [
        "Toyota",
        "Honda",
        "Ford",
        "BMW",
        "Tesla"
    ]
    return render(request, "cars/index.html", {"manufacturers": manufacturers})


def result(request):
    if request.method == "POST":
        manufacturer = request.POST.get("manufacturer")
        model = request.POST.get("model")

        context = {
            "manufacturer": manufacturer,
            "model": model
        }
        return render(request, "cars/result.html", context)

    return redirect("index")