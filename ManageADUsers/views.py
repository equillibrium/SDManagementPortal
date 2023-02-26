from django.shortcuts import render

from ManageADUsers.ad import *
from ManageADUsers.forms import ADUser, SearchADUser


def manageADUsers(request):
    error = ''
    users = ''
    dict_users = {}

    if request.method == 'POST':
        form = SearchADUser(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
            result = find_ad_users(search)

            dict_users = {
                'FullName': [],
                'DP': [],
            }

            for u in result:
                dict_users['DP'].append(u['TASS-1C-DepartmentPath'].value)
                dict_users['FullName'].append(u.name.value)

            for items in dict_users.items():
                for i in items:
                    print(i)


        else:
            error = 'Форма неверна'

    searchform = SearchADUser
    userform = ADUser

    data = {
        'searchform': searchform,
        'userform': userform,
        'title': 'Управление учетной записью в домене corp.tass.ru',
        'dict_users': dict_users,
    }

    return render(request, 'manageADUsers/manageADUsers.html', data)
