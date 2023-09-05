"""fix schemas

Revision ID: 9219327b4b7a
Revises: 83494b65a6a6
Create Date: 2023-04-22 22:14:57.072067

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '9219327b4b7a'
down_revision = '83494b65a6a6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'role')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('role', postgresql.ENUM(name='roles'), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
