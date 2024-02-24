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
              class_id INTEGER,
                
        FOREIGN KEY (class_id) REFERENCES categories (id)
        
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
    cursor.execute('''SELECT news.id, news.title, news.description, categories.name, news.image
                   FROM news INNER JOIN categories 
                   ON news.class_id == categories.id
                ''')
    return cursor.fetchall()

def get_news_by_id(id):
    open()
    cursor.execute('''SELECT news.title, news.description, categories.name, 
                   FROM news INNER JOIN categories 
                   ON news.class_id == categories.id
                ''', [id])
    return cursor.fetchall()

def add_news(title, description, image, class_id,):
    open()
    cursor.execute('''INSERT INTO news 
                   (title, description, image, class_id ) 
                   VALUES (?, ?, ?, ?)''', [title, description, image, class_id ])
    conn.commit()
    close()

#show_tables()

#drop_table()
create_tables()
 
show_tables()
add_news('12eawd', '123wd', 'https://i.infocar.ua/i/12/6918/1200x800.jpg', '1' )
news = get_all_news()
print(news)
