from __future__ import annotations

import dataclasses
from uuid import UUID

import typing

from sqlalchemy import func

from stocks_website.database import db

from sqlalchemy.dialects.postgresql import UUID as UUIDColumn, UUID, ENUM


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
    id = db.Column(UUIDColumn, primary_key=True, server_default=func.uuid_generate_v4())
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    password = db.Column(db.Binary(), nullable=False)
    country = db.Column(db.String(120), nullable=True)
    sex = db.Column(ENUM("female", "male", "other", name="sex_enum", create_type=True),
                    nullable=False,
                    default='other')
    addresses = db.relationship('Address')


class Address(db.Model):
    id = db.Column(UUIDColumn, primary_key=True, server_default=func.uuid_generate_v4())
    street_address = db.Column(db.String(255), nullable=False)
    city = db.Column(db.String(255), nullable=False)
    zipcode = db.Column(db.String(30), nullable=True)
    user_id = db.Column(UUIDColumn, db.ForeignKey('user.id'))
