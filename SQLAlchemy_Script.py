from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()


class User(Base):
    __tablename__ = "users"
    u_id = Column(Integer, primary_key=True)
    u_name = Column(String(50))


engine = create_engine(
    "mysql+pymysql://root:vaishali@localhost/my_first_database"
)

Base.metadata.create_all(engine)
print("Table created if it did not exist.")

Session = sessionmaker(bind=engine)
session = Session()

user_names = ["Shivam", "Rajesh", "Kartik"]
for i in user_names:
    new_user = User(u_name=i)
    session.add(new_user)
session.commit()

print("New user added.")
