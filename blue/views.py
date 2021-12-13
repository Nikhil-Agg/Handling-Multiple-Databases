from django.shortcuts import render
from .models import test
# Create your views here.
def index(requests):
    if requests.method == 'POST':
        title = requests.POST['title']
        detail = requests.POST['detail']

        obj = test(title=title, detail=detail,)
        obj.save()
    return render(requests, 'index.html')