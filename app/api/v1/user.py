from email import message
from flask import Blueprint, request

from app.models import User
from app.utils import send_error, send_result, get_timestamp_now

api = Blueprint('user', __name__)

@api.route('/register/<string:username>', methods=['POST'])
def register(username):
    user = User.find_by_username(username)
    if user:
        return send_error(message="da co r nha")
    data = request.get_json()
    try:
        user = User(**data)
        user.save_data()
    except:
        return send_error(message="something wrong")
    return send_result(data=user.json())

@api.route('/update/<string:username>', methods=['POST'])
def update(username):
    data = request.get_json()
    user = User.find_by_username(username)
    if user:
        for item in data:
            if data['{}'.format(item)] != "": 
                if item == "username" or item == "id":
                    continue
                user.item = data['{}'.format(item)]                     
        user.modified_date = get_timestamp_now()
        user.save_changes()
        return send_result(data=user.json() ,message="da dc sua")
    return send_error(message="khong co trong nay ma sua")

@api.route('/delete/<string:username>', methods=['POST'])
def delete(username):
    user = User.find_by_username(username)
    if not user:
        return send_error(message="khong co")
    try:
        user.delete_data()
    except:
        return send_error(message="something wrong")

    return send_result(message="da xoa thanh cong")

@api.route('/inactive', methods=['GET'])
def inactive():
    user = User.query.filter(User.is_active == 0).all()
    if user:
        return send_result(data=user.json(), message="nhung tai khoan chua active")
    return send_error(message="active het roi")

@api.route('/find_by_id/<string:id>', methods=['GET'])
def find_by_id(id):
    user = User.query.filter_by(id=id).first()
    if user:
        return send_result(data=user.json(), message="day nha")
    return send_error(message="chiu khong co")

@api.route('/get_all', methods=['GET'])
def get_all():
    user = User.query.all()
    if user:
        return send_result(data=user.json(), message="danh sach user")
    return send_error(message="chua co 1 thang nao")

@api.route('/find_like_address/<string:address>', methods=['GET'])
def find_like_address(address):
    search = '%{}%'.format(address)
    user = User.query.filter(User.address.like(search)).all()
    if user:
        return send_result(data=user.json(), message="tim thay roi nay")
    return send_error(message="ko co 1 thang nao luon")

@api.route('/find_like_username/<string:username>', methods=['GET'])
def find_like_address(username):
    search = '%{}%'.format(username)
    user = User.query.filter(User.username.like(search)).all()
    if user:
        return send_result(data=user.json(), message="tim thay roi nay")
    return send_error(message="ko co 1 thang nao luon")

@api.route('/find_like_username', methods=['GET'])
def find_like_address():
    user = User.query.filter(18 <User.age < 40).all()
    if user:
        return send_result(data=user.json(), message="tim thay roi nay")
    return send_error(message="ko co 1 thang nao luon")