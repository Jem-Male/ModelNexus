from ai_api_nexus.curse.lessonAI import create_lesson
from ai_api_nexus.curse.planAI import create_plan
from ai_api_nexus.curse.quizAI import create_quiz
from ai_api_nexus.curse.taskAI import create_task

theme = str(input())
cache = []

try:
    plan = create_plan(theme)
    print(plan)
    cache.append({"role": "assistant", "content": plan.model_dump_json()})
    lessons = []
    for les in plan.lessons:
        lesson = create_lesson(les)
        print(lesson)
        cache.append({"role": "assistant", "content": lesson.model_dump_json()})
        lessons.append(lesson)
    quiz = create_quiz(cache)
    print(quiz)
    task = create_task(cache)
    print(task)
    
except Exception as e:
    raise e

