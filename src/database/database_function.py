from src.database.connection import databaseConnection

def exec(sql_query, values):
    result = []
    connection = databaseConnection()
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query, values)
            result.append(cursor.fetchall())
            connection.commit()
            return result   
    finally:    
        connection.close()
        return result
    
    