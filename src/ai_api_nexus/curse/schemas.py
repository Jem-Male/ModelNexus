from pydantic import BaseModel, Field
from typing import Annotated
import json


class LessonPlanSchema(BaseModel):
    lesson_name: Annotated[str, Field(max_length=250)]
    lesson_plan: str


class CursePlanSchema(BaseModel):
    title: Annotated[str, Field(max_length=250, description='Course name')]
    lessons: list[LessonPlanSchema]

ReturnSchemaCursePlan = json.dumps(CursePlanSchema.model_json_schema(), ensure_ascii=False)


class LessonSchema(BaseModel):
    title: Annotated[str, Field(max_length=250, description='a lesson title')]
    description: Annotated[str, Field(description='the content of a lesson prepared according to a plan')]

ReturnSchemaLesson = json.dumps(LessonSchema.model_json_schema(), ensure_ascii=False)


class TaskSchema(BaseModel):
    title: Annotated[str, Field(max_length=200, description='question title')]
    question_text: Annotated[str, Field(description='description of the issue')]

ReturnSchemaTask = json.dumps(TaskSchema.model_json_schema(), ensure_ascii=False)


QuizSchemaFeedbackDescription = """
The `feedback` field stores a text 
explanation or hint that is shown to 
the user immediately after they select 
a given answer option, clarifying why 
it is correct or incorrect.
"""

class QuizOptionSchema(BaseModel):
    question_text: Annotated[str, Field(max_length=150, description='Option Text')]
    is_correct: bool
    feedback: Annotated[str, Field(max_length=250, description=QuizSchemaFeedbackDescription)]

class QuizSchema(BaseModel):
    options_test: Annotated[str, Field(max_length=200, description='quiz question')]
    quiz_options: list[QuizOptionSchema]

ReturnQuizSchema = json.dumps(QuizSchema.model_json_schema(), ensure_ascii=False)