from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

engine = create_engine("sqlite:///:memory:", echo=False)#True щоб все бачити!!!!
DBSession = sessionmaker(bind=engine)
session = DBSession()

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)


class Address(Base):
    __tablename__ ='addresses'
    id = Column(Integer, primary_key=True)
    user_email = Column('email', String(150), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User) #звязок для алхемі


Base.metadata.create_all(engine)


if __name__ == '__main__':
    new_user = User(fullname='Mykola Gryshyn')
    session.add(new_user)
    # new_address = Address(user_email='mykola@i.ua', user_id =new_user.id)
    new_address = Address(user_email='mykola@i.ua', user=new_user)
    session.add(new_address)
    session.commit()

    u = session.query(User).first()
    print(u.id, u.fullname)

    adrs = session.query(Address).join(Address.user).all()
    print(adrs)
    for a in adrs:
        print(a.id, a.user_email, a.user.fullname)

    session.close()