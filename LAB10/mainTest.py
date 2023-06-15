import mysql.connector
import unittest

class DatabaseTestCase(unittest.TestCase):
    def setUp(self):
        # Połączenie z bazą danych
        self.cnx = mysql.connector.connect(
            host='localhost',
            user='username',
            password='password',
            database='database'
        )
        
        # Utworzenie tabeli (jeśli nie istnieje)
        self.cursor = self.cnx.cursor()
        create_table_query = """
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL
            )
        """
        self.cursor.execute(create_table_query)
        self.cnx.commit()

    def tearDown(self):
        # Usunięcie tabeli
        drop_table_query = "DROP TABLE IF EXISTS users"
        self.cursor.execute(drop_table_query)
        self.cnx.commit()
        
        # Zamknięcie połączenia
        self.cursor.close()
        self.cnx.close()

    def test_create_user(self):
        # Test 1: Dodanie użytkownika do bazy danych
        add_user_query = """
            INSERT INTO users (name, email) VALUES (%s, %s)
        """
        user_data = ('John Doe', 'john@example.com')
        self.cursor.execute(add_user_query, user_data)
        self.cnx.commit()
        
        # Sprawdzenie, czy użytkownik został pomyślnie dodany
        select_user_query = """
            SELECT * FROM users WHERE name = %s AND email = %s
        """
        self.cursor.execute(select_user_query, user_data)
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'John Doe')
        self.assertEqual(user[2], 'john@example.com')

        # Test 2: Dodanie innego użytkownika do bazy danych
        user_data2 = ('Jane Smith', 'jane@example.com')
        self.cursor.execute(add_user_query, user_data2)
        self.cnx.commit()
        
        # Sprawdzenie, czy użytkownik został pomyślnie dodany
        self.cursor.execute(select_user_query, user_data2)
        user2 = self.cursor.fetchone()
        self.assertIsNotNone(user2)
        self.assertEqual(user2[1], 'Jane Smith')
        self.assertEqual(user2[2], 'jane@example.com')

    def test_read_users(self):
        add_user_query = """
            INSERT INTO users (name, email) VALUES (%s, %s)
        """
        users_data = [
            ('John Doe', 'john@example.com'),
            ('Jane Smith', 'jane@example.com')
        ]
        for user_data in users_data:
            self.cursor.execute(add_user_query, user_data)
        self.cnx.commit()

        # Pobranie wszystkich użytkowników
        select_users_query = """
            SELECT * FROM users
        """
        self.cursor.execute(select_users_query)
        users = self.cursor.fetchall()
        
        # Sprawdzenie, czy liczba pobranych użytkowników jest zgodna z oczekiwaniami
        self.assertEqual(len(users), 2)

        # Test 2: Pobranie użytkownika o określonym ID
        select_user_by_id_query = """
            SELECT * FROM users WHERE id = %s
        """
        self.cursor.execute(select_user_by_id_query, (1,))
        user = self.cursor.fetchone()
        
        # Sprawdzenie, czy pobrany użytkownik ma oczekiwane dane
        self.assertIsNotNone(user)
        self.assertEqual(user[1], 'John Doe')
        self.assertEqual(user[2], 'john@example.com')

    def test_update_user(self):
        add_user_query = """
            INSERT INTO users (name, email) VALUES (%s, %s)
        """
        users_data = [
            ('John Doe', 'john@example.com'),
            ('Jane Smith', 'jane@example.com')
        ]
        for user_data in users_data:
            self.cursor.execute(add_user_query, user_data)
        self.cnx.commit()

        # Aktualizacja danych użytkownika
        update_user_query = """
            UPDATE users SET name = %s, email = %s WHERE id = %s
        """
        new_name = 'Jane Smith'
        new_email = 'jane@example.com'
        user_id = 1  # Uwaga: ID użytkownika, którego chcemy zaktualizować
        self.cursor.execute(update_user_query, (new_name, new_email, user_id))
        self.cnx.commit()

        # Sprawdzenie, czy dane użytkownika zostały pomyślnie zaktualizowane
        select_user_query = """
            SELECT * FROM users WHERE id = %s
        """
        self.cursor.execute(select_user_query, (user_id,))
        user = self.cursor.fetchone()
        self.assertIsNotNone(user)
        self.assertEqual(user[1], new_name)
        self.assertEqual(user[2], new_email)

        # Test 2: Aktualizacja danych innego użytkownika
        new_name2 = 'Michael Johnson'
        new_email2 = 'michael@example.com'
        user_id2 = 2
        self.cursor.execute(update_user_query, (new_name2, new_email2, user_id2))
        self.cnx.commit()

        # Sprawdzenie, czy dane użytkownika zostały pomyślnie zaktualizowane
        self.cursor.execute(select_user_query, (user_id2,))
        user2 = self.cursor.fetchone()
        self.assertIsNotNone(user2)
        self.assertEqual(user2[1], new_name2)
        self.assertEqual(user2[2], new_email2)

    def test_delete_user(self):
        # Test 1: Usunięcie użytkownika o określonym ID
        add_user_query = """
            INSERT INTO users (name, email) VALUES (%s, %s)
        """
        users_data = [
            ('John Doe', 'john@example.com'),
            ('Jane Smith', 'jane@example.com')
        ]
        for user_data in users_data:
            self.cursor.execute(add_user_query, user_data)
        self.cnx.commit()
        
        delete_user_query = """
            DELETE FROM users WHERE id = %s
        """
        user_id = 1
        self.cursor.execute(delete_user_query, (user_id,))
        self.cnx.commit()

        # Sprawdzenie, czy użytkownik został pomyślnie usunięty
        select_user_query = """
            SELECT * FROM users WHERE id = %s
        """
        self.cursor.execute(select_user_query, (user_id,))
        user = self.cursor.fetchone()
        self.assertIsNone(user)

        # Test 2: Usunięcie innego użytkownika
        user_id2 = 2
        self.cursor.execute(delete_user_query, (user_id2,))
        self.cnx.commit()

        # Sprawdzenie, czy użytkownik został pomyślnie usunięty
        self.cursor.execute(select_user_query, (user_id2,))
        user2 = self.cursor.fetchone()
        self.assertIsNone(user2)
        
if __name__ == '__main__':
    unittest.main()
