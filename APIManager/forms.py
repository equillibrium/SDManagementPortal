from crispy_forms import bootstrap, layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div
from django import forms
from django.forms import Form

'''
class SearchJIRAUser(Form):
    search = forms.CharField(label='Введите username или Фамилию')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline align-items-center'

        self.helper.layout = Layout(
            Div(
                Div(bootstrap.InlineField('search'), css_class='col-sm-5 pe-1'),
                Div(bootstrap.FormActions(layout.Submit('submit', 'Найти', css_class='btn btn-secondary')),
                    css_class='col-sm-2 p-0'),
            css_class='row justify-content-md-center mb-4'
            )
        )

'''


class SearchDocByID(Form):
    UUID = forms.UUIDField(label='Введите ID Документа')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline align-items-center'

        self.helper.layout = Layout(
            Div(
                Div(bootstrap.InlineField('UUID'), css_class='col-sm-5 pe-1'),
                Div(bootstrap.FormActions(layout.Submit('submit', 'Удалить', css_class='btn btn-secondary')),
                    css_class='col-sm-1 p-0'), css_class='row justify-content-md-center'
            )
        )
