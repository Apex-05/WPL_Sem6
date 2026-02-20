from django.shortcuts import render

def home(request):
    context = {}

    if request.method == "POST":

        # If Exit button pressed
        if "exit" in request.POST:
            context["exit"] = True
            return render(request, "formatter/home.html", context)

        # If Clear button pressed
        if "clear" in request.POST:
            return render(request, "formatter/home.html")

        name = request.POST.get("name")
        message = request.POST.get("message")
        color = request.POST.get("color")

        bold = request.POST.get("bold")
        italic = request.POST.get("italic")
        underline = request.POST.get("underline")

        formatted_text = f"Name: {name}<br>Message: {message}"

        style = ""

        if bold:
            style += "font-weight:bold;"
        if italic:
            style += "font-style:italic;"
        if underline:
            style += "text-decoration:underline;"
        if color:
            style += f"color:{color};"

        context["formatted_text"] = formatted_text
        context["style"] = style

    return render(request, "formatter/home.html", context)
