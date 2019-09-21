from models.user_model import UserModel
class UserService():
    @staticmethod
    def get_user_list(user_info):
        if user_info['power_id'] == 1:
            return UserModel.get_user_list(user_info['group_id'])
        else:
            return UserModel.get_user_list()

    @classmethod
    def get_user_info_by_id(cls, id):
        return UserModel.get_user_info_by_id(id)

    @classmethod
    def update_stat_by_id(cls, id, type='update'):
        if type == 'update':
            new_user_stat = 3 - UserModel.get_user_info_by_id(id)['stat']
            return UserModel.update_user_stat_by_id(id, new_user_stat)
        else:
            return UserModel.update_user_stat_by_id(id, 3)
