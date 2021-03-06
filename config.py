import os

from flask_appbuilder.const import AUTH_DB

basedir = os.path.abspath(os.path.dirname(__file__))

# NOTE: Set the following secret config parameters in a local .env file:
# FLASK_SECRET_KEY created using secrets.token_urlsafe()
# FLASK_SQLALCHEMY_DATABASE_URI
# FLASK_RECAPTCHA_PUBLIC_KEY
# FLASK_RECAPTCHA_PRIVATE_KEY
# FLASK_MAIL_SERVER
# FLASK_MAIL_PORT
# FLASK_MAIL_USE_TLS
# FLASK_MAIL_USERNAME
# FLASK_MAIL_PASSWORD
# FLASK_MAIL_DEFAULT_SENDER

CSRF_ENABLED = True
SQLALCHEMY_POOL_RECYCLE = 3
SQLALCHEMY_TRACK_MODIFICATIONS = False

BABEL_DEFAULT_LOCALE = "de"
BABEL_DEFAULT_FOLDER = "translations"
LANGUAGES = {
    "de": {"flag": "at", "name": "German"},
}

FAB_API_MAX_PAGE_SIZE = 100
FAB_PASSWORD_COMPLEXITY_ENABLED = False

FAB_ROLES = {
    "Student": [
        ["Question.*", "can_list"],
        ["AssignmentModelStudentView", "can_list"],
        ["AssignmentModelStudentView", "can_show"],
        ["CategoryModelStudentView", "can_list"],
        ["CategoryModelStudentView", "can_show"],
        ["questions_.*", "menu_access"],
        ["random_.*", "menu_access"],
        ["topics", "menu_access"],
        ["assignments_student", "menu_access"],
        [".*", "can_get"],
        [".*", "can_info"],
        [".*", "can_this_form_get"],
        [".*", "can_this_form_post"],
        [".*", "can_userinfo"],
        [".*", "userinfoedit"],
        [".*", "resetmypassword"],
        ["QuestionRandom", "can_question_random"],
        ["IdToForm", "can_id_to_form"]
    ],
    "Teacher": [
        [".*", "can_list"],
        [".*", "can_show"],
        [".*", "menu_access"],
        [".*", "can_get"],
        [".*", "can_info"],
        [".*", "can_this_form_get"],
        [".*", "can_this_form_post"],
        [".*", "can_userinfo"],
        [".*", "userinfoedit"],
        [".*", "resetmypassword"],
        ["AssignmentModelStudentView", "can_edit"],
        ["AssignmentModelStudentView", "can_add"],
        ["QuestionRandom", "can_question_random"],
        ["IdToForm", "can_id_to_form"]
    ]
}

# ------------------------------
# GLOBALS FOR GENERAL APP's
# ------------------------------
UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_FOLDER = basedir + "/app/static/uploads/"
IMG_UPLOAD_URL = "/static/uploads/"
AUTH_TYPE = AUTH_DB
AUTH_USER_REGISTRATION = True
AUTH_USER_REGISTRATION_ROLE = 'Student'

AUTH_ROLE_ADMIN = "Admin"
AUTH_ROLE_PUBLIC = "Public"
APP_NAME = "Mathe ??ben"
APP_THEME = ""
FAB_SECURITY_MANAGER_CLASS = 'app.security.general.ExtendedSecurityManager'
FAB_BASE_TEMPLATE = 'extended_base.html'
FAB_INDEX_VIEW = 'app.views.index.ExtendedIndexView'
