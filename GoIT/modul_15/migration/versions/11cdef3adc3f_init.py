"""Init

Revision ID: 11cdef3adc3f
Revises: 
Create Date: 2022-10-30 22:51:53.452412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11cdef3adc3f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('news',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=250), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('link_news', sa.String(length=200), nullable=False),
    sa.Column('views', sa.String(length=10), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('news')
    # ### end Alembic commands ###
