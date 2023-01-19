from flask import Blueprint

student_connector = Blueprint("student_connector", __name__)


@student_connector.route("/home")
@student_connector.route("/")
def student_connector_home():
    return "Student Connector Home"
