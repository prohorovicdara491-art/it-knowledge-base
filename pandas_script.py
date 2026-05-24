import pandas as pd
import psycopg2
import matplotlib.pyplot as plt

# Подключение к PostgreSQL
conn = psycopg2.connect(
    dbname='mydb',
    user='myuser',
    password='mypassword',
    host='localhost',
    port='5432'
)

# Загрузка данных, преобразование created_at в naive datetime (без timezone)
df = pd.read_sql('SELECT id, title, created_at FROM myapp_note', conn)
df['created_at'] = pd.to_datetime(df['created_at']).dt.tz_localize(None)

conn.close()

# Вывод данных
print("Данные из таблицы myapp_note:")
print(df)

# Сохранение в CSV
df.to_csv('notes_export.csv', index=False, encoding='utf-8')
print("\n✅ Данные сохранены в notes_export.csv")

# Сохранение в Excel
df.to_excel('notes_export.xlsx', index=False)
print("✅ Данные сохранены в notes_export.xlsx")

# Простой график
if not df.empty:
    df['date'] = df['created_at'].dt.date
    daily_counts = df.groupby('date').size()
    
    plt.figure(figsize=(10, 5))
    daily_counts.plot(kind='bar', color='skyblue')
    plt.title('Количество заметок по дням')
    plt.xlabel('Дата')
    plt.ylabel('Количество заметок')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('notes_chart.png')
    print("✅ График сохранён в notes_chart.png")
else:
    print("⚠️ Нет данных для построения графика.")
