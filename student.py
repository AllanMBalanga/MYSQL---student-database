from database import Database

class Student():
    def __init__(self):
        self.db = Database()

    def check_login(self, email, password):
        query = "SELECT * FROM account WHERE email = %s AND password = %s"
        result = self.db.fetch_all(query, (email, password))
        return bool(result)  # Returns True if login is successful

    def create_account(self, email, password):
        # Check if email already exists
        query = "SELECT email FROM account WHERE email = %s"
        existing_account = self.db.fetch_all(query, (email,))
        if existing_account:
            return False  # Email already exists

        # Create new account
        query = "INSERT INTO account (email, password) VALUES (%s, %s)"
        self.db.execute_query(query, (email, password))
        return True


    def post(self, name, student_id, email, phone, gender=None):
        query = "INSERT INTO student (name, student_id, email, phone, gender) VALUES (%s, %s, %s, %s, %s)"
        values = (name, student_id, email, phone, gender)

        self.db.execute_query(query,values)

    def update(self, id, **kwargs):
        keys = ", ".join([f"{key} = %s" for key in kwargs])
        query = f"UPDATE student SET {keys} WHERE id = %s"
        values = list(kwargs.values()) + [id]

        self.db.execute_query(query,values)

    def delete(self, id):
        query = "DELETE FROM student WHERE id = %s"
        self.db.execute_query(query,(id,))

    def fetch_all(self):
        query = "SELECT * FROM student"
        return self.db.fetch_all(query)


