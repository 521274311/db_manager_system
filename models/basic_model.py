import pymysql
from config.conn_config import host, port, username, password
from pymysql.cursors import DictCursor

class BasicModel():

    conn = pymysql.connect(host=host, port=port, user=username, password=password, db='db_manager_system_db')

    @classmethod
    def query_all(cls,sql):
        cursor = cls.conn.cursor(DictCursor)
        cursor.execute(sql)
        res = cursor.fetchall()
        cursor.close()
        return res

    @classmethod
    def update(cls, sql):
        cursor = cls.conn.cursor()
        cursor.execute(sql)
        cls.conn.commit()
        cursor.close()
        return True

    @classmethod
    def insert(cls,table_name, json_data):
        if type(json_data) == list:
            model_json_data = json_data[0]
        else:
            model_json_data = json_data
        cols = ','.join((f'`{t}`' for t in model_json_data.keys()))
        val_cols = ','.join(f'%({t})s' for t in model_json_data.keys())
        sql = f'insert into {table_name}({cols}) values ({val_cols})'
        cursor = cls.conn.cursor()
        if type(json_data) == list:
            cursor.executemany(sql, json_data)
        else:
            cursor.execute(sql, json_data)
        cls.conn.commit()
        cursor.close()
        return True
