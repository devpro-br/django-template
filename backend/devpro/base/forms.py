# from django import forms
# from django.contrib.auth.forms import ReadOnlyPasswordHashField
# from django.utils.translation import gettext_lazy as _
#
# from devpro.base.models import User
#
#
# class UserChangeForm(forms.ModelForm):
#     password = ReadOnlyPasswordHashField(
#         label=_("Password"),
#         help_text=_(
#             "Raw passwords are not stored, so there is no way to see this "
#             "user’s password, but you can change the password using "
#             '<a href="{}">this form</a>.'
#         ),
#     )
#
#     class Meta:
#         model = User
#         fields = "__all__"
#         field_classes = {"username": UsernameField}
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         password = self.fields.get("password")
#         if password:
#             password.help_text = password.help_text.format(
#                 f"../../{self.instance.pk}/password/"
#             )
#         user_permissions = self.fields.get("user_permissions")
#         if user_permissions:
#             user_permissions.queryset = user_permissions.queryset.select_related(
#                 "content_type"
#             )
#
# class UserCreationForm(BaseUserCreationForm):
#     def clean_username(self):
#         """Reject usernames that differ only in case."""
#         username = self.cleaned_data.get("username")
#         if (
#             username
#             and self._meta.model.objects.filter(username__iexact=username).exists()
#         ):
#             self._update_errors(
#                 ValidationError(
#                     {
#                         "username": self.instance.unique_error_message(
#                             self._meta.model, ["username"]
#                         )
#                     }
#                 )
#             )
#         else:
#             return username
#
# class AdminPasswordChangeForm(forms.Form):
#     """
#     A form used to change the password of a user in the admin interface.
#     """
#
#     error_messages = {
#         "password_mismatch": _("The two password fields didn’t match."),
#     }
#     required_css_class = "required"
#     password1 = forms.CharField(
#         label=_("Password"),
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "new-password", "autofocus": True}
#         ),
#         strip=False,
#         help_text=password_validation.password_validators_help_text_html(),
#     )
#     password2 = forms.CharField(
#         label=_("Password (again)"),
#         widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
#         strip=False,
#         help_text=_("Enter the same password as before, for verification."),
#     )
#
#     def __init__(self, user, *args, **kwargs):
#         self.user = user
#         super().__init__(*args, **kwargs)
#
#     def clean_password2(self):
#         password1 = self.cleaned_data.get("password1")
#         password2 = self.cleaned_data.get("password2")
#         if password1 and password2 and password1 != password2:
#             raise ValidationError(
#                 self.error_messages["password_mismatch"],
#                 code="password_mismatch",
#             )
#         password_validation.validate_password(password2, self.user)
#         return password2
#
#     def save(self, commit=True):
#         """Save the new password."""
#         password = self.cleaned_data["password1"]
#         self.user.set_password(password)
#         if commit:
#             self.user.save()
#         return self.user
#
#     @property
#     def changed_data(self):
#         data = super().changed_data
#         for name in self.fields:
#             if name not in data:
#                 return []
#         return ["password"]
#
