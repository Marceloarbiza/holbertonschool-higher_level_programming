#!/usr/bin/python3
"""Start link class to table in database
"""


if __name__ == "__main__":

    import sys
    from model_state import Base, State
    from model_city import City

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    tot = session.query(State, City).filter(City.state_id == State.id)\
                 .order_by(City.id).all()
    for st, ci in tot:
        print(f'{st.name}: ({ci.id}) {ci.name}')
    session.close()
