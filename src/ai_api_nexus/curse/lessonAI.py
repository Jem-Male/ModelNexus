from ai_api_nexus.client import client as cl
from ai_api_nexus.config import AI_MODEL
from ai_api_nexus.curse.schemas import ReturnSchemaLesson, LessonSchema, LessonPlanSchema

instructions =f"""
You have been provided with a topic and an outline to use for creating a lesson.
The response should be in the following format:
{ReturnSchemaLesson}
"""

def create_lesson(input_theme: LessonPlanSchema) -> tuple[LessonSchema, str]:
    content = f"""
    name: {input_theme.lesson_name}
    plan: {input_theme.lesson_plan}
    """
    response = cl.chat.completions.create(
        model=AI_MODEL, #type: ignore
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": content},
        ]
    )
    result = response.choices[0].message.content
    return LessonSchema.model_validate_json(result), result #type: ignore