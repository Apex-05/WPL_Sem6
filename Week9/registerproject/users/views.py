from django.shortcuts import render

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        contact = request.POST.get("contact")

        context = {
            "username": username,
            "email": email,
            "contact": contact
        }

        return render(request, "users/success.html", context)

    return render(request, "users/register.html")