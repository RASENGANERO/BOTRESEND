import sqlite3


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.connection_cursor = self.connection.cursor()
        self.cursor = self.connection_cursor

    async def all_users(self):
        with self.connection:
            result = self.cursor.execute("SELECT user_id FROM users").fetchall()
            return len(result)

    async def user_exists(self, user_id):
        result = self.cursor.execute("SELECT user_id FROM users WHERE user_id = ?", (user_id,)).fetchall()
        return bool(len(result))

    async def add_user(self, user_id):
        with self.connection:
            self.cursor.execute("INSERT INTO 'users' ('user_id') VALUES (?)", (user_id,))