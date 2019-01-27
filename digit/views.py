from django.shortcuts import render
from digit.predict import img_prp, img_prp2,answer


def index(request):
    if request.method == 'POST':
        data = request.POST['img']
        if data:
            # val = img_prp2(data)
            # val = answer(val)
            # val = str(answer(val)).replace('[', '').replace(']', '')
            val = data
        else:
            val = "No data"
        return render(request, 'digit/index.html',  {'img': val})
    else:
        return render(request, 'digit/index.html', {})
