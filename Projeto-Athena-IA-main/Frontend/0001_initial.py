from alembic import op
import sqlalchemy as sa

revision = "0001_initial"
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table("users",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("email", sa.String(255), nullable=False),
        sa.Column("name", sa.String(150), nullable=False),
        sa.Column("password_hash", sa.String(255), nullable=False),
        sa.Column("active", sa.Boolean(), nullable=False, server_default=sa.true()))
    op.create_index("ix_users_email", "users", ["email"], unique=True)

    op.create_table("tasks",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("description", sa.String(1000)),
        sa.Column("priority", sa.String(20), nullable=False, server_default="normal"),
        sa.Column("completed", sa.Boolean(), nullable=False, server_default=sa.false()))
    op.create_index("ix_tasks_user_id", "tasks", ["user_id"])

    op.create_table("routines",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("title", sa.String(200), nullable=False),
        sa.Column("description", sa.String(1000)),
        sa.Column("duration_minutes", sa.Integer()))
    op.create_index("ix_routines_user_id", "routines", ["user_id"])

    op.create_table("diary_entries",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("user_id", sa.Integer(), sa.ForeignKey("users.id", ondelete="CASCADE"), nullable=False),
        sa.Column("content", sa.Text(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False))

    op.create_index("ix_diary_entries_user_id", "diary_entries", ["user_id"])

def downgrade():
    op.drop_table("diary_entries")
    op.drop_table("routines")
    op.drop_table("tasks")
    op.drop_table("users")
