from ai_api_nexus.curse.lessonAI import create_lesson
from ai_api_nexus.curse.planAI import create_plan
from ai_api_nexus.curse.quizAI import create_quiz
from ai_api_nexus.curse.taskAI import create_task

theme = str(input())
cache = []

try:
    plan = create_plan(theme)
    print(plan[0])
    cache.append({"role": "assistant", "content": plan[1]})
    lessons = []
    for les in plan[0].lessons:
        lesson = create_lesson(les)
        print(lesson[0])
        cache.append({"role": "assistant", "content": lesson[1]})
        lessons.append(lesson[0])
    quiz = create_quiz(cache)
    print(quiz[0])
    task = create_task(cache)
    print(task)
    
except Exception as e:
    raise e