"""photo model fix

Revision ID: e91870495617
Revises: 48b3cfa769ee
Create Date: 2023-05-13 17:06:37.167059

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e91870495617'
down_revision = '48b3cfa769ee'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('unique_photo_user', 'photos', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('unique_photo_user', 'photos', ['user_id'])
    # ### end Alembic commands ###
