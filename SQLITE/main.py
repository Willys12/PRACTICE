import sqlite3

connection = sqlite3.connect("Books.db")
cursor = connection.cursor()

cursor.execute("create table books(year_of_publication integer, name_of_book text, author text)")

books_list = [
    (2000, "Across the Bridge", "Chinua Achebe"),
    (2011, "Confessions of economic Hitman", "John Perkins"),
    (2006, "Make your Plans", "Samson Peace"),
    (1990, "Make me a millionaire", "Perris Morgan"),
    (1998, "Business Morning", "Wallace Steve"),
    (2010, "A Trip to Sussex", "Perris Morgan"),
    (2024, "A Poor Nation is Looming", "Perris Morgan")
]

cursor.executemany("insert into books values(?,?,?)", books_list)

#let's print db rows
for row in cursor.execute("select * from Books"):
    print(row)

#separator 1
print("**********************")
#print specific row
cursor.execute("select * from Books where author=:a", {"a": "Perris Morgan"})
book_search = cursor.fetchall()
print(book_search)

#separator 2
print("**********************")

#creating another table
cursor.execute("create table authors(publication_name text, real_name text)")
cursor.execute("insert into authors values(?,?)", ("Perris Morgan", "Stephen Willis"))
cursor.execute("select * from authors where publication_name=:a", {"a": "Perris Morgan"})

name_search = cursor.fetchall()
print(name_search)

#manipulate data in db
print("*******************")
for i in book_search:
    adjusted = [name_search[0][1] if value==name_search[0][0] else value for value in i]
    print(adjusted)

connection.close()