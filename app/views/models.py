from flask import g
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.filters import FilterInFunction, FilterEqual, FilterEqualFunction
from flask_appbuilder.models.sqla.interface import SQLAInterface
from wtforms import HiddenField

from app.utils.filters import FilterQuestionByAnsweredCorrectness
from app.models.general import Question, QuestionType, LearningGroup, Assignment, Topic, Category
from app.models.relations import AssocUserQuestion
from app.utils.general import get_active_topics, link_formatter, state_to_emoji_markup
from app.views.widgets import ExtendedListWidget


class Question2of5ModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.two_of_five.value]]
    title = '2 aus 5'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_two_of_five
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.two_of_five.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'title']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class Question1of6ModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.one_of_six.value]]
    title = '1 aus 6'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_one_of_six
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.one_of_six.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'title']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class Question3to3ModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.three_to_three.value]]
    title = 'L??ckentext'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_three_to_three
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.three_to_three.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'title']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class Question2DecimalsModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.two_decimals.value]]
    title = 'Werteingabe zwei Zahlen'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_two_decimals
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.two_decimals.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'title']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class Question1DecimalModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.one_decimal.value]]
    title = 'Werteingabe eine Zahl'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_one_decimal
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.one_decimal.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'title']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class QuestionSelfAssessedModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.self_assessed.value]]
    title = 'Selbstkontrolle'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_self_assessed
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.self_assessed.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'solution_image_img']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class QuestionSelect4ModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics], [
        'type', FilterEqual, QuestionType.select_four.value]]
    title = 'Zuordnung'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    add_columns = Question.cols_select_four
    add_form_extra_fields = {'type': HiddenField(
        default=QuestionType.select_four.value)}
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    show_columns = ['description_image_img', 'solution_image_img']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class QuestionModelView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics]]
    base_order = ('external_id', 'asc')
    title = 'Aufgaben'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie', 'state': 'Status'}
    list_columns = ['id', 'topic', 'state']
    formatters_columns = {'id': link_formatter, 'state': state_to_emoji_markup}
    page_size = 100
    list_widget = ExtendedListWidget


class AssocUserQuestionModelView(ModelView):
    datamodel = SQLAInterface(AssocUserQuestion)
    list_columns = ['user', 'question', 'created_on', 'is_answer_correct']


class LearningGroupModelView(ModelView):
    datamodel = SQLAInterface(LearningGroup)
    list_columns = ['name']


class AssignmentModelAdminView(ModelView):
    datamodel = SQLAInterface(Assignment)
    list_columns = ['name', 'learning_group', 'additional_links']
    label_columns = {'name': 'Titel',
                     'learning_group': 'Klasse',
                     'starts_on': 'Erhalten am',
                     'is_due_on': 'F??llig am',
                     'additional_links': 'Auswertung'}


class AssignmentModelStudentView(ModelView):
    datamodel = SQLAInterface(Assignment)
    base_filters = [['learning_group_id', FilterEqualFunction, lambda: g.user.learning_group_id]]

    label_columns = {'name': 'Titel',
                     'learning_group': 'Klasse',
                     'starts_on': 'Erhalten am',
                     'is_due_on': 'F??llig am'}
    list_columns = ['name', 'starts_on', 'is_due_on']
    show_columns = ['name', 'starts_on', 'is_due_on']
    title = 'Haus??bungen'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title

    related_views = [QuestionModelView]
    show_template = "show_cascade_expanded.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"


class CategoryModelStudentView(ModelView):
    datamodel = SQLAInterface(Category)

    label_columns = {'name': 'Titel'}
    list_columns = ['name']
    show_columns = ['name']
    title = 'Maturaaufgaben'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title

    related_views = [QuestionModelView]
    show_template = "show_cascade_expanded.html"
    edit_template = "appbuilder/general/model/edit_cascade.html"


class QuestionModelIncorrectAnsweredView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics],
                    ['', FilterQuestionByAnsweredCorrectness, False]]
    title = 'Aufgaben (falsch beantwortet)'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class QuestionModelCorrectAnsweredView(ModelView):
    datamodel = SQLAInterface(Question)
    base_filters = [['topic_id', FilterInFunction, get_active_topics],
                    ['', FilterQuestionByAnsweredCorrectness, True]]
    title = 'Aufgaben (richtig beantwortet)'
    list_title = title
    show_title = title
    add_title = title
    edit_title = title
    label_columns = {'description_image': 'Beschreibung',
                     'id': 'Frage Nr.', 'topic': 'Grundkompetenzbereich', 'category': 'Kategorie'}
    list_columns = ['id', 'topic']
    formatters_columns = {'id': link_formatter}
    page_size = 100


class TopicModelView(ModelView):
    datamodel = SQLAInterface(Topic)


class CategoryModelAdminView(ModelView):
    datamodel = SQLAInterface(Category)
