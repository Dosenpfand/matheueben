import logging

from flask import url_for, g
from markupsafe import Markup
from sqlalchemy import func

from app import db
from app.models.general import Question, Topic, QuestionUserState


def link_formatter(external_id, filters=None):
    assignment_id = None
    if filters:
        assignment_id = filters.get_filter_value('assignments')

    url = url_for(f'ExtIdToForm.ext_id_to_form', ext_id=external_id, assignment_id=assignment_id)
    return Markup(f'<a href="{url}">{external_id}</a>')


# TODO: should be in jinja and imported!
def state_to_emoji_markup(state, filters=None):
    if state is QuestionUserState.solved_success:
        emoji = 'bi-emoji-sunglasses'
        label = 'label-success'
        title = 'Richtig gelöst'
    elif state is QuestionUserState.tried_failed:
        emoji = 'bi-emoji-frown'
        label = 'label-danger'
        title = 'Falsch gelöst'
    else:
        emoji = 'bi-emoji-neutral'
        label = 'label-warning'
        title = 'Kein Versuch'
    return Markup(f'<span class="label {label}" title="{title}"><i class="bi {emoji}"></i></span>')


def get_question(question_type, ext_id=None):
    if ext_id:
        result = db.session.query(Question).filter_by(
            external_id=ext_id, type=question_type).first()
    else:
        active_topic_ids = get_active_topics()
        filter_arg = Question.topic_id.in_(active_topic_ids)
        result = db.session.query(Question).order_by(
            func.random()).filter(filter_arg).filter_by(type=question_type).first()

    return result


def get_question_count(type):
    active_topic_ids = get_active_topics()
    filter_arg = Question.topic_id.in_(active_topic_ids)
    count = db.session.query(Question).order_by(
        func.random()).filter(filter_arg).filter_by(type=type).count()
    return count


def get_active_topics():
    topic_ids = [topic.id for topic in g.user.active_topics]

    # If no topic IDs set for this user
    if not topic_ids:
        # Set all topic IDs
        results = db.session.query(Topic).all()
        topic_ids = [result.id for result in results]

    return topic_ids


def safe_math_eval(string):
    allowed_chars = "0123456789+-*(). /"
    if string == '':
        return ''

    for char in string:
        if char not in allowed_chars:
            return ''
    return eval(string)


def commit_safely(db_session):
    try:
        db_session.commit()
    except Exception as e:
        db_session.rollback()
        logging.warning(e, exc_info=True)
