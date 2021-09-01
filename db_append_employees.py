import os
import django
import random
from datetime import date

from faker.providers.person.ru_RU import Provider as Names
from faker.providers.job.ru_RU import Provider as Jobs

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_traffic_light.settings")

django.setup()

from employee.models import Unit, Employee

units_list = [i[0] for i in Unit.objects.values_list('id')]

first_name_list = list(set(Names.first_names_male))
last_name_list = list(set(Names.last_names_male))
middle_name_list = list(set(Names.middle_names_male))
position_list = list(set(Jobs.jobs))


def random_name(name_list: list) -> str:
    return random.choice(name_list)


def random_salary() -> int:
    return random.randint(50000, 200000)


def random_year_date() -> object:
    start_date = date.today().replace(day=1, month=1).toordinal()
    end_date = date.today().toordinal()
    return date.fromordinal(random.randint(start_date, end_date))


for i in range(50000):
    random_user = Employee(first_name=random_name(first_name_list),
                           last_name=random_name(last_name_list),
                           middle_name=random_name(middle_name_list),
                           employment_date=random_year_date(),
                           salary=random_salary(),
                           unit_id=random_name(units_list),
                           position=random_name(position_list))
    random_user.save()
