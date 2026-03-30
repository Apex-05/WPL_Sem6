from django.shortcuts import render

def form(request):

    if request.method == "POST":

        name = request.POST.get("name")

        return render(request,"feedback/result.html",{
            "name":name
        })

    return render(request,"feedback/form.html")