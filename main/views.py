from django.shortcuts import render

def show_main(request):
    context = {
        "npm": "2306227311",
        "name": "Franky Raymarcell Sinaga",
        "class": "PBP F"
    }

    return render(request, "main.html", context)
