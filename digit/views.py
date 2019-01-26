from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# from django.template.response import TemplateResponse
# from django.http import HttpResponse, HttpResponseRedirect
# from django.utils import timezone
# from .models import Post
# from io import BytesIO
# from PIL import Image
# import re
# import base64


@csrf_exempt
def index(request):
    if request.method == 'POST':

        data = request.POST['img']
        if data:
            val = 1
        else:
            val = 0

        #image_width = int(request.POST['width'])
        #image_height = int(request.POST['height'])
        #image_data = re.sub("^data:image/png;base64,", "", image_data)
        #image_data = base64.b64decode(image_data)
        #image_data = BytesIO(image_data)
        #im = Image.open(image_data)

        # return HttpResponseRedirect('/', {'img': 'val'})
        return render(request, 'digit/index.html',  {'img': val})
    else:
        return render(request, 'digit/index.html', {})
