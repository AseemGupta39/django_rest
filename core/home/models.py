from django.db.models import Model,CharField,IntegerField

# Create your models here.
class Student(Model):
    name = CharField(max_length = 100)
    age = IntegerField(default = 18)
    father_name = CharField(max_length = 100)

    def __str__(self) -> str:
        return self.name




