"""empty message

Revision ID: fbc10888464a
Revises: 8015ec3a9bde
Create Date: 2023-06-27 11:40:18.326651

"""
import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'fbc10888464a'
down_revision = '8015ec3a9bde'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(collation='utf8mb4_general_ci', length=20),
               type_=sa.String(length=100),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=100),
               type_=mysql.VARCHAR(collation='utf8mb4_general_ci', length=20),
               existing_nullable=False)

    # ### end Alembic commands ###
