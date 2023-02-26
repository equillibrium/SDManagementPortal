from crispy_forms import bootstrap
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column
from django.forms import ModelForm

from NewADUser.models import NewADUser


class NewADUserForm(ModelForm):
    class Meta:
        model = NewADUser
        fields = ['f', 'i', 'o']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column(
                    bootstrap.InlineField('f', placeholder='Фамилия'),
                    css_class='form-group col mx-0 px-0'
                ),
                Column(
                    bootstrap.InlineField('i', placeholder='Имя'),
                    css_class='form-group col mx-0 px-0'
                ),
                Column(
                    bootstrap.InlineField('o', placeholder='Отчество'),
                    css_class='form-group col mx-0 px-0'
                ),
                Column(
                    Submit('submit', 'Проверить', css_class='btn-secondary'),
                    css_class='form-group col mb-2 p-0 m-0'
                ),
            ),
        )
