from app.routes.utils import *
from app.models.Subject import Subject


bp = Blueprint('subject', __name__)


@bp.route('/subjects/<id>', methods=['GET'])
def get_subject_by_id(id):
    subject = Subject.objects.get_or_404(id=id)

    return jsonify(subject), 201


@bp.route('/subjects/<name>', methods=['GET'])
def get_subject_by_name(name):
    subject = Subject.objects.get_or_404(name=name)

    return jsonify(subject), 201


@bp.route('/subjects', methods=['POST'])
def create_subject():
    body = request.get_json()

    subject = Subject.objects.create(**body)

    return jsonify(subject), 201


@bp.route('/subjects', methods=['DELETE'])
def delete_subject(id):
    subject = Subject.objects.get_or_404(id=id)
    subject.delete()

    return jsonify(str(subject.id)), 200


@bp.route('/subject/<id>/students', methods=['POST'])
def append_students_to_subject():
    student = request.get_json()

    subject = Subject.objects.get_or_404(id=id)

    subject.subjects.append(**student)

    return jsonify(subject), 201


@bp.route('/subject/<id>', methods=['PATCH'])
@jwt_required()
def update_subject():
    body = request.get_json()

    subject = Subject.objects.get_or_404(id=id)
    subject.update(**body)

    return jsonify(subject), 200
