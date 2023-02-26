from django.shortcuts import render

from NewADUser.forms import NewADUserForm


def createadaccount(request):
    error = ''
    if request.method == 'POST':
        form = NewADUserForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма неверна'

    form = NewADUserForm

    data = {
        'form': form,
        'title': 'Создание учетной записи в домене corp.tass.ru',
    }
    return render(request, 'NewADUser/createadaccount.html', data)
