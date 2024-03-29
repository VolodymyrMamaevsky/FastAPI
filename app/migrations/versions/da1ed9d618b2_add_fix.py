"""add fix

Revision ID: da1ed9d618b2
Revises: 03784c15252d
Create Date: 2024-01-11 17:42:57.551598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'da1ed9d618b2'
down_revision: Union[str, None] = '03784c15252d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('rooms', sa.Column('description', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('rooms', 'description')
    # ### end Alembic commands ###
