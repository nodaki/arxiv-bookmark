"""Add User table

Revision ID: 6e3cb5332e64
Revises: 4dc2aa8f4235
Create Date: 2020-03-15 21:19:27.283966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e3cb5332e64'
down_revision = '4dc2aa8f4235'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('paper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.TEXT(), nullable=True),
    sa.Column('published', sa.DATETIME(), nullable=True),
    sa.Column('updated', sa.DATETIME(), nullable=True),
    sa.Column('is_new', sa.Boolean(), nullable=True),
    sa.Column('summary', sa.TEXT(), nullable=True),
    sa.Column('arxiv_url', sa.String(127), nullable=True),
    sa.Column('pdf_url', sa.String(127), nullable=True),
    sa.Column('arxiv_primary_category', sa.String(16), nullable=True),
    sa.Column('arxiv_comment', sa.TEXT(), nullable=True),
    sa.Column('affiliation', sa.String(127), nullable=True),
    sa.Column('journal_reference', sa.String(127), nullable=True),
    sa.Column('doi', sa.String(127), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_paper_id'), 'paper', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_paper_id'), table_name='paper')
    op.drop_table('paper')
    # ### end Alembic commands ###