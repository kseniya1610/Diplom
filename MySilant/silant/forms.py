from django import forms
from .models import *


class FactoryNumber(forms.Form):
    factory_number = forms.CharField(label='Заводской №', widget=forms.TextInput(attrs={'size': 8}),
                                     max_length=10)


class CreateMachineForm(forms.ModelForm):
    client = forms.ModelChoiceField(
        queryset=CustomUser.objects.filter(groups__name='client').order_by('first_name')
    )

    class Meta:
        model = Machine
        widgets = {'factory_number': forms.Textarea(attrs={'rows': 1}),
                   'engine_number': forms.Textarea(attrs={'rows': 1}),
                   'transmission_number': forms.Textarea(attrs={'rows': 1}),
                   'drive_axle_number': forms.Textarea(attrs={'rows': 1}),
                   'steerable_axle_number': forms.Textarea(attrs={'rows': 1}),
                   'supply_contract': forms.Textarea(attrs={'rows': 1}),
                   'consignee': forms.Textarea(attrs={'rows': 1}),
                   'delivery_address': forms.Textarea(attrs={'rows': 2}),
                   'equipment': forms.Textarea(attrs={'rows': 5}),
                   'date_of_shipment_from_the_factory': forms.NumberInput(attrs={'type': 'date'}),
                   }
        fields = '__all__'


class CreateMaintenancesForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        # exclude = ('service_company',)
        fields = '__all__'
        widgets = {'order': forms.Textarea(attrs={'rows': 1}),
                   'maintenance_date': forms.NumberInput(attrs={'type': 'date'}),
                   'order_date': forms.NumberInput(attrs={'type': 'date'}),
                   'machine': forms.HiddenInput(),
                   'service_company': forms.HiddenInput(),

                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        service_company = kwargs.pop('initial')['service_company']
        self.fields['service_company'].initial = service_company


class UpdateMaintenancesForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'
        widgets = {'order': forms.Textarea(attrs={'rows': 1}),
                   'maintenance_date': forms.NumberInput(attrs={'type': 'date'}),
                   'order_date': forms.NumberInput(attrs={'type': 'date'}),
                   'machine': forms.HiddenInput(),
                   # 'service_company': forms.widgets.Select(attrs={'disabled': 'disabled'})
                   'service_company': forms.HiddenInput()
                   }


class CreateReclamationsForm(forms.ModelForm):
    class Meta:
        model = Reclamations
        fields = '__all__'
        widgets = {'date_of_refusal': forms.NumberInput(attrs={'type': 'date'}),
                   'failure_node': forms.Textarea(attrs={'rows': 1}),
                   'parts_used': forms.Textarea(attrs={'rows': 1}),
                   'date_of_restoration': forms.NumberInput(attrs={'type': 'date'}),
                   'equipment_downtime': forms.Textarea(attrs={'rows': 1}),
                   'machine': forms.HiddenInput(),
                   'service_company': forms.HiddenInput(),
                   }

    def __init__(self, *args, **kwargs):
        super(CreateReclamationsForm, self).__init__(*args, **kwargs)
        self.fields['service_company'].help_text = 'Назначить или изменить организацию для данной машины может менеджер в информации о машине'


class UpdateReclamationsForm(forms.ModelForm):
    class Meta:
        model = Reclamations
        fields = '__all__'
        widgets = {'date_of_refusal': forms.NumberInput(attrs={'type': 'date'}),
                   'failure_node': forms.Textarea(attrs={'rows': 1}),
                   'parts_used': forms.Textarea(attrs={'rows': 1}),
                   'date_of_restoration': forms.NumberInput(attrs={'type': 'date'}),
                   'equipment_downtime': forms.Textarea(attrs={'rows': 1}),
                   'machine': forms.HiddenInput(),
                   'service_company': forms.HiddenInput()
                   }


class UpdateTechniqueModelForm(forms.ModelForm):
    class Meta:
        model = TechniqueModel
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateEngineModelForm(forms.ModelForm):
    class Meta:
        model = EngineModel
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateTransmissionModelForm(forms.ModelForm):
    class Meta:
        model = TransmissionModel
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateDriveAxleModelForm(forms.ModelForm):
    class Meta:
        model = DriveAxleModel
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateSteerableAxleModelForm(forms.ModelForm):
    class Meta:
        model = SteerableAxleModel
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class CreateServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateServiceCompanyForm(forms.ModelForm):
    class Meta:
        model = ServiceCompany
        fields = '__all__'
        # exclude = ('user',)
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), 'user': forms.HiddenInput(), }


class UpdateTypeMaintenanceForm(forms.ModelForm):
    class Meta:
        model = TypeMaintenance
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateDescriptionFailureForm(forms.ModelForm):
    class Meta:
        model = DescriptionFailure
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }


class UpdateRecoveryMethodForm(forms.ModelForm):
    class Meta:
        model = RecoveryMethod
        fields = '__all__'
        widgets = {'name': forms.Textarea(attrs={'rows': 1}), }
