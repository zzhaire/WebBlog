from django import forms


class RegisterForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={"required": "请填写邮箱", 'invalid': "请填写有效的邮箱"}
    )
    password = forms.CharField(
        required=True,
        error_messages={"required": "请填写密码"}
    )
    nick_name = forms.CharField(
        required=True, error_messages={"required": "请填写名字"}
    )


class UserLoginForm(forms.Form):
    email = forms.EmailField(
        required=True,
        error_messages={"required": "请填写邮箱", 'invalid': "请填写有效的邮箱"}
    )
    password = forms.CharField(
        required=True,
        error_messages={"required": "请填写密码"}
    )
