import hashlib

from sqlalchemy.exc import DatabaseError

from stocks_website.database import db
from stocks_website.users.models import UserDTO, User


class LoginFailed(Exception):
    pass


### RAW DB-API example ###

class RAWUsersRepository:
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


class UsersRepository:
    def register(self, email,
                 first_name,
                 last_name,
                 password,
                 country,
                 sex):
        user = User(email=email,
                    first_name=first_name,
                    last_name=last_name,
                    password=hashlib.sha256(password.encode('utf-8')).digest(),
                    country=country,
                    sex=sex)
        db.session.add(user)
        db.session.commit()
