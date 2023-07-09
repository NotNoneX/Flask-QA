"""empty message

Revision ID: 22486d196121
Revises: fbc10888464a
Create Date: 2023-06-27 11:41:47.452725

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '22486d196121'
down_revision = 'fbc10888464a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               type_=sa.String(length=300),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=300),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=100),
               existing_nullable=False)

    # ### end Alembic commands ###
