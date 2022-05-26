from django import forms
from shortage.models import Core,CoreHistory,Mrp_element,Apro_spec

class Myform(forms.ModelForm):
    class Meta:
        model = Core
        fields = '__all__'
        exclude =['created_on','created_by','deleted','deleted_by','deleted_on','updated_by','updated_on','status','closing_date']
        widgets = {
            'requested_date': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'closing_date' : forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'created_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'deleted_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'updated_on': forms.DateInput(format=('%m/%d/%Y'),attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }
    def clean_material(self):
        material = self.cleaned_data['material']
        if len(material) == 0:
            raise forms. ValidationError("Material is requiered")
        return material

class Form(forms.ModelForm):
     class Meta:
        model = CoreHistory
        fields = '__all__'
        exclude =['core','created_on','created_by','action']
     def __init__(self, *args, **kwargs):
        super(Form, self).__init__(*args, **kwargs)
        self.fields['comment'].required = False
    

class Form_mrp(forms.ModelForm):
     class Meta:
        model = Mrp_element
        fields = '__all__'
        exclude =['year','week','uploaded_by','uploaded_at','deleted','deleted_by','deleted_on']


class Form_apro(forms.ModelForm):
     class Meta:
        model = Apro_spec
        fields = '__all__'
        exclude =['year','week','uploaded_by','uploaded_at','deleted','deleted_by','deleted_on']

           