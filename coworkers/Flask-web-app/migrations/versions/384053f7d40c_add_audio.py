"""Add audio

Revision ID: 384053f7d40c
Revises: 22f198a3476e
Create Date: 2022-09-19 17:18:41.141608

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '384053f7d40c'
down_revision = '22f198a3476e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('audios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('path', sa.String(length=350), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('path')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('audios')
    # ### end Alembic commands ###
