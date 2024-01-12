"""Add location777 to hotels

Revision ID: 53215709f35f
Revises: e600104d05a0
Create Date: 2024-01-11 17:33:10.466484

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '53215709f35f'
down_revision: Union[str, None] = 'e600104d05a0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('location777', sa.String(), nullable=False))
    op.drop_column('hotels', 'locations')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('locations', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'location777')
    # ### end Alembic commands ###
