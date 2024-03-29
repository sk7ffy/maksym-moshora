import sqlite3

db_name = 'db.sqlite'

conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()


def do(query):
    cursor.execute(query)
    conn.commit()


def create_tables():
    open()


    do('''CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY ,
        name VARCHAR )
        ''')
    
    


    do('''CREATE TABLE IF NOT EXISTS news (
              id INTEGER PRIMARY KEY,
              title VARCHAR,
              description VARCHAR,
              image VARCHAR,
              class_id VARCHAR,
              video_url VARCHAR
            
            
                
        
        
       )
    ''')
    close()


def drop_table():
    open()
    do('DROP TABLE IF EXISTS news')
    do('DROP TABLE IF EXISTS categories')
    close()


def show_tables():
    open()
    
    
    cursor.execute('''SELECT * FROM categories''')
    print(cursor.fetchall())

    cursor.execute('''SELECT * FROM news''')
    print(cursor.fetchall())
    close()

def get_all_news():
    open()
    cursor.execute(''' SELECT * FROM news
                   
                ''')
    return cursor.fetchall()

def get_news_by_id(id):
    open()
    cursor.execute('''SELECT * FROM news
                   WHERE id = (?)
                ''', [id])
    return cursor.fetchone()

def add_news(title, description, image, class_id,video_url):
    open()
    cursor.execute('''INSERT INTO news 
                   (title, description, image, class_id,video_url ) 
                   VALUES (?, ?, ?, ?,?)''', [title, description, image, class_id,video_url ])
    conn.commit()
    close()

def add_category(name):
    open()
    cursor.execute('''INSERT INTO categories 
                   (name ) 
                   VALUES (?)''', [name])
    conn.commit()
    close()

#show_tables()

#drop_table()
#create_tables()
 

#add_category("sport")
    
#add_news('BMW XM', 'BMW XM (G09) — люксовий кросовер (SUV), що дебютував 27 вересня 2022 року. Зовні автомобіль подібний на концепт-кар BMW Concept XM 2021 року. Старт серійного виробництва ХМ заплановано на кінець 2022 року на заводі BMW у Спартанбурзі, Південна Кароліна. Старт продажів очікується на початку 2023 року.', 'https://nextcar.ua/images/blog/527/bmw-xm__10_.jpg',1,'https://www.youtube.com/embed/PjngNGfmOaE')
#add_news('BMW M3 G80', 'BMW M3 — високотехнологічна версія автомобілів середнього класу BMW 3 серії від BMW M GmbH. Моделі M3 зроблені на базі E30, E36, E46, E90/E92/E93, F30 та G20 3-ї серії. Основні відмінності від «стандартних» автомобілів 3 серії включають потужніший двигун, поліпшена підвіска, агресивніший і аеродинамічний кузов, множинні акценти, як в інтер"єрі так і в екстер"єрі на приналежність до лінійки «M» / Motorsport.', 'https://s.auto.drom.ru/i24275/c/photos/fullsize/bmw/m3/bmw_m3_1099869.jpg',2,'https://www.youtube.com/embed/XddW1bpdGWY')
#add_news('BMW M5 F10', 'F10 BMW M5 являє собою спортивний автомобіль виробництва німецької фірми BMWЦей новий M5 є новим лідером 5-ї серії. Відповідно до політики скорочення габаритів, що проводиться в даний час BMW, у цьому новому поколінні, званому версією седана F10, замість V10 замінюється V8 Перший – це «класичний» М5. Він був випущений у 2011 році. Він відчиняє новий двигун. Він відмовляється від свого атмосферного V10 на твін-турбо V8 у логіці зменшення габаритів. Він також вибирає систему зупинки/запуску, яка автоматично відключає та перезапускає двигун.Другий – «змагальний пакет».Він зявився під час рестайлінгу M5, що експлуатується у 2013 році. Він хоче скласти конкуренцію Mercedes E63 AMG S-4MATIC потужністю 585 л.Останнє - "30 jahre" (30 років по-французьки). Він був створений на честь 30-річчя серії 5. Він містить ті ж елементи, що й набір змагань. Він обмежений тиражем 300 екземплярів. ', 'https://s.auto.drom.ru/i24196/c/photos/fullsize/bmw/m5/bmw_m5_477550.jpg',2,'https://www.youtube.com/embed/HWdVn27j_gI')
#add_news('BMW M5 F90', 'BMW M5 (БМВ М5) – повнопривідний седан класу «E», індекс моделі – F90. Шосте покоління моделі стало першим в історії М5, на якому реалізовано систему повного приводу. Офіційна презентація автомобіля відбулася на Франкфуртському автосалоні у вересні 2017 року.Говорячи про пяту серію BMW із шильдиком «М», потрібно починати з продуктивності моделі. Це  її надбання, і тут є чим пишатися. Двигун F90 – це 4.4-літровий V8 з двома турбінами. Порівняно з попередньою версією (а мотор залишився колишнім) віддача зросла за рахунок збільшення тиску впорскування палива, інших турбокомпресорів та деяких інших змін. У результаті – 600 л. с. і 750 Нм крутного моменту, який, що важливо, доступний вже з 1800 об/хв. І якщо мова вже пішла про цифри, то у М5 головними є 3.4 с до першої «сотні» і 11.1 с до 200 км/год! ', 'https://i.infocar.ua/i/2/5388/98757/1400x.jpg',2,'https://www.youtube.com/embed/kxK5xSZXX6w')
#add_news('Mercedes G63(G-class)', 'Mercedes-Benz G-клас, що іноді називається G-Wagen (G - скор. від ньому. Geländewagen - [ɡəˈlɛːndəvaːɡn], «позашляховик») - серія повнорозмірних люксових позашляховиків (автомобілів підвищеної прохідності), вироблених в Австрії [2] (раніше Steyr-Daimler-Puch[3]) і продаваних під торговою маркою Mercedes-Benz. Випускається з 1979 року до теперішнього часу.G-клас був розроблений в якості військового транспортного засобу на пропозицію іранського шаха Мохаммеда Реза Пехлеві [1] [3] [4], що в той час був акціонером компанії Mercedes-Benz. Цивільна версія автомобіля була представлена ​​у 1979 році.', 'https://images.prismic.io/carwow/d7d113bc-6570-4db2-aa5c-0fbbecb43e90_2021+Mercedes+G-Class+front+quarter+moving+2.jpg',2,'https://www.youtube.com/embed/O_7yRsmf8Q8')
#add_news('Mercedes E63(W213)', 'У листопаді 2016 року компанія Мерседес-Бенц представила на автосалоні в Лос-Анджелесі спортивні модифікації седана W213 від підрозділу Mercedes-AMG. Автомобілі, як і раніше, доступні для покупки в двох модифікаціях: E63 і E63 S. Перший варіант комплектується вдосконаленим 4,0-літровим бітурбірованним бензиновим двигуном V8 потужністю 571 к.с. (420 кВт) і 750 Нм крутного моменту. Версія з приставкою S має підвищену потужністю 612 к.с. (450 кВт) і 850 Нм крутного моменту. Розгін до 100 км/год займає 3,5 секунди для E63 AMG і 3,4 секунди для E63 AMG S. В кузові універсал ці значення рівні 3,6 і 3,5 секунд відповідно. Максимальна швидкість обмежена електронікою на позначці в 250 км/год, але може бути збільшена до 300 км (290 для універсалу) на годину при установці опціонального пакета AMG Driver"s package. В обох версіях двигун працює спільно з дев"ятиступеневою роботизованою коробкою передач AMG Speedshift з мокрим багатодисковим зчепленням замість гідротрансформатора.У червні 2020 року Mercedes-AMG представив оновлені седан та універсал E 63.', 'https://i.pinimg.com/originals/65/9e/c8/659ec8047abee475ef70af0d57511f60.jpg',2,'https://www.youtube.com/embed/HTxvNSUly5k')
#add_news('Audi RS6 Avant','5 грудня 2012 року компанія Audi представила нове покоління моделі RS6 в кузові універсал. Серійне виробництво та продаж почалось у 2013 році. Автомобіль обладнаний TFSI-двигуном V8 об"ємом 4,0 л із двома турбокомпресорами. Номінальна потужність при цьому знизилась на 20 к. с. (560 сил замість колишніх 580), але машина при стартовому прискоренні від нуля до 100 км/год стала на 0,7 с швидшою (3,9 с проти 4,6). Крутний момент зріс до 700 Н·м при 1750—5500 об/хв.Салон Audi RS 6 відповідає параметрам довершеності. Увагу було приділено найдрібнішому шву. Як і очікувалось від автомобіля такого рівня, майже скрізь у салоні зустрічається вуглецеве волокно. Сидіння забезпечують максимальну підтримку. RS 6 має шкіряний інтер"єр та дуже приємні на дотик матеріали оздоблення. Він запропонує чимало простору, тому п"ятеро людей зможуть зручно розміститись. Загалом, RS 6 належить до зовсім іншоїкатегорії автомобілів, яка втілює параметри автомобільної вишуканості. До бази усіх моделей входять: автоматичний клімат-контроль, сучасна аудіо система BOSE, жорстка спортивна підвіска, 18-дюймові литі диски коліс, система антиблокувальних гальм та система розподілу гальмівних зусиль.', 'https://img.tsn.ua/cached/258/tsn-a7bcdedcd32efef57a130292f7597e57/thumbs/1036x648/6b/94/589fe42eca3e67efc277a38d080f946b.jpg',2,'https://www.youtube.com/embed/wCf4U6JZNnE')
#news = get_all_news()
#print(news)
#drop_table()
#show_tables()
    