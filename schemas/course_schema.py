from enum import Enum

from pydantic import BaseModel
from typing import Optional, List


class Course(BaseModel):
    course_name: str
    course_code: str
    course_serial: int
    course_instructor: str
    course_from: str
    course_credit: int
    course_outline: str
    course_language: str


class CourseQuery(BaseModel):

    # Note that since we should have some situation that we
    course_name: Optional[str] = None
    course_code: Optional[str] = None

class CourseResult(BaseModel):
    course_list: List[Course]