from sqlalchemy import Column, Integer, Boolean , Text
from database import Base  #database.py에 있는 Base를 임포트한것

class Todo(Base):
    # 테이블 이름 설정
    __tablename__ = 'todos'

    # 컬럼 설정
    id = Column(Integer, primary_key=True)
    task = Column(Text)
    completed = Column(Boolean, default=False)



