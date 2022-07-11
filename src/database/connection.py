from pymysql import connect

def databaseConnection():
    connection = connect(
        host='127.0.0.1',
        user='root',
        password='Basket@4433',
        database='my_tower'
    )
    
    return connection