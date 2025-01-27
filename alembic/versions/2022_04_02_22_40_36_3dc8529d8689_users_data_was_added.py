"""users data was added

Revision ID: 3dc8529d8689
Revises: b6a744784764
Create Date: 2022-04-03 17:40:36.446728

"""
import logging
from dataclasses import asdict

from alembic import op
from sqlalchemy import column, table, Integer, Text, DateTime, Boolean, Date
from scripts.faker.users import User, generate


# revision identifiers, used by Alembic.
revision = "3dc8529d8689"
down_revision = "b6a744784764"
branch_labels = None
depends_on = None


def upgrade():
    users_table = table(
        "users",
        column("id", Integer),
        column("email", Text),
        column("password", Text),
        column("created_at", DateTime),
        column("is_active", Boolean),
        column("name", Text),
        column("birthday", Date),
    )

    users: list[User] = generate(count=100)

    try:
        op.bulk_insert(
            users_table,
            [asdict(user) for user in users],
        )
    except Exception as err:
        logging.warning(f"Error with users' data insertion: {err}")
        raise


def downgrade():
    pass
