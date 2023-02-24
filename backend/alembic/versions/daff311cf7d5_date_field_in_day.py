"""date field in day

Revision ID: daff311cf7d5
Revises: 46df3b8662c3
Create Date: 2023-02-24 17:54:32.439918

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = 'daff311cf7d5'
down_revision = '46df3b8662c3'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('day', sa.Column('day_date', sa.Date(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('day', 'day_date')
    # ### end Alembic commands ###
