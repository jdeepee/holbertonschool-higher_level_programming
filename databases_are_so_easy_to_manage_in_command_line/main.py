from sys import argv
from models import *

def create_tables():
    my_models_db.connect()
    my_models_db.create_tables([School, Batch, User, Student, Exercise])

def print_table():
    if len(argv) == 3:
        if argv[2] == "school":
            results = School.select()

            for row in results:
                print row

        elif argv[2] == "batch":
            results = Batch.select()

            for row in results:
                print row

        elif argv[2] == "user":
            results = User.select()

            for row in results:
                print row

        elif argv[2] == "student":
            results = Student.select()

            for row in results:
                print row

        elif argv[2] == "exercise":
            results = Exercise.select()

            for row in results:
                print row

def insert_record():
	with my_models_db.transaction():
		if argv[2] == "school":
			insert = School.create(name=argv[3])

			print "insert school: " + str(insert)

		elif argv[2] == "batch":
			insert = Batch.create(
						school=argv[3],
						name=argv[4],
						)

			print "insert batch: " + str(insert)

		elif argv[2] == "student":
			if len(argv) == 7:
				insert = Student.create(
							batch=int(argv[3]),
							age=int(argv[4]),
							last_name=argv[5],
							first_name=argv[6],
							)

			else:
				insert = Student.create(
							batch=int(argv[3]),
							age=int(argv[4]),
							last_name=argv[5],
							)

			print "insert student: " + str(insert)

		elif argv[2] == "exercise":
			new = Exercise.create(
				student = int(argv[3]),
				subject = argv[4],
				note = int(argv[5]),
			)

			print "New exercise: " + str(new)

def delete_tables():
    if argv[2] == "school":
        query = School.select().where(Schools.id == argv[3])

        if query.exists():
            result = query.get()
            School.delete().where(School.id == argv[3]).execute()
            print "Delete: " + str(result)

        else:
            print "Nothing to delete"

    elif argv[2] == "batch":
        query = Batch.select().where(Batch.id == argv[3])

        if query.exists():
            result = query.get()
            Batch.delete().where(Batch.id == argv[3]).execute()

            print "Delete: " + str(result)

        else:
            print "Nothing to delete"

    elif argv[2] == "student":
        query = Student.select().where(Student.id == argv[3])

        if query.exists():
            result = query.get()
            Student.delete().where(Student.id == argv[3]).execute()
            print "Delete: " + str(result)

        else:
            print "Nothing to delete"

    elif argv[2] == "exercise":
        query = Exercise.select().where(Exercise.id == argv[3])

        if query.exists():
            target = query.get()
            Exercise.delete().where(Exercise.id == argv[3]).execute()
            print "Delete: " + str(target)

        else:
        	print "Nothing to delete"

def print_batch_by_school():
    query = (School.select().where(School.id == argv[2]))

    if query.exists():
        results = (Batch.select().where(Batch.school == argv[2]))

        for batch in results:
            print batch

    else:
        print "School not found"

def print_student_by_batch():
    query = (Batch.select().where(Batch.id == argv[2]))

    if query.exists():
        results = (Student.select().where(Student.batch == argv[2]))

        for student in results:
            print student

    else:
        print "Batch not found"

def print_student_by_school():
    query = (School.select().where(School.id == argv[2]))

    if query.exists():
        results = (Student.select().join(Batch).where(Batch.school == argv[2]))

        for student in results:
            print student
    else:
        print "School not found"

def print_family():
    query = (Student.select().where(Student.last_name == argv[2]))

    for student in query:
        print student

def age_average():
    if len(argv) == 3:
        query = (Student.select(peewee.fn.Avg(Student.age).alias('age_avg')).where(Student.batch == argv[2])).get()

        print query.age_avg

    else:
        query = (Student.select(peewee.fn.Avg(Student.age).alias('age_avg'))).get()

        print query.age_avg

def change_batch():
    student = (Student.select().where(Student.id == argv[2]))
    batch = (Batch.select().where(Batch.id == argv[3]))

    if student.exists():
        student = student.get()

        if batch.exists():
            batch = batch.get()
            print student.batch.id

            if student.batch != batch:
                student.batch = batch
                student.save()

                print str(student) + " has been moved to " + str(batch)

            else:
                print str(student) + " already in " + str(batch)
        else:
            print "Batch not found"
    else:
        print "Student not found"

def print_all():
    schools = School.select()
    batches = (Batch.select().join(School))
    students = (Student.select().join(Batch))
    exercises = (Exercise.select().join(Student))

    for school in schools:
        print school
        school_batches = batches.where(School.id == school.id)

        for batch in school_batches:
            print '\t' + str(batch)
            batch_students = students.where(Batch.id == batch.id)

            for student in batch_students:
                print '\t\t' + str(student)
                student_exercises = exercises.where(Student.id == student.id)

                for exercise in student_exercises:
                    print '\t\t\t' + str(exercise)

def note_average_by_student():
    query = (Student.select().where(Student.id == argv[2]))

    if query.exists():
        averages = (Exercise.select(Exercise.subject, peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).group_by(Exercise.subject).where(Exercise.student == argv[2]))

        for average in averages:
            print average.subject + ": " + str(average.note_avg)
    else:
        print "Student not found"

def note_average_by_batch():
    query = (Batch.select().where(Batch.id == argv[2]))

    if query.exists():
        averages = (Exercise.select(Exercise.subject,peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).group_by(Exercise.subject).where(Student.batch == argv[2]))

        for average in averages:
            print average.subject + ": " + str(average.note_avg)
    else:
        print "Batch not found"

def note_average_by_school():
    query = (School.select().where(School.id == argv[2]))

    if query.exists():
        averages = (Exercise.select(Exercise.subject.alias('subject'), peewee.fn.Avg(Exercise.note).coerce(False).alias('note_total')).join(Student).join(Batch).group_by(Exercise.subject).where(Batch.school == argv[2]))

        for average in averages:
            print average.subject + ": " + str(average.note_total)
    else:
        print "School not found"

def top_batch():
    query = (Batch.select().where(Batch.id == argv[2]))

    if query.exists():
        if len(argv) == 4:
            averages = (Exercise.select(Exercise.subject,Exercise.student,peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).group_by(Exercise.subject, Exercise.student).where(Exercise.subject == argv[3],Student.batch == argv[2]).order_by(peewee.fn.Avg(Exercise.note).desc()))

            print str(averages[0].student)

        elif len(argv) == 3:
            averages = (Exercise.select(Exercise.student,peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).group_by(Exercise.student).order_by(peewee.fn.Avg(Exercise.note).desc()))

            print str(averages[0].student)
    else:
        print "Batch not found"

def top_school():
    query = (School.select().where(School.id == argv[2]))

    if query.exists():
        if len(argv) == 4:
            averages = (Exercise.select(Exercise.subject,Exercise.student,peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).join(Batch).group_by(Exercise.subject, Exercise.student).where(Exercise.subject == argv[3],Batch.school == argv[2]).order_by(peewee.fn.Avg(Exercise.note).desc()))

            print str(averages[0].student)
        elif len(argv) == 3:
            averages = (Exercise.select(Exercise.subject,Exercise.student,peewee.fn.Avg(Exercise.note).coerce(False).alias('note_avg')).join(Student).join(Batch).where(Batch.school == argv[2]).group_by(Exercise.student).order_by(peewee.fn.Avg(Exercise.note).desc()))

            if averages.exists():
                print str(averages[0].student)
    else:
        print "Batch not found"

if len(argv) < 2:
    print "Please enter an action"
elif argv[1] == "create":
    create_tables()
elif argv[1] == "print":
    print_table()
elif argv[1] == "insert":
    insert_record()
elif argv[1] == "delete":
    delete_tables()
elif argv[1] == "print_batch_by_school":
    print_batch_by_school()
elif argv[1] == "print_student_by_batch":
    print_student_by_batch()
elif argv[1] == "print_student_by_school":
    print_student_by_school()
elif argv[1] == "print_family":
    print_family()
elif argv[1] == "age_average":
    age_average()
elif argv[1] == "change_batch":
    change_batch()
elif argv[1] == "print_all":
    print_all()
else:
    print "Undefined action " + argv[1]

