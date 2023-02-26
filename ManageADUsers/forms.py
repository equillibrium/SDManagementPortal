from crispy_forms import bootstrap, layout
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div
from django import forms
from django.forms import ModelForm, Form

from ManageADUsers.models import ADUser


class SearchADUser(Form):
    search = forms.CharField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.method = "POST"
        self.helper.form_class = 'form-inline align-items-center'

        self.helper.layout = Layout(
            Div(
                Div(bootstrap.InlineField('search', placeholder='Поиск'), css_class='col-sm-5 pe-1'),
                Div(bootstrap.FormActions(layout.Submit('submit', 'Найти', css_class='btn btn-secondary')),
                    css_class='col-sm-2 p-0'),
                css_class='row justify-content-md-center'
            )
        )


class ADUser(ModelForm):
    class Meta:
        model = ADUser
        fields = ['fullname', 'mail']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    bootstrap.InlineField('fullname'),
                    css_class='form-group col mx-0 px-0'
                ),
            ),
            Row(
                Column(
                    bootstrap.InlineField('mail'),
                    css_class='form-group col mx-0 px-0'
                ),
            ),
            Row(
                Column(
                    Submit('submit', 'Сохранить', css_class='btn-success'),
                    css_class='form-group col mb-0 p-0 m-0',
                ),

            ),
        )
