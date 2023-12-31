"""empty message

Revision ID: 4f8254cfab29
Revises: 8ce942bef2e5
Create Date: 2023-09-30 16:32:23.901774

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4f8254cfab29'
down_revision = '8ce942bef2e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # op.drop_table('langchain_pg_embedding')
    # op.drop_table('langchain_pg_collection')
    with op.batch_alter_table('call', schema=None) as batch_op:
        batch_op.drop_constraint('call_session_id_key', type_='unique')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('call', schema=None) as batch_op:
        batch_op.create_unique_constraint('call_session_id_key', ['session_id'])

    # op.create_table('langchain_pg_collection',
    # sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('cmetadata', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    # sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False),
    # sa.PrimaryKeyConstraint('uuid', name='langchain_pg_collection_pkey'),
    # postgresql_ignore_search_path=False
    # )
    # op.create_table('langchain_pg_embedding',
    # sa.Column('collection_id', sa.UUID(), autoincrement=False, nullable=True),
    # sa.Column('embedding', sa.NullType(), autoincrement=False, nullable=True),
    # sa.Column('document', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('cmetadata', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=True),
    # sa.Column('custom_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    # sa.Column('uuid', sa.UUID(), autoincrement=False, nullable=False),
    # sa.ForeignKeyConstraint(['collection_id'], ['langchain_pg_collection.uuid'], name='langchain_pg_embedding_collection_id_fkey', ondelete='CASCADE'),
    # sa.PrimaryKeyConstraint('uuid', name='langchain_pg_embedding_pkey')
    # )
    # ### end Alembic commands ###
