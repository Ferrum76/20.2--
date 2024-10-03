from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField, forms

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, ModelForm):
    bad_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('name',
                  'image',
                  'price',
                  'description',
                  'category',
                  )  # перечисляем поля для отображения

    def clean_name(self):
        clean_name = self.cleaned_data.get('name')
        for word in self.bad_words:
            if word in clean_name:
                raise forms.ValidationError(
                    "В названии продукта не должно быть запрещенных слов"
                )
        return clean_name

    def clean_description(self):
        cleaned_data = self.cleaned_data["description"]
        for word in self.bad_words:
            if word in cleaned_data:
                raise forms.ValidationError(
                    "В описании продукта не должно быть запрещенных слов"
                )
        return cleaned_data

class VersionForm(StyleFormMixin, ModelForm):
    class Meta:
        model = Version
        fields = ('product', 'version_name', 'version_number')  # перечисляем поля для отображения