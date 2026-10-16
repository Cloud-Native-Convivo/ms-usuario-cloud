"""esquema inicial: usuarios

Revision ID: 0001
Revises:
Create Date: 2026-10-16

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0001"
down_revision: str | Sequence[str] | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "usuarios",
        sa.Column("id", sa.Integer(), sa.Identity(), primary_key=True),
        sa.Column("sub_identidad", sa.String(255), nullable=False),
        sa.Column("proveedor_identidad", sa.String(20), nullable=False),
        sa.Column("nombre", sa.String(255), nullable=True),
        sa.Column("correo", sa.String(255), nullable=True),
        sa.Column("activo", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.create_unique_constraint("uq_usuario_sub_identidad", "usuarios", ["sub_identidad"])


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_usuario_sub_identidad", "usuarios", type_="unique")
    op.drop_table("usuarios")
