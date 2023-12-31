"""Added Complaint

Revision ID: b9022a6ba665
Revises: 7fa3fe8faeb1
Create Date: 2023-12-25 21:25:52.036474

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b9022a6ba665"
down_revision: Union[str, None] = "7fa3fe8faeb1"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "complaint",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("text", sa.String(), nullable=True),
        sa.Column("created_at", sa.TIMESTAMP(), nullable=True),
        sa.Column(
            "complaint_type",
            sa.Enum(
                "fraud",
                "spam",
                "wrong_category",
                "obscene_expressions",
                name="complainttype",
            ),
            nullable=True,
        ),
        sa.Column("created_by", sa.Integer(), nullable=True),
        sa.Column("advertisement_id", sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(
            ["advertisement_id"],
            ["advertisement.id"],
        ),
        sa.ForeignKeyConstraint(
            ["created_by"],
            ["user.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("complaint")
    # ### end Alembic commands ###
