"""add_country_to_user

Revision ID: 247141e40aa5
Revises: ea4921658ce2
Create Date: 2019-12-11 10:24:11.167338

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '247141e40aa5'
down_revision = 'ea4921658ce2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('country', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'country')
    # ### end Alembic commands ###
