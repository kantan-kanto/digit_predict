from django.shortcuts import render
from digit.dnn.predict import img_prp, answer
from digit.cnn.predict import img_prp_cnn, answer_cnn


def index(request):
    if request.method == 'POST':
        data = request.POST.getlist('img')
        cvssize = data[0]
        if data[1]:
            val = data[1]
            val = img_prp(val)
            val = answer(val)
            val = str(val).replace('[', '').replace(']', '')
        else:
            val = "No data"
        return render(request, 'digit/index_cnn.html',  {'img': val, 'cvssize': cvssize})
    else:
        return render(request, 'digit/index.html', {})


def index_cnn(request):
    if request.method == 'POST':
        data = request.POST.getlist('img')
        cvssize = data[0]
        if data[1]:
            val = data[1]
            val = img_prp_cnn(val)
            val = answer_cnn(val)
            val = str(val).replace('[', '').replace(']', '')
        else:
            val = "No data"
        return render(request, 'digit/index_cnn.html',  {'img': val, 'cvssize': cvssize})
    else:
        return render(request, 'digit/index_cnn.html', {})
