from django.shortcuts import render
from digit.dnn.predict import img_prp, answer, pb_dnn
from digit.cnn.predict import img_prp_cnn, answer_cnn, pb_cnn
import numpy as np


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
        return render(request, 'digit/index.html',  {'img': val, 'cvssize': cvssize})
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


def index_j(request):
    if request.method == 'POST':
        data = request.POST.getlist('img')
        cvssize = data[0]
        if data[1]:
            val0 = data[1]
            val1_cnn = img_prp_cnn(val0)
            val = answer_cnn(val1_cnn)
            val = str(val).replace('[', '').replace(']', '')

            list_cnn = pb_cnn(val1_cnn)
            sort_cnn = list_cnn.argsort()
            dic_cnn = {}
            for i in range(10):
                dic_cnn[sort_cnn[0][i]] = '{:.5g}'.format(list_cnn[0][sort_cnn[0][i]])

            val1_dnn = img_prp(val0)
            list_dnn = pb_dnn(val1_dnn)
            sort_dnn = list_dnn.argsort()
            dic_dnn = {}
            for i in range(10):
                dic_dnn[sort_dnn[0][i]] = '{:.5g}'.format(list_dnn[0][sort_dnn[0][i]])
        else:
            val = None
        return render(request, 'digit/index_j.html',  {'img': val, 'cvssize': cvssize, 'list_cnn': dic_cnn, 'list_dnn': dic_dnn})
    else:
        return render(request, 'digit/index_j.html', {})
