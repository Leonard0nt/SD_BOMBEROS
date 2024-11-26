from django import forms
from django.core.exceptions import ValidationError
from aplicacionAdministrador.models import voluntarios

class VoluntarioEditForm(forms.ModelForm):
    password = forms.CharField(
        label='Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6 border-black'}),
        required=True,
    )
    confirm_password = forms.CharField(
        label='Confirmar Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6 border-black'}),
        required=True,
    )

    class Meta:
        model = voluntarios
        fields = ['nombres', 'apellidos', 'telefono', 'compania', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2, 'class': 'form-control col-md-6 border-black'}),
        }

    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.data.get('confirm_password')

        voluntario = self.instance  # Accede al objeto voluntario asociado al formulario

        # Verifica la contraseña actual antes de realizar la validación
        if not voluntario.check_password(password):
            raise ValidationError("La contraseña actual no es correcta.")

        # Realiza la validación de coincidencia de contraseñas
        if password and password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden. Vuelve a intentarlo.")

        return password
    
    def save(self, commit=True):
        voluntario = super().save(commit=False)

        if commit:
            voluntario.save()

        return voluntario

