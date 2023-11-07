"""empty message

Revision ID: 265c4d507126
Revises: 672af8e8096f
Create Date: 2023-10-14 21:40:19.387535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '265c4d507126'
down_revision = '672af8e8096f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resource', schema=None) as batch_op:
        batch_op.drop_column('training_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('resource', schema=None) as batch_op:
        batch_op.add_column(sa.Column('training_id', sa.VARCHAR(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###