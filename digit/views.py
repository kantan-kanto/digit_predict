from django.shortcuts import render
from digit.predict import img_prp2, answer


def index(request):
    if request.method == 'POST':
        data = request.POST['img']
        if data:
            val = data
            val = img_prp2(val)
            val = answer(val)
            val = str(val).replace('[', '').replace(']', '')
        else:
            val = "No data"
        return render(request, 'digit/index.html',  {'img': val})
    else:
        return render(request, 'digit/index.html', {})
