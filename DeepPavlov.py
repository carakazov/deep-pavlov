from deeppavlov import build_model


def read_article():
    file = open("article.txt", "r", encoding='utf-8')
    content = file.readlines()
    file.close()
    return content


bot = build_model('squad_ru_bert', install=True, download=True)
context_batch = read_article()

is_running = True

print("Добрый вечер! Вас приветствует бот-гид. Здесь вы можете задать свой вопрос о Москве!")
print("Чтобы закончить, введите 'стоп'")

while is_running:
    question = input("Введите Ваш вопрос - ")
    if question != "стоп":
        answer = bot(context_batch, [question])
        print(answer[0][0])
    else:
        is_running = False
