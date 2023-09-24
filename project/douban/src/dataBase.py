# 导入PyMySQL模块
import pymysql

options = {
    'host': "localhost",
    'user': 'root',
    'password': '123456',
    'database': 'douban',
    'charset': 'utf8'
}


class MyDB:

    def __init__(self):
        self.conn = None
        self.cursor = None

    def link(self):
        try:
            self.conn = pymysql.connect(**options)
            self.cursor = self.conn.cursor()
            print('数据库链接成功')
        except Exception:
            print('数据库链接失败')
            exit()

    def query(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 获取查询结果
            return self.cursor.fetchall()
        except Exception:
            print('查询失败')
            return False

    def push(self, sql):
        try:
            # 执行SQL语句
            self.cursor.execute(sql)
            # 提交
            self.conn.commit()
            return True
        except Exception:
            print('提交失败')
            return False

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
        print("数据库链接关闭")
