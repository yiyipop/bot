import random
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Генераторы
def generate_russian_name():
    names = ["Иван", "Алексей", "Дмитрий", "Сергей", "Андрей"]
    surnames = ["Иванов", "Петров", "Сидоров", "Смирнов", "Кузнецов"]
    return f"👤 Имя: {random.choice(names)} {random.choice(surnames)}"

def generate_passport():
    series = random.randint(1000, 9999)
    number = random.randint(100000, 999999)
    return f"📄 Паспорт: Серия {series}, Номер {number}"

def generate_phone():
    return f"📱 Телефон: +7{random.randint(900, 999)}{random.randint(1000000, 9999999)}"

def generate_address():
    cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург", "Новосибирск"]
    streets = ["Ленина", "Пушкина", "Гагарина", "Советская", "Мира"]
    return f"🏠 Адрес: г. {random.choice(cities)}, ул. {random.choice(streets)}, д. {random.randint(1, 100)}"

def generate_credit_card():
    card_number = ''.join([str(random.randint(0, 9)) for _ in range(16)])
    expiry_date = f"{random.randint(1, 12):02d}/{random.randint(23, 30)}"
    cvv = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    return f"💳 Карта: Номер {card_number}, Срок действия {expiry_date}, CVV {cvv}"

def generate_business_name():
    types = ["ООО", "ИП", "АО"]
    names = ["Технологии", "Стройка", "Торговля", "Услуги", "Инновации"]
    return f"🏢 Компания: {random.choice(types)} '{random.choice(names)}'"

def generate_company():
    industries = ["IT", "Строительство", "Розничная торговля", "Услуги", "Производство"]
    names = ["Технологии", "Стройка", "Торговля", "Услуги", "Инновации"]
    cities = ["Москва", "Санкт-Петербург", "Казань", "Екатеринбург", "Новосибирск"]
    streets = ["Ленина", "Пушкина", "Гагарина", "Советская", "Мира"]
    address = f"г. {random.choice(cities)}, ул. {random.choice(streets)}, д. {random.randint(1, 100)}"
    return f"🏢 Компания: {random.choice(names)}, Отрасль: {random.choice(industries)}, Адрес: {address}"

def generate_business():
    ideas = ["Открыть кофейню", "Создать приложение для доставки еды", "Запустить онлайн-курсы"]
    return f"💡 Бизнес-идея: {random.choice(ideas)}"

def generate_inn():
    return f"📝 ИНН: {random.randint(1000000000, 9999999999)}"

def generate_snils():
    return f"📝 СНИЛС: {random.randint(10000000000, 99999999999)}"

def generate_bank_account():
    return f"🏦 Расчётный счёт: {random.randint(10000000000000000000, 99999999999999999999)}"

def generate_bic():
    return f"🏦 БИК: {random.randint(100000000, 999999999)}"

def generate_kpp():
    return f"📝 КПП: {random.randint(100000000, 999999999)}"

def generate_okpo():
    return f"📝 ОКПО: {random.randint(10000000, 99999999)}"

def generate_ogrn():
    return f"📝 ОГРН: {random.randint(1000000000000, 9999999999999)}"

def generate_oktmo():
    return f"📝 ОКТМО: {random.randint(10000000, 99999999)}"

def generate_okved():
    return f"📝 ОКВЭД: {random.randint(10, 99)}.{random.randint(10, 99)}"

def generate_email():
    domains = ["gmail.com", "yandex.ru", "mail.ru"]
    return f"📧 Email: {random.choice(['user', 'admin', 'test'])}{random.randint(1, 100)}@{random.choice(domains)}"

def generate_password():
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
    return f"🔑 Пароль: {''.join(random.choice(chars) for _ in range(12))}"

def generate_random_number():
    return f"🔢 Случайное число: {random.randint(1, 1000)}"

def generate_lorem_ipsum():
    return "📜 Lorem ipsum dolor sit amet, consectetur adipiscing elit."

def generate_meme():
    memes = ["Смешной мем 1", "Смешной мем 2", "Смешной мем 3"]
    return f"😂 Мем: {random.choice(memes)}"

def generate_business_idea():
    ideas = ["Открыть кофейню", "Создать приложение для доставки еды", "Запустить онлайн-курсы"]
    return f"💡 Бизнес-идея: {random.choice(ideas)}"

def generate_color_palette():
    colors = ["#FF5733", "#33FF57", "#3357FF", "#F1C40F", "#8E44AD"]
    return f"🎨 Цветовая палитра: {', '.join(colors)}"

def generate_qr_code_data():
    return f"📲 QR-код: https://example.com/{random.randint(1000, 9999)}"

def generate_date():
    year = random.randint(2020, 2025)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    return f"📅 Дата: {day:02d}.{month:02d}.{year}"

def generate_math_problem():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    return f"🧮 Задача: {a} + {b} = ?"

def generate_joke():
    jokes = ["Почему программисты любят тёмный режим? Потому что свет притягивает баги!", "Какой язык программирования самый крутой? Тот, на котором ты пишешь!"]
    return f"😂 Шутка: {random.choice(jokes)}"

def generate_quote():
    quotes = ["Всё, что не убивает, делает нас сильнее.", "Дорогу осилит идущий."]
    return f"📜 Цитата: {random.choice(quotes)}"

def generate_to_do_list():
    tasks = ["Купить молоко", "Позвонить другу", "Сделать домашку"]
    return f"📝 Список дел:\n" + "\n".join(tasks)

def generate_nickname():
    nicknames = ["Кибервоин", "Тёмный лорд", "Светлый ангел"]
    return f"👤 Никнейм: {random.choice(nicknames)}"

def generate_recipe():
    recipes = ["Спагетти карбонара", "Пельмени", "Борщ"]
    return f"🍲 Рецепт: {random.choice(recipes)}"

def generate_route():
    routes = ["Москва → Санкт-Петербург", "Казань → Екатеринбург", "Новосибирск → Владивосток"]
    return f"🗺️ Маршрут: {random.choice(routes)}"

def generate_fact():
    facts = ["Земля — третья планета от Солнца.", "Венера — самая горячая планета в Солнечной системе."]
    return f"📚 Факт: {random.choice(facts)}"

def generate_personality():
    traits = ["Экстраверт", "Интроверт", "Амбиверт"]
    hobbies = ["Спорт", "Музыка", "Кино", "Книги", "Путешествия"]
    return f"🧠 Личность: {random.choice(traits)}, Увлечения: {random.choice(hobbies)}"

def generate_car():
    brands = ["Toyota", "BMW", "Audi", "Mercedes", "Ford"]
    models = ["Corolla", "X5", "A4", "C-Class", "Mustang"]
    return f"🚗 Автомобиль: {random.choice(brands)} {random.choice(models)}"

def generate_pet():
    pets = ["Собака", "Кошка", "Попугай", "Хомяк", "Рыбка"]
    names = ["Бобик", "Мурзик", "Кеша", "Хома", "Немо"]
    return f"🐾 Домашнее животное: {random.choice(pets)}, Имя: {random.choice(names)}"

def generate_job():
    jobs = ["Программист", "Врач", "Учитель", "Инженер", "Дизайнер"]
    companies = ["Google", "Яндекс", "Microsoft", "Сбербанк", "Ростех"]
    return f"💼 Работа: {random.choice(jobs)}, Компания: {random.choice(companies)}"

def generate_university():
    universities = ["МГУ", "СПбГУ", "МФТИ", "ВШЭ", "МГТУ"]
    faculties = ["Факультет информатики", "Факультет экономики", "Факультет медицины", "Факультет инженерии", "Факультет дизайна"]
    return f"🎓 Университет: {random.choice(universities)}, Факультет: {random.choice(faculties)}"

def generate_country():
    countries = ["Россия", "США", "Германия", "Китай", "Япония"]
    capitals = ["Москва", "Вашингтон", "Берлин", "Пекин", "Токио"]
    return f"🌍 Страна: {random.choice(countries)}, Столица: {random.choice(capitals)}"

def generate_city():
    cities = ["Москва", "Нью-Йорк", "Берлин", "Пекин", "Токио"]
    populations = ["12 млн", "8 млн", "3 млн", "21 млн", "13 млн"]
    return f"🏙️ Город: {random.choice(cities)}, Население: {random.choice(populations)}"

def generate_language():
    languages = ["Русский", "Английский", "Немецкий", "Китайский", "Японский"]
    levels = ["Начальный", "Средний", "Продвинутый"]
    return f"🗣️ Язык: {random.choice(languages)}, Уровень: {random.choice(levels)}"

def generate_hobby():
    hobbies = ["Спорт", "Музыка", "Кино", "Книги", "Путешествия"]
    return f"🎭 Хобби: {random.choice(hobbies)}"

def generate_food():
    foods = ["Пицца", "Суши", "Бургер", "Паста", "Салат"]
    return f"🍕 Еда: {random.choice(foods)}"

def generate_drink():
    drinks = ["Кофе", "Чай", "Сок", "Вода", "Кола"]
    return f"🍹 Напиток: {random.choice(drinks)}"

def generate_movie():
    movies = ["Матрица", "Властелин колец", "Звёздные войны", "Гарри Поттер", "Пираты Карибского моря"]
    return f"🎬 Фильм: {random.choice(movies)}"

def generate_book():
    books = ["1984", "Мастер и Маргарита", "Война и мир", "Гарри Поттер", "Маленький принц"]
    return f"📚 Книга: {random.choice(books)}"

def generate_music():
    genres = ["Рок", "Поп", "Джаз", "Классика", "Хип-хоп"]
    return f"🎵 Музыка: {random.choice(genres)}"

def generate_sport():
    sports = ["Футбол", "Баскетбол", "Теннис", "Плавание", "Бег"]
    return f"⚽ Спорт: {random.choice(sports)}"

def generate_game():
    games = ["Dota 2", "CS:GO", "Minecraft", "Fortnite", "The Witcher 3"]
    return f"🎮 Игра: {random.choice(games)}"

def generate_website():
    websites = ["Google", "YouTube", "Facebook", "Twitter", "Instagram"]
    return f"🌐 Сайт: {random.choice(websites)}"

def generate_app():
    apps = ["Telegram", "WhatsApp", "Instagram", "YouTube", "Spotify"]
    return f"📱 Приложение: {random.choice(apps)}"

def generate_os():
    os_list = ["Windows", "macOS", "Linux", "Android", "iOS"]
    return f"💻 ОС: {random.choice(os_list)}"

def generate_programming_language():
    languages = ["Python", "Java", "C++", "JavaScript", "Go"]
    return f"💻 Язык программирования: {random.choice(languages)}"

def generate_currency():
    currencies = ["Рубль", "Доллар", "Евро", "Фунт", "Йена"]
    return f"💰 Валюта: {random.choice(currencies)}"

def generate_stock():
    stocks = ["Apple", "Google", "Tesla", "Amazon", "Microsoft"]
    return f"📈 Акция: {random.choice(stocks)}"

def generate_crypto():
    cryptos = ["Bitcoin", "Ethereum", "Litecoin", "Ripple", "Dogecoin"]
    return f"💰 Криптовалюта: {random.choice(cryptos)}"

def generate_weather():
    weathers = ["Солнечно", "Дождь", "Снег", "Облачно", "Туман"]
    return f"🌤️ Погода: {random.choice(weathers)}"

def generate_season():
    seasons = ["Зима", "Весна", "Лето", "Осень"]
    return f"🍂 Сезон: {random.choice(seasons)}"

def generate_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    return f"⏰ Время: {hour:02d}:{minute:02d}"

def generate_emoji():
    emojis = ["😀", "😎", "🤔", "😍", "🤯"]
    return f"😀 Эмодзи: {random.choice(emojis)}"

def generate_hashtag():
    hashtags = ["#любовь", "#жизнь", "#путешествия", "#еда", "#спорт"]
    return f"#️⃣ Хэштег: {random.choice(hashtags)}"

def generate_quote_of_the_day():
    quotes = ["Всё, что не убивает, делает нас сильнее.", "Дорогу осилит идущий.", "Жизнь — это то, что происходит, пока ты строишь планы."]
    return f"📜 Цитата дня: {random.choice(quotes)}"

def generate_fact_of_the_day():
    facts = ["Земля — третья планета от Солнца.", "Венера — самая горячая планета в Солнечной системе.", "Самая длинная река в мире — Амазонка."]
    return f"📚 Факт дня: {random.choice(facts)}"

def generate_joke_of_the_day():
    jokes = ["Почему программисты любят тёмный режим? Потому что свет притягивает баги!", "Какой язык программирования самый крутой? Тот, на котором ты пишешь!"]
    return f"😂 Шутка дня: {random.choice(jokes)}"

def generate_tip_of_the_day():
    tips = ["Пейте больше воды.", "Регулярно делайте перерывы в работе.", "Не забывайте про физическую активность."]
    return f"💡 Совет дня: {random.choice(tips)}"

# Обработчики команд
def start(update: Update, context: CallbackContext):
    keyboard = [
        ["👤 Имя", "📄 Паспорт", "📱 Телефон"],
        ["🏠 Адрес", "💳 Карта", "🏢 Компания"],
        ["💡 Бизнес-идея", "📝 ИНН", "📝 СНИЛС"],
        ["🏦 Расчётный счёт", "🏦 БИК", "📝 КПП"],
        ["📝 ОКПО", "📝 ОГРН", "📝 ОКТМО"],
        ["📝 ОКВЭД", "📧 Email", "🔑 Пароль"],
        ["🔢 Число", "📜 Текст", "😂 Мем"],
        ["🎨 Цвета", "📲 QR-код", "📅 Дата"],
        ["🧮 Задача", "😂 Шутка", "📜 Цитата"],
        ["📝 Список дел", "👤 Никнейм", "🍲 Рецепт"],
        ["🗺️ Маршрут", "📚 Факт", "🧠 Личность"],
        ["🚗 Автомобиль", "🐾 Домашнее животное", "💼 Работа"],
        ["🎓 Университет", "🌍 Страна", "🏙️ Город"],
        ["🗣️ Язык", "🎭 Хобби", "🍕 Еда"],
        ["🍹 Напиток", "🎬 Фильм", "📚 Книга"],
        ["🎵 Музыка", "⚽ Спорт", "🎮 Игра"],
        ["🌐 Сайт", "📱 Приложение", "💻 ОС"],
        ["💻 Язык программирования", "💰 Валюта", "📈 Акция"],
        ["💰 Криптовалюта", "🌤️ Погода", "🍂 Сезон"],
        ["⏰ Время", "😀 Эмодзи", "#️⃣ Хэштег"],
        ["📜 Цитата дня", "📚 Факт дня", "😂 Шутка дня"],
        ["💡 Совет дня"]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    update.message.reply_text("Выбери генератор:", reply_markup=reply_markup)

def handle_message(update: Update, context: CallbackContext):
    text = update.message.text
    if text == "👤 Имя":
        update.message.reply_text(generate_russian_name())
    elif text == "📄 Паспорт":
        update.message.reply_text(generate_passport())
    elif text == "📱 Телефон":
        update.message.reply_text(generate_phone())
    elif text == "🏠 Адрес":
        update.message.reply_text(generate_address())
    elif text == "💳 Карта":
        update.message.reply_text(generate_credit_card())
    elif text == "🏢 Компания":
        update.message.reply_text(generate_company())
    elif text == "💡 Бизнес-идея":
        update.message.reply_text(generate_business())
    elif text == "📝 ИНН":
        update.message.reply_text(generate_inn())
    elif text == "📝 СНИЛС":
        update.message.reply_text(generate_snils())
    elif text == "🏦 Расчётный счёт":
        update.message.reply_text(generate_bank_account())
    elif text == "🏦 БИК":
        update.message.reply_text(generate_bic())
    elif text == "📝 КПП":
        update.message.reply_text(generate_kpp())
    elif text == "📝 ОКПО":
        update.message.reply_text(generate_okpo())
    elif text == "📝 ОГРН":
        update.message.reply_text(generate_ogrn())
    elif text == "📝 ОКТМО":
        update.message.reply_text(generate_oktmo())
    elif text == "📝 ОКВЭД":
        update.message.reply_text(generate_okved())
    elif text == "📧 Email":
        update.message.reply_text(generate_email())
    elif text == "🔑 Пароль":
        update.message.reply_text(generate_password())
    elif text == "🔢 Число":
        update.message.reply_text(generate_random_number())
    elif text == "📜 Текст":
        update.message.reply_text(generate_lorem_ipsum())
    elif text == "😂 Мем":
        update.message.reply_text(generate_meme())
    elif text == "🎨 Цвета":
        update.message.reply_text(generate_color_palette())
    elif text == "📲 QR-код":
        update.message.reply_text(generate_qr_code_data())
    elif text == "📅 Дата":
        update.message.reply_text(generate_date())
    elif text == "🧮 Задача":
        update.message.reply_text(generate_math_problem())
    elif text == "😂 Шутка":
        update.message.reply_text(generate_joke())
    elif text == "📜 Цитата":
        update.message.reply_text(generate_quote())
    elif text == "📝 Список дел":
        update.message.reply_text(generate_to_do_list())
    elif text == "👤 Никнейм":
        update.message.reply_text(generate_nickname())
    elif text == "🍲 Рецепт":
        update.message.reply_text(generate_recipe())
    elif text == "🗺️ Маршрут":
        update.message.reply_text(generate_route())
    elif text == "📚 Факт":
        update.message.reply_text(generate_fact())
    elif text == "🧠 Личность":
        update.message.reply_text(generate_personality())
    elif text == "🚗 Автомобиль":
        update.message.reply_text(generate_car())
    elif text == "🐾 Домашнее животное":
        update.message.reply_text(generate_pet())
    elif text == "💼 Работа":
        update.message.reply_text(generate_job())
    elif text == "🎓 Университет":
        update.message.reply_text(generate_university())
    elif text == "🌍 Страна":
        update.message.reply_text(generate_country())
    elif text == "🏙️ Город":
        update.message.reply_text(generate_city())
    elif text == "🗣️ Язык":
        update.message.reply_text(generate_language())
    elif text == "🎭 Хобби":
        update.message.reply_text(generate_hobby())
    elif text == "🍕 Еда":
        update.message.reply_text(generate_food())
    elif text == "🍹 Напиток":
        update.message.reply_text(generate_drink())
    elif text == "🎬 Фильм":
        update.message.reply_text(generate_movie())
    elif text == "📚 Книга":
        update.message.reply_text(generate_book())
    elif text == "🎵 Музыка":
        update.message.reply_text(generate_music())
    elif text == "⚽ Спорт":
        update.message.reply_text(generate_sport())
    elif text == "🎮 Игра":
        update.message.reply_text(generate_game())
    elif text == "🌐 Сайт":
        update.message.reply_text(generate_website())
    elif text == "📱 Приложение":
        update.message.reply_text(generate_app())
    elif text == "💻 ОС":
        update.message.reply_text(generate_os())
    elif text == "💻 Язык программирования":
        update.message.reply_text(generate_programming_language())
    elif text == "💰 Валюта":
        update.message.reply_text(generate_currency())
    elif text == "📈 Акция":
        update.message.reply_text(generate_stock())
    elif text == "💰 Криптовалюта":
        update.message.reply_text(generate_crypto())
    elif text == "🌤️ Погода":
        update.message.reply_text(generate_weather())
    elif text == "🍂 Сезон":
        update.message.reply_text(generate_season())
    elif text == "⏰ Время":
        update.message.reply_text(generate_time())
    elif text == "😀 Эмодзи":
        update.message.reply_text(generate_emoji())
    elif text == "#️⃣ Хэштег":
        update.message.reply_text(generate_hashtag())
    elif text == "📜 Цитата дня":
        update.message.reply_text(generate_quote_of_the_day())
    elif text == "📚 Факт дня":
        update.message.reply_text(generate_fact_of_the_day())
    elif text == "😂 Шутка дня":
        update.message.reply_text(generate_joke_of_the_day())
    elif text == "💡 Совет дня":
        update.message.reply_text(generate_tip_of_the_day())
    else:
        update.message.reply_text("Неизвестная команда. Выбери генератор из меню.")

# Запуск бота
def main():
    token = "8029071480:AAHNH8DFZhcMXQshb5D7mLMyKYY5OfxQiyQ"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
