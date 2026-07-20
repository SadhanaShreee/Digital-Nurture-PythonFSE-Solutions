"""initial schema

Revision ID: 2b53c7884622
Revises: 
Create Date: 2026-07-20 11:37:09.316212

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b53c7884622'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # departments - no foreign keys, so it must be created first
    op.create_table('departments',
        sa.Column('dept_id', sa.Integer(), nullable=False),
        sa.Column('dept_name', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('dept_id')
    )

    # students - depends on departments
    op.create_table('students',
        sa.Column('student_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=True),
        sa.Column('last_name', sa.String(length=50), nullable=True),
        sa.Column('email', sa.String(length=100), nullable=True),
        sa.Column('enrollment_year', sa.Integer(), nullable=True),
        sa.Column('dept_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['dept_id'], ['departments.dept_id']),
        sa.PrimaryKeyConstraint('student_id'),
        sa.UniqueConstraint('email')
    )

    # professors - depends on departments
    op.create_table('professors',
        sa.Column('professor_id', sa.Integer(), nullable=False),
        sa.Column('first_name', sa.String(length=50), nullable=True),
        sa.Column('last_name', sa.String(length=50), nullable=True),
        sa.Column('dept_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['dept_id'], ['departments.dept_id']),
        sa.PrimaryKeyConstraint('professor_id')
    )

    # courses - depends on professors
    op.create_table('courses',
        sa.Column('course_id', sa.Integer(), nullable=False),
        sa.Column('course_code', sa.String(length=20), nullable=True),
        sa.Column('course_name', sa.String(length=100), nullable=True),
        sa.Column('professor_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['professor_id'], ['professors.professor_id']),
        sa.PrimaryKeyConstraint('course_id')
    )

    # enrollments - depends on both students and courses, so created last
    op.create_table('enrollments',
        sa.Column('enrollment_id', sa.Integer(), nullable=False),
        sa.Column('student_id', sa.Integer(), nullable=True),
        sa.Column('course_id', sa.Integer(), nullable=True),
        sa.Column('grade', sa.String(length=2), nullable=True),
        sa.ForeignKeyConstraint(['course_id'], ['courses.course_id']),
        sa.ForeignKeyConstraint(['student_id'], ['students.student_id']),
        sa.PrimaryKeyConstraint('enrollment_id')
    )


def downgrade():
    # drop in EXACT reverse order - enrollments depends on students/courses,
    # so it must go first; departments has nothing depending on it, so it's last
    op.drop_table('enrollments')
    op.drop_table('courses')
    op.drop_table('professors')
    op.drop_table('students')
    op.drop_table('departments')