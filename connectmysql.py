import pymysql

import pymysql
import connectmysql as con

# อันไหนใช้บ่อยให้แยกไว้
# สร้างฟังก์ชั่นสำหรับเชื่อมDB mysql


# def connectdb():
#     connectdb = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='',
#         db='pythondb',
#         port=3306,
#         cursorclass=pymysql.cursors.DictCursor,
#         charset='utf8'
#     )
#     return connectdb


# call function
# print(connectdb())

def connectdb():
    connectdb = pymysql.connect(
        host='bhkc05crhs7zigzyxwkt-mysql.services.clever-cloud.com',
        user='u7pnpbjt231tuuwn',
        password='wWtprfw7u8RxkekYkM1F',
        db='bhkc05crhs7zigzyxwkt',
        port=3306,
        cursorclass=pymysql.cursors.DictCursor,
        charset='utf8'
    )
    return connectdb
