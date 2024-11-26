from django import forms
from django.core.exceptions import ValidationError
from aplicacionAdministrador.models import voluntarios



class ContrasenaEditForm(forms.ModelForm):
    actual_password = forms.CharField(
        label='Contraseña actual',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6 border-black'}),
        required=True,
    )
    new_password = forms.CharField(
        label='Nueva Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6 border-black'}),
        required=True,
    )
    confirm_password = forms.CharField(
        label='Confirmar Nueva Contraseña',
        widget=forms.PasswordInput(attrs={'class': 'form-control col-6 border-black'}),
        required=True,
    )

    class Meta:
        model = voluntarios
        fields = []


    def clean_actual_password(self):
        actual_password = self.cleaned_data.get('actual_password')

        voluntario = self.instance  # Accede al objeto voluntario asociado al formulario

        # Verifica la contraseña actual antes de realizar la validación
        if not voluntario.check_password(actual_password):
            raise ValidationError("La contraseña actual no es correcta.")

        return actual_password

    def clean_confirm_password(self):
        new_password = self.cleaned_data.get('new_password')
        confirm_password = self.cleaned_data.get('confirm_password')

        # Realiza la validación de coincidencia de contraseñas
        if new_password and new_password != confirm_password:
            raise ValidationError("Las contraseñas no coinciden. Vuelve a intentarlo.")

        return confirm_password

    def save(self, commit=True):
        voluntario = super().save(commit=False)

        # Accede a la nueva contraseña del método clean_confirm_password
        nueva_contraseña = self.cleaned_data.get('confirm_password')

        # Establece la nueva contraseña en el objeto voluntario
        voluntario.set_password(nueva_contraseña)

        if commit:
            voluntario.save()

        return voluntario

        