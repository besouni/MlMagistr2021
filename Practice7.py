import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               password="",
                               database="gaumldb")
# print(mydb)
cursor = mydb.cursor();
create_table = "CREATE TABLE users (id INT(11) UNSIGNED AUTO_INCREMENT PRIMARY KEY, " \
               "firstname VARCHAR (50), lastname VARCHAR (50), age INT(3))"
# cursor.execute(create_table)
alter_table = "ALTER TABLE users ADD COLUMN  gender VARCHAR (10)"
# cursor.execute(alter_table)
insert = "INSERT INTO users(firstname, lastname, age, gender) VALUES(%s, %s, %s, %s)"
values = [
            ("Elene", "Sokhadze", 21, "famale"),
            ("Natia", "Chitashvili", 22, "famale")]
# cursor.executemany(insert, values)
# mydb.commit()
# print(cursor.rowcount)

select = "SELECT * FROM users LIMIT 2";
cursor.execute(select)
result = cursor.fetchall()
print(result)
for value in result:
    print(value)

update = "UPDATE users SET firstname=%s WHERE id=%s"
# values2 = ("Rezi", 2)
# cursor.execute(update, values2)
# mydb.commit()


delete = "DELETE FROM users WHERE id=%s"
# values3 = (3,)
# cursor.execute(delete, values3)
# mydb.commit()
