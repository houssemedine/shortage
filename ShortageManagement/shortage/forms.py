from django import forms
from shortage.models import Core,CoreHistory

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
            'material': forms.TextInput(attrs={

                'hx-trigger': 'keyup',
                'hx-target': '#div_id_material',
               })
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
        
   
        

           