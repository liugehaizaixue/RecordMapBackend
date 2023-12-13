""" 
该文件将负责定义标记相关的路由处理函数并调用 userService
"""

from flask import Blueprint, request, jsonify
from services.user_service import UserService

user_controller = Blueprint('user_controller', __name__)
user_service = UserService()

@user_controller.route('/user_login', methods=['POST'])
def login():
    data = request.get_json()
    users = user_service.login(data)
    print(users)
    return jsonify(users)


