"""empty message

Revision ID: 61adbe60a180
Revises: 
Create Date: 2024-05-20 17:05:00.353944

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61adbe60a180'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('club',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('city', sa.String(length=60), nullable=False),
    sa.Column('gym', sa.String(length=60), nullable=False),
    sa.Column('address', sa.String(length=180), nullable=True),
    sa.Column('phone', sa.String(length=60), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('url', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('coach',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nickname', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('lastname', sa.String(length=40), nullable=False),
    sa.Column('description', sa.String(length=180), nullable=False),
    sa.Column('image', sa.String(length=180), nullable=True),
    sa.Column('speciality', sa.String(length=80), nullable=False),
    sa.Column('calendar', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('shop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('product', sa.String(length=120), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('vip_price', sa.Float(), nullable=True),
    sa.Column('image_product', sa.String(length=200), nullable=False),
    sa.Column('description', sa.String(length=180), nullable=False),
    sa.Column('type', sa.String(length=80), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('nickname', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=40), nullable=False),
    sa.Column('lastname', sa.String(length=40), nullable=False),
    sa.Column('rol', sa.String(length=40), nullable=False),
    sa.Column('calendar', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('shop_car',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['shop.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shop_car')
    op.drop_table('user')
    op.drop_table('shop')
    op.drop_table('coach')
    op.drop_table('club')
    # ### end Alembic commands ###
