""" 
该文件将负责定义标记相关的路由处理函数并调用 MarkerService
"""

from flask import Blueprint, request, jsonify
from services.marker_service import MarkerService

marker_controller = Blueprint('marker_controller', __name__)
marker_service = MarkerService()

@marker_controller.route('/marker', methods=['GET'])
def get_markers():
    markers = marker_service.get_markers()
    return jsonify(markers)

@marker_controller.route('/marker', methods=['POST'])
def create_marker():
    data = request.get_json()
    marker = marker_service.create_marker(data)
    print(marker)
    return jsonify(marker)

@marker_controller.route('/marker/<int:id>', methods=['GET'])
def get_marker(id):
    marker = marker_service.get_marker(id)
    return jsonify(marker)

@marker_controller.route('/marker/<int:id>', methods=['PUT'])
def update_marker(id):
    data = request.get_json()
    marker = marker_service.update_marker(id, data)
    return jsonify(marker)

@marker_controller.route('/marker/<int:id>', methods=['DELETE'])
def delete_marker(id):
    result = marker_service.delete_marker(id)
    return jsonify(result)
