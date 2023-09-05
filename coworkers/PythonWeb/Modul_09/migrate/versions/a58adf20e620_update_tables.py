"""update tables

Revision ID: a58adf20e620
Revises: d854c8b97c67
Create Date: 2022-09-03 20:19:48.913496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a58adf20e620'
down_revision = 'd854c8b97c67'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('phones',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('phone', sa.String(length=20), nullable=False),
    sa.Column('contacts_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['contacts_id'], ['contacts.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('contacts', 'phone')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('phone', sa.VARCHAR(length=20), autoincrement=False, nullable=False))
    op.drop_table('phones')
    # ### end Alembic commands ###
