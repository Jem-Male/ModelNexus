from ai_api_nexus.client import client as cl
from ai_api_nexus.config import AI_MODEL
from ai_api_nexus.curse.schemas import ReturnSchemaTask, TaskSchema

instructions =f"""
Create a question based on the course materials 
that were sent to you.
Choose the most important topic 
and formulate a question about it. 
Provide your answer strictly in
the following format:
{ReturnSchemaTask}
"""

def create_task(cache) -> tuple[TaskSchema, str]:
    response = cl.chat.completions.create(
        model=AI_MODEL, #type: ignore
        messages=[
            {"role": "system", "content": instructions},
            *cache
        ]
    )

    result = response.choices[0].message.content
    return [TaskSchema.model_validate_json(result), result] #type: ignore