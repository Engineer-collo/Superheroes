"""Initial migration

Revision ID: c1b77dd6d6f4
Revises: 
Create Date: 2025-03-29 16:56:42.174508

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1b77dd6d6f4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('heroes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('super_name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('powers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('description', sa.String(length=300), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hero_power',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('strength', sa.String(length=255), nullable=False),
    sa.Column('hero_id', sa.Integer(), nullable=False),
    sa.Column('power_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hero_id'], ['heroes.id'], name=op.f('fk_hero_power_hero_id_heroes')),
    sa.ForeignKeyConstraint(['power_id'], ['powers.id'], name=op.f('fk_hero_power_power_id_powers')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('hero_power')
    op.drop_table('powers')
    op.drop_table('heroes')
    # ### end Alembic commands ###
