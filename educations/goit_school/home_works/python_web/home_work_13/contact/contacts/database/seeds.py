from faker import Faker

from models import Contact
from db import SessionLocal


fake = Faker('en-US')
count_contacts = 10


def create_contacts():
    db = SessionLocal()
    for _ in range(count_contacts):
        contact = Contact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            phone=fake.unique.numerify('+38(0##)###-##-##'),
            birthday=fake.date(),
            information=fake.job()
        )
        db.add(contact)
    db.commit()


if __name__ == '__main__':
    create_contacts()
    print('Success inserting data to database')