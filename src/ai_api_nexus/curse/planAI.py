from ai_api_nexus.client import client as cl
from ai_api_nexus.config import AI_MODEL
from ai_api_nexus.curse.schemas import ReturnSchemaCursePlan, CursePlanSchema

instructions =f"""
    You draw up a strict plan and don’t create anything yourself!
    Develop a 6-stage course plan on the specified topic.
    The plan must include 6 theoretical lessons that explore the essence of the topic.
    Prepare the response in the language specified by the user.
    Strictly follow these instructions!
    The response must be formatted as follows:
    In the 'lesson name' field, you enter the title of the lesson.
    {ReturnSchemaCursePlan}
"""

def create_plan(input_theme) -> CursePlanSchema:
    response = cl.chat.completions.create(
        model=AI_MODEL, #type: ignore
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": input_theme}
        ]
    )

    result = response.choices[0].message.content
    return CursePlanSchema.model_validate_json(result) #type: ignore