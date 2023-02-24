"""Task fields

Revision ID: e8f9d6c204f0
Revises: 640539169725
Create Date: 2023-02-21 22:08:14.854418

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "e8f9d6c204f0"
down_revision = "640539169725"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("task", sa.Column("deadline", sa.Time(), nullable=True))
    op.add_column("task", sa.Column("is_done", sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("task", "is_done")
    op.drop_column("task", "deadline")
    # ### end Alembic commands ###
