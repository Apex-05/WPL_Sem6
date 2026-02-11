from django.shortcuts import render
from django.shortcuts import render
def square_view(request):
    result = None
    number = None
    if request.method == "POST":
        try:
            number = float(request.POST.get("number"))
            result = number ** 2
        except (ValueError, TypeError):
            result = "Invalid input! Please enter a number."
    return render(request, "mycalculator/square.html", {"result": result, "number": number})
