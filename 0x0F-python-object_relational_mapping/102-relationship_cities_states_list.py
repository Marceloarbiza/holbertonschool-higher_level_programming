#!/usr/bin/python3
"""Start link class to table in database
"""
if __name__ == "__main__":

    import sys
    from relationship_state import Base, State
    from relationship_city import City

    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()
    states_data = session.query(State).order_by(State.id).all()
    for s in states_data:
        for c in s.cities:
            print(f'{c.id}: {c.name} -> {s.name}')
    session.close()
