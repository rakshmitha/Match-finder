# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///soul_data.db', echo = True)
Base = declarative_base() 

class SoulSimilarity(Base):
    __tablename__ = 'soulValues'

    Name = Column(String, primary_key = True)
    Gender = Column(String, nullable = False)
    age = Column(Integer, nullable = False)
    income = Column(Integer, nullable = False)
    race = Column(Integer, nullable = False)
    '''education = Column(Integer, nullable = False)
    physical_attractiveness = Column(Integer, nullable = False)
    bio_chemistry = Column(Integer, nullable = False)
    core_values = Column(Integer, nullable = False)
    life_stage = Column(Integer, nullable = False)
    mutual_selection = Column(Integer, nullable = False)
    life_orientation = Column(Integer, nullable = False)
    financial_security = Column(Integer, nullable = False)
    healthy_living = Column(Integer, nullable = False)
    emotional_outlook = Column(Integer, nullable = False)
    continuous_learning = Column(Integer, nullable = False)
    behavior_pattern = Column(Integer, nullable = False)
    interpersonal_skills = Column(Integer, nullable = False)
    commitment_level = Column(Integer, nullable = False)
    psychological_cost= Column(Integer, nullable = False)'''

Session = sessionmaker(bind = engine)
session = Session()

def add_data(Name, gender, age, income, race):
    
    row = SoulSimilarity(Name = Name, Gender = gender, age = age, income = income, race = race)    
    session.add(row)
    session.commit()      

def select_data (soul):
    print(soul)
    result = session.query(SoulSimilarity).filter(SoulSimilarity.Name.like(soul))
    print(result)
    try:
        return result[0].Name
    except:
        return -1

    