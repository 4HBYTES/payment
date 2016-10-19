from wtforms import Form, StringField, ValidationError
from auth import app


class HealthForm(Form):
    token = StringField('token')

    def validate_token(form, field):
        if field.data != app.config['APP_TOKEN']:
            raise ValidationError('Token is incorrect')
