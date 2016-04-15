"""empty message

Revision ID: 4b1245457a28
Revises: 049dfe12f581
Create Date: 2016-04-15 20:07:44.390210

"""

# revision identifiers, used by Alembic.
revision = '4b1245457a28'
down_revision = '049dfe12f581'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('source_sentence', sa.Text(), nullable=True))
    op.drop_column('question', 'source_sentece')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('source_sentece', sa.TEXT(), autoincrement=False, nullable=True))
    op.drop_column('question', 'source_sentence')
    ### end Alembic commands ###
