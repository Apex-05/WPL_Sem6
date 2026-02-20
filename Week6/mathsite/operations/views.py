from django.shortcuts import render

def home(request):
    result = None
    error = None

    if request.method == "POST":
        try:
            num1 = int(request.POST.get("num1"))
            num2 = int(request.POST.get("num2"))
            operation = request.POST.get("operation")

            if operation == "add":
                result = num1 + num2

            elif operation == "subtract":
                result = num1 - num2

            elif operation == "multiply":
                result = num1 * num2

            elif operation == "divide":
                if num2 == 0:
                    error = "Division by zero is not allowed."
                else:
                    result = num1 / num2

        except ValueError:
            error = "Please enter valid integers."

    return render(request, "operations/home.html", {
        "result": result,
        "error": error
    })
