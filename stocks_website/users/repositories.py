from stocks_website.users.models import UserDTO


class LoginFailed(Exception):
    pass


### RAW DB-API example ###

class UsersRepository:
    def __init__(self, connection):
        self.connection = connection

    def login(self, email: str, password: str) -> UserDTO:
        cursor = self.connection.cursor()

        cursor.execute(
            """
            SELECT id, email, first_name, last_name FROM users
            WHERE email = %s
            AND password = digest(%s, 'sha256')::varchar
            """,
            (email, password)
        )

        if not cursor.rowcount:
            raise LoginFailed()

        result = cursor.fetchone()

        return UserDTO.create_from_db(*result)
