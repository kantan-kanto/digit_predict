from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        data = request.POST['img']
        if data:
            val = data
        else:
            val = 0
        return render(request, 'digit/index.html',  {'img': val})
    else:
        return render(request, 'digit/index.html', {})
