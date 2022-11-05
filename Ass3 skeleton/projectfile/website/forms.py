
from flask_wtf import FlaskForm
from wtforms.fields import (
    TextAreaField, SubmitField, StringField, PasswordField,
    DateField, SelectField, DateTimeField, RadioField,
    IntegerField, DecimalField, TimeField, BooleanField, DateTimeLocalField
)

from wtforms.validators import (
    InputRequired, Length, Email, EqualTo, Regexp, Optional, NumberRange)
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.widgets import TextArea


#creates the login information
class LoginForm(FlaskForm):
    user_name = StringField("Username", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

 # this is the registration form
class RegisterForm(FlaskForm):
    user_name=StringField("User Name", validators=[InputRequired()])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email")])
    #linking two fields - password should be equal to data entered in confirm
    password=PasswordField("Password", validators=[InputRequired(),
                  EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    dob = DateField("Date of Birth", validators=[Optional()])


    #submit button
    submit = SubmitField("Register")

ALLOWED_IMAGE = {'PNG', 'JPG', 'png', 'jpg', 'avif'}


class CreateEventForm(FlaskForm):
    eventname = StringField('Event Name', validators=[InputRequired()])

    # startDate = DateTimeLocalField("Date of Event", format='%m/%d/%y', validators=[InputRequired()])
    startDate = StringField("Date of Event", validators=[InputRequired()])
    

    # endDate = DateTimeLocalField("End date of Event", format='%m/%d/%y', validators=[Optional()])
    endDate = StringField("End date of Event", validators=[Optional()])

    info = TextAreaField('Event Information', widget=TextArea(), validators=[Length(min=10), InputRequired()])
    venue = StringField("Venue", validators=[InputRequired()])



    # status = RadioField('Event Status',
    #                     choices=['UPCOMING', 'SOLD_OUT', 'CANCELLED'], default='UPCOMING')
    status = StringField('Event Status', validators=[InputRequired()])
    price = IntegerField('Price per Ticket', validators=[InputRequired(), NumberRange(min=0, message="Ticket Price must be equal or greater than 0")])
    tickets = IntegerField('Available Tickets', validators=[InputRequired(),
                                                            NumberRange(min=1, message="Ticket Quantity must be greater than 0")])
    artist = StringField('Artist', validators=[InputRequired()])

    image = FileField("Upload Event Image", validators=[FileAllowed(ALLOWED_IMAGE, message='Only supports png, jpg, JPG, PNG, avif')])

    submit = SubmitField("Create")
   
