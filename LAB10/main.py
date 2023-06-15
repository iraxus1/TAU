import mysql.connector

# Połączenie z bazą danych
cnx = mysql.connector.connect(
    host='localhost',
    user='username',
    password='password',
    database='database'
)

# Utworzenie tabeli (jeśli nie istnieje)
cursor = cnx.cursor()
create_table_query = """
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL
    )
"""
cursor.execute(create_table_query)
cnx.commit()
# Zamknięcie połączenia
cursor.close()
cnx.close()
