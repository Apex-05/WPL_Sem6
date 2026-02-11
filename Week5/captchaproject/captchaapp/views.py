from django.shortcuts import render
import random
import string

def generate_captcha():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def captcha_view(request):
    if 'captcha_text' not in request.session:
        request.session['captcha_text'] = generate_captcha()
    if 'attempts' not in request.session:
        request.session['attempts'] = 0

    message = ""
    result = ""
    disabled = False

    if request.method == "POST":
        user_input = request.POST.get("captcha")
        captcha_text = request.session.get('captcha_text', '')
        if user_input.upper() == captcha_text:
            message = "Captcha Matched Successfully!"
            result = "success"
            request.session['attempts'] = 0
            request.session['captcha_text'] = generate_captcha()
        else:
            request.session['attempts'] += 1
            message = "Captcha Mismatch!"
            result = "error"
            if request.session['attempts'] >= 3:
                disabled = True

    return render(request, "captchaapp/captcha.html", {
        "captcha": request.session.get('captcha_text'),
        "message": message,
        "result": result,
        "disabled": disabled,
        "request": request
    })
