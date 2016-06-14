import peewee

my_models_db = peewee.SqliteDatabase('my_models.db', pragmas=(('foreign_keys', True),))

class BaseModel(peewee.Model):
    id = peewee.PrimaryKeyField(primary_key=True, unique=True)

    class Meta:
        database = my_models_db
        order_by = ('id',)

class School(BaseModel):
    name = peewee.FixedCharField(max_length=128)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

class Batch(BaseModel):
    school = peewee.ForeignKeyField(School, related_name="batches", on_delete="cascade")
    name = peewee.FixedCharField(max_length=128)

    def __str__(self):
        return self.name + " (" + str(self.id) + ")"

class User(BaseModel):
    first_name = peewee.FixedCharField(max_length=128, default="")
    last_name = peewee.FixedCharField(max_length=128)
    age = peewee.IntegerField()

    def __str__(self):
        print self.first_name, self.last_name, self.id

class Student(User):
    batch = peewee.ForeignKeyField(Batch, related_name="students", on_delete="cascade")

    def __str__(self):
        return "" + self.first_name + " " + self.last_name + " (" + str(self.id) + ") " + "part of batch: " + str(self.batch)

class Exercise(BaseModel):
    SUBJECTS = [('math', "Math"),
                ('english', "English"),
                ('history', "History"),
                ('c_prog', "C prog"),
                ('swift_prog', "Swift prog")]

    student = peewee.ForeignKeyField(Student, related_name="exercises", on_delete="cascade")
    subject = peewee.FixedCharField(max_length=128)
    note = peewee.IntegerField(default = 0)
    
    def __str__(self):
        return "Exercise: " + str(self.student) + " has " + str(self.note) + " in " + str(self.subject) + " (" + str(self.id) + ")"
