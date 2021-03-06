"""Update Paper model

Revision ID: 213e87a58f3a
Revises: 9e01561ae1ac
Create Date: 2020-03-18 10:52:25.756953

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '213e87a58f3a'
down_revision = '9e01561ae1ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('paper', 'arxiv_primary_category',
               existing_type=mysql.VARCHAR(length=16),
               type_=sa.String(length=127),
               existing_nullable=True)
    op.alter_column('paper', 'journal_reference',
               existing_type=mysql.VARCHAR(length=127),
               type_=sa.TEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('paper', 'journal_reference',
               existing_type=sa.TEXT(),
               type_=mysql.VARCHAR(length=127),
               existing_nullable=True)
    op.alter_column('paper', 'arxiv_primary_category',
               existing_type=sa.String(length=127),
               type_=mysql.VARCHAR(length=16),
               existing_nullable=True)
    # ### end Alembic commands ###
