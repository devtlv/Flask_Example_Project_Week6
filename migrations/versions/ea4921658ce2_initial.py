"""initial

Revision ID: ea4921658ce2
Revises: 
Create Date: 2019-12-11 10:06:45.214442

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from sqlalchemy import func
from sqlalchemy.dialects.postgresql import UUID

revision = 'ea4921658ce2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.execute('CREATE EXTENSION "uuid-ossp"')
    op.create_table(
        'user',
        sa.Column('id', UUID, server_default=func.uuid_generate_v4()),
        sa.Column('email', sa.String(120), unique=True, nullable=False),
        sa.Column('first_name', sa.String(120), nullable=False),
        sa.Column('last_name', sa.String(120), nullable=False),
        sa.Column('password', sa.Binary(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade():
    op.drop_table('user')
