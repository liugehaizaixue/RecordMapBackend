""" 
该文件将负责定义标记相关的服务代码
"""
from database import Session, Marker
from werkzeug.exceptions import BadRequest

class MarkerService:
    # 查询全部标记点
    def get_markers(self):
        with Session() as session:
            markers = session.query(Marker).all()
            return {'result': True, 'data': [marker.to_dict() for marker in markers]}
    
    # 添加新的Marker点
    def create_marker(self, data):
        # 判断必需的字段是否都存在
        if not all(key in data for key in ('latitude', 'longitude')):
            raise BadRequest('Missing required data')

        marker = Marker(
            content=data.get('content',""),
            name=data.get('name',""),
            latitude=data.get('latitude'),
            longitude=data.get('longitude'),
            star=data.get('star', 0),
            kind=data.get('kind', 'want')
        )

        with Session() as session:
            try:
                session.add(marker)
                session.commit()
                return {'result': True, 'data': marker.to_dict_with_id()}  # 添加成功

            except Exception as e:
                session.rollback()  # 出现异常时回滚事务
                return {'result': False, 'data': {'error': str(e)}}  # 添加失败，返回错误原因
            
    # 根据id查询某个marker点
    def get_marker(self, id):
        with Session() as session:
            marker = session.query(Marker).get(id)

            if marker:
                return {'result': True, 'data': marker.to_dict()}
            else:
                return {'result': False, 'data': {'error': 'Marker not found'}}

    def update_marker(self, id, data):
        # 判断必需的字段是否都存在
        if not all(key in data for key in ('latitude', 'longitude')):
            raise BadRequest('Missing required data')
        
        with Session() as session:
            marker = session.query(Marker).get(id)

            if marker:
                marker.content = data.get('content', marker.content)
                marker.name = data.get('name', marker.name)
                marker.latitude = data.get('latitude', marker.latitude)
                marker.longitude = data.get('longitude', marker.longitude)
                marker.star = data.get('star', marker.star)
                marker.kind = data.get('kind', marker.kind)
                try:
                    session.commit()
                    return {'result': True, 'data':{}}
                except Exception as e:
                    session.rollback()
                    print(f"Error committing changes: {e}")
                    return {'result': False, 'data': {'error': str(e)}}
            else:
                return {'result': False, 'data': {'error': 'Marker not found'}}

    # 根据id删除某个marker点 
    def delete_marker(self, id):
        with Session() as session:
            try:
                marker = session.query(Marker).get(id)
                if marker:
                    session.delete(marker)
                    session.commit()

                    return {'result': True, 'data': {}}
                else:
                    return {'result': False, 'data': {'error': 'Marker not found'}}
            except Exception as e:
                session.rollback()
                return {'result': False, 'data': {'error': 'Failed to delete marker: {}'.format(str(e))}}