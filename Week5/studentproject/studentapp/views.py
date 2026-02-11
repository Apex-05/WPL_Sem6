from django.shortcuts import render

def student_form(request):
    details = ""
    percentage = None

    if request.method == "POST":
        name = request.POST.get("name")
        dob = request.POST.get("dob")
        address = request.POST.get("address")
        contact = request.POST.get("contact")
        email = request.POST.get("email")
        english = float(request.POST.get("english"))
        physics = float(request.POST.get("physics"))
        chemistry = float(request.POST.get("chemistry"))

        total = english + physics + chemistry
        percentage = total / 3

        details = (
            f"Name: {name}\n"
            f"DOB: {dob}\n"
            f"Address: {address}\n"
            f"Contact: {contact}\n"
            f"Email: {email}\n"
            f"English: {english}\n"
            f"Physics: {physics}\n"
            f"Chemistry: {chemistry}\n"
        )

    return render(request, "studentapp/form.html", {
        "details": details,
        "percentage": percentage
    })
