from __future__ import annotations

import dataclasses
from uuid import UUID

import typing

from stocks_website.database import db

from sqlalchemy.dialects.postgresql import UUID as UUIDColumn, UUID


@dataclasses.dataclass()
class UserDTO:
    id: UUID
    email: str
    first_name: str
    last_name: str

    @staticmethod
    def create_from_db(id: typing.Union[UUID, str],
                       email: str,
                       first_name: str,
                       last_name: str,
                       *args) -> UserDTO:
        if isinstance(id, str):
            id = UUID(id)
        return UserDTO(id=id,
                       email=email,
                       first_name=first_name,
                       last_name=last_name)


class User(db.Model):
    id = db.Column(UUIDColumn, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Binary(), nullable=False)
