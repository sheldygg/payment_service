"""inital

Revision ID: 8d65a0cc60d9
Revises: 
Create Date: 2024-10-18 01:11:30.464719

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8d65a0cc60d9"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "wallet",
        sa.Column("address", sa.String(), primary_key=True),
        sa.Column("private_key", sa.String(), nullable=False),
    )
    op.create_table(
        "payment",
        sa.Column("id", sa.String(), primary_key=True),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("description", sa.String(), nullable=False),
    )


def downgrade() -> None:
    op.drop_table("payment")
    op.drop_table("wallet")
