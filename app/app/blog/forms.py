from wtforms import Form, StringField, validators

class CreateOrUpdateBlogForm(Form):
    title = StringField('title', [validators.required()])
    content = StringField('content', [validators.required()])
