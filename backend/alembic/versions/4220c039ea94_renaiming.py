"""renaiming

Revision ID: 4220c039ea94
Revises: 1cb448911678
Create Date: 2023-03-29 11:31:59.139535

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4220c039ea94"
down_revision = "1cb448911678"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("verification_ids", sa.Column("verification_code", sa.UUID(), nullable=True))
    op.drop_column("verification_ids", "verification_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("verification_ids", sa.Column("verification_id", sa.UUID(), autoincrement=False, nullable=True))
    op.drop_column("verification_ids", "verification_code")
    # ### end Alembic commands ###
