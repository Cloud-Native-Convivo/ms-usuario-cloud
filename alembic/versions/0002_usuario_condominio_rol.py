"""agrega tabla usuario_condominio_rol

Revision ID: 0002
Revises: 0001
Create Date: 2026-10-16

"""
from collections.abc import Sequence

import sqlalchemy as sa

from alembic import op

revision: str = "0002"
down_revision: str | Sequence[str] | None = "0001"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "usuario_condominio_rol",
        sa.Column("id", sa.Integer(), sa.Identity(), primary_key=True),
        sa.Column("usuario_id", sa.Integer(), sa.ForeignKey("usuarios.id", ondelete="CASCADE"), nullable=False),
        sa.Column("condominio_id", sa.Integer(), nullable=False),
        sa.Column("unidad_id", sa.Integer(), nullable=True),
        sa.Column("rol", sa.String(20), nullable=False),
        sa.Column("activo", sa.Boolean(), nullable=False, server_default=sa.true()),
    )
    op.create_index("ix_ucr_usuario_id", "usuario_condominio_rol", ["usuario_id"])
    op.create_index("ix_ucr_condominio_id", "usuario_condominio_rol", ["condominio_id"])
    op.create_unique_constraint(
        "uq_ucr_asociacion", "usuario_condominio_rol", ["usuario_id", "condominio_id", "unidad_id", "rol"]
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint("uq_ucr_asociacion", "usuario_condominio_rol", type_="unique")
    op.drop_index("ix_ucr_condominio_id", table_name="usuario_condominio_rol")
    op.drop_index("ix_ucr_usuario_id", table_name="usuario_condominio_rol")
    op.drop_table("usuario_condominio_rol")
