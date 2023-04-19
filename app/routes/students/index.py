from app.routes.utils import *
from app.models.Student import Student

bp = Blueprint('students', __name__)


@bp.route('/students', methods=['POST'])
def create_student():
    body = request.get_json()

    student = Student.objects.create(**body)

    return jsonify(student), 201


@bp.route('/students', methods=['PUT', 'PATCH'])
@jwt_required()
def update_student():
    body = request.get_json()
    body['updated_at'] = datetime.utcnow

    current_user = get_jwt_identity()

    student = Student.objects.get_or_404(email=current_user)
    student.update(**body)

    return jsonify({
        "message": "Successfully, you have changed information pertaining to your account.",
        "user": student
    }), 201


@bp.route('/students', methods=['DELETE'])
@jwt_required()
def delete_current_student():
    current_user = get_jwt_identity()

    student = Student.objects.get_or_404(email=current_user)
    student.delete()

    return jsonify(str(student.id)), 200


@bp.route('/students/<id>', methods=['DELETE'])
def delete_student_by_id(id):
    student = Student.objects.get_or_404(id=id)
    student.delete()

    return jsonify(str(student.id)), 200


@bp.route('/students', methods=['GET'])
@jwt_required()
def get_current_student():
    current_student = get_jwt_identity()

    student = Student.objects.get_or_404(email=current_student)

    return jsonify(student), 200


@bp.route('/students/<id>', methods=['GET'])
def get_student_by_id(id):
    student = Student.objects.get_or_404(id=id)

    return jsonify(student), 201
