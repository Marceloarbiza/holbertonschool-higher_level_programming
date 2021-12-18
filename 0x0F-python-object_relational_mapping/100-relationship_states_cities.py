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
    state_parent = State(name='California')
    city_child = City(name='San Francisco')
    state_parent.cities.append(city_child)
    session.add(state_parent)
    session.commit()
    session.close()
