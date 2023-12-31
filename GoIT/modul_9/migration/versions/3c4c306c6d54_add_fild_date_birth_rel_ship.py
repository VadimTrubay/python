"""add fild date_birth rel-ship

Revision ID: 3c4c306c6d54
Revises: 8f08d1d8d2f5
Create Date: 2022-09-06 17:46:48.399801

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c4c306c6d54'
down_revision = '8f08d1d8d2f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('persons', sa.Column('date_birth', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('persons', 'date_birth')
    # ### end Alembic commands ###
