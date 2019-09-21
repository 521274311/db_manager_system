from config.conn_config import prefix
from models.basic_model import BasicModel

class UserModel():
    prefix = prefix
    @classmethod
    def get_user_list(cls, group_id=None):
        sql = ''
        if group_id == None:
            sql = f'select * from {cls.prefix}user_info_tbl where stat<3 order by id'
        else:
            sql = f'select * from {cls.prefix}user_info_tbl where stat<3 and group_id={group_id} order by id'
        return BasicModel.query_all(sql)

    @classmethod
    def get_user_info_by_id(cls, id):
        sql = f'select * from {cls.prefix}user_info_tbl where id={id}'
        return BasicModel.query_all(sql)[0]

    @classmethod
    def update_user_stat_by_id(cls, id, stat):
        sql = f'update {cls.prefix}user_info_tbl set stat={stat} where id={id}'
        return BasicModel.update(sql)

if __name__ == '__main__':
    print(UserModel.update_user_stat_by_id(1, 2))