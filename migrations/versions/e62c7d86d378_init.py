"""Init

Revision ID: e62c7d86d378
Revises:
Create Date: 2023-12-24 22:23:43.919796

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e62c7d86d378"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("email", sa.String(), nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("hashed_password", sa.String(length=1024), nullable=False),
        sa.Column("is_admin", sa.Boolean(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("email"),
        sa.UniqueConstraint("username"),
    )
    op.create_table(
        "advertisement",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("body", sa.String(), nullable=True),
        sa.Column(
            "adv_type",
            sa.Enum("SALE", "PURCHASE", "SERVICE", name="advertisementtype"),
            nullable=True,
        ),
        sa.Column("header", sa.String(), nullable=True),
        sa.Column("timestamp", sa.TIMESTAMP(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "review",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column("user_id", sa.Integer(), nullable=True),
        sa.Column("rating", sa.Integer(), nullable=True),
        sa.Column("advertisement_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["advertisement_id"],
            ["advertisement.id"],
        ),
        sa.ForeignKeyConstraint(
            ["user_id"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("review")
    op.drop_table("advertisement")
    op.drop_table("user")
    # ### end Alembic commands ###
