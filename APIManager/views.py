import requests
from django.shortcuts import render

from APIManager.forms import *


def apimanager(request):
    result = ''

    if request.method == 'POST':
        form = SearchDocByID(request.POST)
        if form.is_valid():
            uuid = form.cleaned_data['UUID']

            uri = "http://tass-guy.preprod.tass.ru/admin/documents/delete"
            auth = requests.auth.HTTPBasicAuth("admin", "admin")
            headers = {
                "Content-Type": "application/json",
                "accept": "application/json",
            }

            body = {
                "document_ids": [],
                "document_1c_ids": [
                    str(uuid)
                ]
            }

            response = requests.post(uri, json=body, headers=headers, auth=auth)

            print(str(uuid), response.status_code, response.json())

            result = [str(uuid), response.status_code, response.json()]

        else:
            result = 'В поле введён не UUID, введите UUID в формате 40b24b4c-adaf-4527-ac7a-96c4ae073291'

    data = {
        'searchformTASSOVETS': SearchDocByID,
        'title': 'APIManager',
        'subtitle': '- Тассовец',
        'result': result,
    }

    return render(request, 'APIManager/apimanager.html', data)
