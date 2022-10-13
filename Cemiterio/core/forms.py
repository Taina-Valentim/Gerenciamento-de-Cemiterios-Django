from core.models import Jazigo, Obito, Sepultamento
from django.forms import ModelForm
from bootstrap_datepicker_plus import DateTimePickerInput

class FormJazigo(ModelForm):
    class Meta:
        model = Jazigo
        fields = '__all__'

class FormObito(ModelForm):
    class Meta:
        model = Obito
        fields = '__all__'
        widgets = {'dataObito': DateTimePickerInput()}

class FormSepultamento(ModelForm):
    class Meta:
        model = Sepultamento
        fields = '__all__'
        widgets = {'dataSepultamento': DateTimePickerInput()}
