from app.models.Teacher import Teacher
from app.routes.utils import *


bp = Blueprint('teachers', __name__)


@bp.route('/teachers', methods=['POST'])
def create_teacher():
    body = request.get_json()

    teacher = Teacher.objects.create(
        name=body['name'],
        username=body['username'],
        email=body['email'],
        password=body['password']
    )

    return jsonify(teacher), 201


@bp.route('/teachers', methods=['GET'])
@jwt_required()
def get_teacher():
    current_user = get_jwt_identity()
    teacher = Teacher.objects.get_or_404(email=current_user)

    return jsonify(teacher), 200


@bp.route('/teachers/<id>', methods=['GET'])
def get_teacher_by_id(id: str):
    teacher = Teacher.objects.get_or_404(id=id)

    return jsonify(teacher), 200


@bp.route('/teachers', methods=['PUT'])
@jwt_required()
def update_teacher():
    body = request.get_json()
    body['updated_at'] = datetime.utcnow

    current_user = get_jwt_identity()

    teacher = Teacher.objects.get_or_404(email=current_user)
    teacher.update(**body)

    return jsonify({
        "message": "Successfully, you have changed information pertaining to your account.",
        "user": teacher
    }), 201


@bp.route('/teachers/<id>', methods=['DELETE'])
@jwt_required()
def delete_teacher(id: str):
    teacher = Teacher.objects.get_or_404(id=id)
    teacher.delete()

    return jsonify(str(teacher.id)), 200


@bp.route('/login/teachers', methods=["POST"])
def login_teacher():
    try:
        data = request.json
    except:
        return jsonify({
            "message": "Please provide user details",
            "data": None,
            "error": "Bad request"
        }), 400

    valid_user = Teacher.objects(
        email=data['email'], password=data['password']).first()

    if valid_user is None:
        return jsonify({
            "message": "Error fetching auth token!, invalid email or password",
            "data": None,
            "error": "Unauthorized"
        }), 404

    try:
        access_token = create_access_token(identity=valid_user['email'])

        user = {
            'id': str(valid_user['id']),
            'name': valid_user['name'],
            'username': valid_user['username'],
            'email': valid_user['email'],
            'subject': valid_user['subject']
        }

        return jsonify({
            "message": "Successfully fetched auth token. You are logged in.",
            "token": access_token,
            "user": user
        })
    except Exception as e:
        return jsonify({
            "error": "Something went wrong",
            "message": str(e)
        }), 500
