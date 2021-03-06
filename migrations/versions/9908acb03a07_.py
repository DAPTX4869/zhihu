"""empty message

Revision ID: 9908acb03a07
Revises: d58b8cddaffb
Create Date: 2018-08-03 16:57:43.404543

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9908acb03a07'
down_revision = 'd58b8cddaffb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answer',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
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
