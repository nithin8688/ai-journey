import psycopg2

def get_connection():
    return psycopg2.connect(
            host="localhost",
            database="ai_journey1",
            user="postgres",
            password="postgres",
            port=5432
        )

def rows_to_dicts(cursor, rows):
    columns = [desc[0] for desc in cursor.description]
    return [dict(zip(columns, row)) for row in rows]

def row_to_dict(cursor, row):
    if row is None:
        return None
    columns = [desc[0] for desc in cursor.description]
    return dict(zip(columns,row))

def add_student(name, marks, subject):
    conn = get_connection()
    cursor = conn.cursor() 
    cursor.execute("INSERT INTO students (name, marks, subject, passed) VALUES (%s, %s, %s, %s) RETURNING id, name, marks, subject, passed",
                   (name, marks, subject, marks>=75))
    new_student = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return new_student 

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, marks, subject, passed FROM students")
    rows = cursor.fetchall()
    result = rows_to_dicts(cursor, rows)
    cursor.close()
    conn.close()
    return result 
         

def get_student_by_id(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, marks, subject, passed FROM students WHERE id=%s",(student_id,))
    row = cursor.fetchone()
    result = row_to_dict(cursor, row)
    cursor.close()
    conn.close()
    return result

def update_student_marks(student_id, new_marks):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE students SET marks=%s, passed=%s WHERE id=%s",
                   (new_marks, new_marks>=75, student_id))
    conn.commit()
    cursor.close()
    conn.close() 

def delete_student(names):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE name=%s RETURNING id, name, marks, subject, passed",(names,))
    deleted = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return deleted 


# s1 = add_student("Sai", 76, "Math")
# s2 = add_student("Murali", 55, "Math")
# s3 = add_student("Likki", 93, "Math")
# print("Added students to database",s1,s2,s3)

# all_students = get_all_students()
# print("All Students: ", all_students)

student = get_student_by_id(25)
print("Student 1:", student)

print(student["name"])

update_student_marks(3, 75)
print("Updated student:", get_student_by_id(3))

deleted = delete_student('Likki')
print("deleted student", deleted)
all_students = get_all_students()
for s in all_students:
    print(f"{s['name']} scored {s['marks']} in {s['subject']}")