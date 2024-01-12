"""add fix

Revision ID: c69f476a0f6b
Revises: 53215709f35f
Create Date: 2024-01-11 17:34:21.615535

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c69f476a0f6b'
down_revision: Union[str, None] = '53215709f35f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('location', sa.String(), nullable=False))
    op.drop_column('hotels', 'location777')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('location777', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'location')
    # ### end Alembic commands ###