"""empty message

Revision ID: 22579677813f
Revises: 
Create Date: 2022-05-02 12:13:12.136154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22579677813f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('playlists',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.VARCHAR(length=255), nullable=False),
    sa.Column('owner', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.VARCHAR(length=127), nullable=False),
    sa.Column('email', sa.VARCHAR(length=255), nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=255), nullable=False),
    sa.Column('birth_date', sa.Date(), nullable=False),
    sa.Column('staff_level', sa.Integer(), nullable=True),
    sa.Column('inviter', sa.Integer(), nullable=False),
    sa.Column('github', sa.VARCHAR(length=255), nullable=False),
    sa.Column('linkedin', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('youtube',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('youtube', sa.VARCHAR(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('videos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('youtube_id', sa.Integer(), nullable=True),
    sa.Column('title', sa.VARCHAR(length=255), nullable=False),
    sa.Column('description', sa.VARCHAR(length=510), nullable=False),
    sa.Column('pkaylist', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pkaylist'], ['playlists.id'], ),
    sa.ForeignKeyConstraint(['youtube_id'], ['youtube.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('videos')
    op.drop_table('youtube')
    op.drop_table('users')
    op.drop_table('playlists')
    # ### end Alembic commands ###
