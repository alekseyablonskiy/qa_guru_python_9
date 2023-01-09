import datetime
from dataclasses import dataclass
from datetime import date
from enum import Enum
from typing import Literal, List


@dataclass
class User:
    first_name: str
    last_name: str
    email: str
    phone: str
    address: str
    birthday: datetime.date
    gender: str
    subject: str
    hobbies: str
    image: str
    state: str
    city: str


aleksey = User(
    first_name='Aleksey',
    last_name='Yablonskiy',
    email='alekseyablonskiy@gmail.com',
    phone='1234567890',
    address='Minsk',
    birthday=date(1996, 10, 27),
    gender='Male',
    subject='Computer Science',
    hobbies='Music',
    image='picture.jpg',
    state='NCR',
    city='Delhi')
