from django.shortcuts import render
from .models import Articles
from .forms import ArticlesForm
def index(request):
    return render(request, 'index.html')

def tovar(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Товар был не правильно заполнен'


    form = ArticlesForm()

    date = {
        'form': form,
        'error': error
    }

    return render(request,'tovar.html',date)
