from django.forms import ModelForm, forms
from registration.models import Users


class UsersForm(ModelForm):
    class Meta:
        model = Users
        fields = ['username', 'email']

    def clean_email(self):
        email = self.cleaned_data['email']

        """
        If email exists, raise error. If not error, make the success message as
        an error so that either way the modal is shown after submitting
        the form('templates/info.html').
        """
        if Users.objects.filter(email=email).exists():
            raise forms.ValidationError(f'The email {email} is already enrolled. Please try another one!')  # noqa

        return email

    def clean_username(self):
        username = self.cleaned_data['username'].split()[0]
        username = username.capitalize()  # Capitalize the name
        return username
