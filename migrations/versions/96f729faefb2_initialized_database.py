"""initialized database

Revision ID: 96f729faefb2
Revises: 
Create Date: 2021-06-02 14:18:27.527024

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '96f729faefb2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip',
    sa.Column('trip_id', sa.Integer(), nullable=False),
    sa.Column('starttime', sa.DateTime(), nullable=False),
    sa.Column('stoptime', sa.DateTime(), nullable=False),
    sa.Column('bikeid', sa.Integer(), nullable=False),
    sa.Column('from_station_id', sa.Integer(), nullable=False),
    sa.Column('from_station_name', sa.String(length=80), nullable=False),
    sa.Column('to_station_id', sa.Integer(), nullable=False),
    sa.Column('to_station_name', sa.String(length=80), nullable=False),
    sa.Column('usertype', sa.String(length=80), nullable=False),
    sa.Column('gender', sa.String(length=80), nullable=True),
    sa.Column('birthday', sa.String(length=80), nullable=True),
    sa.Column('trip_duration', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('trip_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('trip')
    # ### end Alembic commands ###
