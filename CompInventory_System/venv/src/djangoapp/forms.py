from django import forms
from .models import Computer

class ComputerForm(forms.ModelForm):
    class Meta:
        model=Computer
        fields=['computer_name','IP_address', 'MAC_address','operating_system','users_name', 'location', 'purchase_date']

    def clean_computer_name(self): # Validates the Computer Name Field<br>
            computer_name = self.cleaned_data.get('computer_name')
            if (computer_name == ""):
                raise forms.ValidationError('This field cannot be left blank')
            for instance in Computer.objects.all():
                if instance.computer_name==computer_name:
                    raise forms.ValidationError('There is a computer with the name ' + computer_name)
            return computer_name

    def clean_IP_address(self): # Validates the Computer Name Field<br>
            IP_address = self.cleaned_data.get('IP_address')
            if (IP_address == ""):
                raise forms.ValidationError('This field cannot be left blank')
            for instance in Computer.objects.all():
                if instance.IP_address==IP_address:
                    raise forms.ValidationError('There is a computer with the IP_address ' + IP_address)
            return IP_address

class ComputerEditForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields=['computer_name','IP_address', 'MAC_address','operating_system','users_name', 'location', 'purchase_date']

class ComputerSearchForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields = ['computer_name', 'users_name' ,'export_to_CSV']
