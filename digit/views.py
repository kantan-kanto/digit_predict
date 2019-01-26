from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect


# @csrf_exempt
# @csrf_protect
def index(request):
    if request.method == 'POST':
        from django.http import QueryDict

        # request.bodyに入っている。
        dic = QueryDict(request.body, encoding='utf-8')
        v1 = dic.get('key1')
        v2 = dic.get('k2')

        val = v1

        # r1, r2 = do_something(v1, v2)

        # from json import dumps
        # ret = dumps({'k1': r1, 'k2': r2})
        # return HttpResponse(ret, content_type='application/json')
        return render(request, 'digit/index.html', {'img': val})
    else:
        return render(request, 'digit/index.html', {})
