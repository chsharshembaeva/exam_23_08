from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    month_to_learn = models.IntegerField()

    def save(self, *args, **kwargs):
        if self.name.islower():
            self.name == self.name.title()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class AbstractPerson(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if self.phone_number[0] == '0':
            self.phone_number = '+996' + self.phone_number[1:]
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Mentor(AbstractPerson):
    main_work = models.CharField(max_length=100)
    experience = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.main_work}'


class Student(AbstractPerson):
    work_study_place = models.CharField(max_length=100, null=True, blank=True)
    has_own_notebook = models.BooleanField()
    os_choices = [('windows', 'Windows'), ('macos', 'MacOS'), ('linux', 'Linux'),]
    preferred_os = models.CharField(max_length=100, choices=os_choices)
    student_men = models.ManyToManyField(Mentor, through='Course')

    def __str__(self):
        return f'{self.name} - {self.work_study_place}'


class Course(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    date_started = models.DateField()
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} - {self.language} - {self.date_started}'














