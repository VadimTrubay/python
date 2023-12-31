"""add roles

Revision ID: ec800a6304b6
Revises: 33f8bd301846
Create Date: 2023-04-14 17:56:41.119389

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'ec800a6304b6'
down_revision = '33f8bd301846'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("CREATE TYPE role AS ENUM('admin', 'moderator', 'user')")
    op.add_column('users',
                  sa.Column('roles', sa.Enum('admin', 'moderator', 'user', name='role'), nullable=True, default='user'))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'roles')
    op.execute("DROP TYPE role")
    # ### end Alembic commands ###
