import sqlite3

connection = sqlite3.connect("fees.db")
cursor = connection.cursor()

cursor.execute("CREATE TABLE fee(Student_Adm_no string, Student_first_name text, Student_second_name text, Fee_balance integer)")

students = [
    ('CA112', "Ben", "Willys", 12000),
    ('W001T', "Okoth", "Francis", 5500),
    ('RT780', "Harry", "Mbugua", 17850),
    ('Q134H', "Harriet", "Kamau", 13007),
    ('C0771', "Lydia", "Moraa", 40000),
    ('D0034', "Shimaka", "Mary", 27000),
]

cursor.executemany("INSERT INTO fee VALUES(?,?,?,?)", students)

#Print records
for i in cursor.execute("SELECT * FROM fee WHERE Fee_balance <= 10000"):
    print(i)

# seperator 1
print("*********************")

# selecting specific record to print
cursor.execute("SELECT * FROM fee WHERE Student_second_name='Mary'")
student_search = cursor.fetchall()
print(student_search)

connection.close()