from ai_api_nexus.client import client as cl
from ai_api_nexus.config import AI_MODEL
from ai_api_nexus.curse.schemas import ReturnQuizSchema, QuizSchema

instructions =f"""
Create a quiz with 4 answer options, 
one of which is correct. You may 
use the material from the courses 
you were sent to create the quiz. 
Provide your answer strictly in 
the following format, as a list of 4 quiz items:
{ReturnQuizSchema}
"""

def create_quiz(cache) -> QuizSchema:
    response = cl.chat.completions.create(
        model=AI_MODEL, #type: ignore
        messages=[
            {"role": "system", "content": instructions},
            *cache
        ]
    )

    result = response.choices[0].message.content
    return QuizSchema.model_validate_json(result) #type: ignore