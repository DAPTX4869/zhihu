"""empty message

Revision ID: 7796e07f95a2
Revises: 9908acb03a07
Create Date: 2018-08-03 20:39:35.995979

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7796e07f95a2'
down_revision = '9908acb03a07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('question_id', sa.Integer(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['question.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answer')
    # ### end Alembic commands ###
