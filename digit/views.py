from django.shortcuts import render

def index(request):
    if request.method == 'POST':

        data = request.POST['img']
        if data:
            val = 1
        else:
            val = 0

        return render(request, 'digit/index.html',  {'img': val})
    else:
        return render(request, 'digit/index.html', {})
