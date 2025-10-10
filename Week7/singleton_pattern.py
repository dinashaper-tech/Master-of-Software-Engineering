import sqlite3
import threading

class DatabaseConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if  cls._instance is None:
                    cls._instance = super().__new__(cls)
                    cls._instance_connection =None
        return cls._instance

    def get_connection(self):
        if self.connection is None:
            self._connection = sqlite3.connect('app.db',check_same_thread=False)
        return self.connection

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.connection = None


class UserService:
    def __init__(self):
        self.db = DatabaseConnection()

    def get_user(self, user_id):
        conn = self.db.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE id = ?", (user_id,))
        return cursor.fetchone()
    
    class OrderService:
        def __init__(self):
            self.db = DatabaseConnection()

        def get_orders(self, user_id):
            conn = self.db.get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM orders WHERE user_id = ?", (user_id,))
            return cursor.fetchall()



if __name__ == "__main__":
    import sqlite3

    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEFER PRIMARY KEY, name TEXT)")
    cursor.execute("CREATE TABLE IF NOT EXISTS orders (id INTEGER PRIMARY KEY, user_id INTEGER, item TEXT)")

    cursor.execute("INSERT INTO users (name) VALUES ('Alice')")
    cursor.execute("INSERT INTO users (name) VALUES ('Bob')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (1, 'Book')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (1, 'Laptop')")
    cursor.execute("INSERT INTO orders (user_id, item) VALUES (2, 'Phone')")

    conn.commit()
    conn.close()

    user_service = UserService()
    order_service = OrderService()
    print(user_service.get_user(1))
    print(order_service.get_orders(1))

