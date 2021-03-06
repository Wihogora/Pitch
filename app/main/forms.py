from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PostForm(FlaskForm):
    title = StringField('Title', validators=[Required()])
    text = TextAreaField('Text', validators=[Required()])
    submit = SubmitField('Submit', validators=[Required()])

# class UpdateProfile(FlaskForm):
#     bio = TextAreaField('Your Bio.',validators = [Required()])
#     submit = SubmitField('Submit')

class CommentForm(FlaskForm):
    text = TextAreaField('Leave a comment:', validators=[Required()])
    submit = SubmitField('Submit')