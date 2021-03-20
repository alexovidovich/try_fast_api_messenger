"""secound

Revision ID: d4a27cc33472
Revises: f706602bdf50
Create Date: 2021-03-19 21:36:13.159959

"""
from alembic import op
import sqlalchemy as sa

import sqlalchemy_utils
# revision identifiers, used by Alembic.
revision = 'd4a27cc33472'
down_revision = 'f706602bdf50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=255), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('_phone_number', sa.Unicode(length=20), nullable=True),
    sa.Column('country_code', sa.Unicode(length=8), nullable=True),
    sa.Column('nickname', sa.String(length=30), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
