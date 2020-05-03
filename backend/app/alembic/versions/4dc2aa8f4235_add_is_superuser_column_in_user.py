"""Add is_superuser column in User

Revision ID: 4dc2aa8f4235
Revises: 2e9744b72098
Create Date: 2020-03-08 19:33:16.786176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4dc2aa8f4235'
down_revision = '2e9744b72098'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_superuser', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_superuser')
    # ### end Alembic commands ###
