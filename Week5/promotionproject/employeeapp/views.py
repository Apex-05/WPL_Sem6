from django.shortcuts import render
from datetime import date

def promotion_check(request):
    result = None

    if request.method == "POST":
        doj = request.POST.get("doj")
        doj_date = date.fromisoformat(doj)
        today = date.today()
        experience = (today - doj_date).days / 365

        if experience > 5:
            result = "YES"
        else:
            result = "NO"

    return render(request, "employeeapp/promotion.html", {
        "result": result
    })
