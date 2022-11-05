from flask import Blueprint, render_template, redirect, flash, jsonify, request, url_for


from .models import Events
# Ticketing, Comment
from . import db
import json
from flask_login import login_required, current_user

from .forms import  CreateEventForm
# BookingForm, CommentForm, EditEventForm
from datetime import datetime
from .functions import check_upload_file


bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = Events.query.all()
    return render_template("index.html", title = "Home", events=events)


@bp.route('/event/<int:event_id>/')
def Event_details(event_id):
    event = Events.query.get_or_404(event_id)
    return render_template("detailPage.html", event=event, user=current_user)

@bp.route('/search')
def search():
    if request.args['search']:
        print(request.args['search'])
        dest = "%" + request.args['search'] + '%'
        events = Events.query.filter(Events.name.like(dest)).all()
        return render_template('index.html', events=events, title='Home')
    else:
        return redirect(url_for('main.index'))

@bp.route('/createevent', methods=['GET', 'POST'])
@login_required
def createevent():
    form = CreateEventForm()

    if (form.validate_on_submit() == True):
        print("Event form has been submitted")
        event = Events(
            name=form.eventname.data, 
            startDate=form.startDate.data,
            endDate=form.endDate.data,
            description=form.info.data,
            location=form.venue.data,
            status=form.status.data,
            price=form.price.data,
            ticketNum=form.tickets.data,
            author=form.artist.data,
            image=check_upload_file(form.image.data)
            )
# user_id=current_user.id

        # db.session.rollback()
        db.session.add(event)
        db.session.commit()
        # db.session.flush()

        return redirect(url_for('main.index'))

    return render_template('/eventCreation.html', form=form, title="Create Event")
