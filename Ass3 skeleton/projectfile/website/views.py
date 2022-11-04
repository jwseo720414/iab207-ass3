from flask import Blueprint, render_template, redirect, flash, jsonify, request


from .models import Events
from . import db
import json
from flask_login import login_required, current_user
# from . import db

bp = Blueprint('main', __name__)


@bp.route('/')
def index():
    events = Events.query.all()
    return render_template("index.html", title = "Home", events=events)


@bp.route('/event/<int:event_id>/')
def Event_details(event_id):
    event = Events.query.get_or_404(event_id)
    return render_template("detailPage.html", event=event, user=current_user)



    # , tag_line=tag_line,
    #                 form=form, hotels=hotels