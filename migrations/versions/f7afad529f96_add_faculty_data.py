"""add faculty data

Revision ID: f7afad529f96
Revises: 7ab92dea48cb
Create Date: 2021-09-28 15:04:57.950214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7afad529f96'
down_revision = '7ab92dea48cb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('dept_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id', 'dept_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('faculty')
    # ### end Alembic commands ###
