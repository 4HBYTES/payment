from wtforms import Form, StringField, validators


class CreateOrUpdatePageForm(Form):
    title = StringField('title', [validators.required()])
    content = StringField('content', [validators.required()])
