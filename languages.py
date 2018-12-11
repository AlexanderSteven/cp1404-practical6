from prac6.programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage ("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage ("Visual Basic", "Static", False, 1991)

print(python)

language = [ruby, python, visual_basic]

for language in languages:
    if language.is_dynamic():
        print(language.name)