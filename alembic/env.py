from logging.config import fileConfig
import sys
import os

from sqlalchemy import engine_from_config, pool
from alembic import context

# -------------------------------------------------
# Ensure app/ is importable
# -------------------------------------------------
sys.path.append(os.getcwd())

# -------------------------------------------------
# Import Base and ALL models
# -------------------------------------------------
from app.models.base import Base

# IMPORTANT: import models so Alembic sees tables
from app.models.user import User
from app.models.role import Role
from app.models.permission import Permission
from app.models.user_role import UserRole
from app.models.roles_permission import RolePermission
from app.models.inverter import Inverter

# -------------------------------------------------
# Alembic config
# -------------------------------------------------
config = context.config

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

# -------------------------------------------------
# Offline migrations
# -------------------------------------------------
def run_migrations_offline() -> None:
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

# -------------------------------------------------
# Online migrations
# -------------------------------------------------
def run_migrations_online() -> None:
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True
        )

        with context.begin_transaction():
            context.run_migrations()

# -------------------------------------------------
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
