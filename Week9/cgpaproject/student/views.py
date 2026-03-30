from django.shortcuts import render, redirect

def page1(request):

    if request.method == "POST":

        name = request.POST.get("name")
        marks = int(request.POST.get("marks"))

        cgpa = marks / 50

        request.session["name"] = name
        request.session["cgpa"] = cgpa

        return redirect("result")

    return render(request,"student/page1.html")


def page2(request):

    name = request.session.get("name")
    cgpa = request.session.get("cgpa")

    return render(request,"student/page2.html",{
        "name":name,
        "cgpa":cgpa
    })