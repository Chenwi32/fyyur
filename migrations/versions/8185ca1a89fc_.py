"""empty message

Revision ID: 8185ca1a89fc
Revises: de2b49fd240b
Create Date: 2022-08-20 05:42:09.572936

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8185ca1a89fc'
down_revision = 'de2b49fd240b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shows')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shows',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('artist_id', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('venue_id', sa.VARCHAR(length=120), autoincrement=False, nullable=True),
    sa.Column('start_time', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='shows_pkey')
    )
    # ### end Alembic commands ###
