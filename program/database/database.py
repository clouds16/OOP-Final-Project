from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload


#engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine('sqlite:///./newdb.db', echo=True)
Base = declarative_base()




class Address(Base):
    __tablename__ = 'addresses'
    
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", backref=backref('addresses'))

    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address


Base.metadata.create_all(engine) 
Session = sessionmaker(bind=engine)
session = Session()


#Create an user
# def main():
#     Session = sessionmaker(bind=engine)
#     session = Session()

#     ed_user = User(name='Hector', fullname='Hector Alvarez', password='hekspw')
#     ed_user.addresses = [Address(email_address='hekthekt@google.com'), Address(email_address='otherhekt@yahoo.com')]

#     session.add(ed_user)
#     session.commit()

# ####### find user that we have just added 
#     print()
#     print()
#     print("###############################   Start of program ###################################")
#     user_by_email = session.query(User)\
#     .filter(Address.email_address=='hekthekt@google.com')\
#     .first()

#     print(user_by_email)
#     print(user_by_email.addresses)

#     print()
#     print()
#     print("#############################   Second Query ###################################")
#     user_by_email = session.query(User)\
#     .filter(Address.email_address=='otherhekt@yahoo.com')\
#     .options(joinedload(User.addresses))\
#     .first()

#     print(user_by_email)
#     print(user_by_email.addresses)


# if __name__ == "__main__":
    # main()