from django.shortcuts import render


# Функция представления для страницы "О нас".
def about(request):
    template_name = 'pages/about.html'
    return render(request, template_name)


# Функция представления для страницы правил.
def rules(request):
    template_name = 'pages/rules.html'
    return render(request, template_name)
