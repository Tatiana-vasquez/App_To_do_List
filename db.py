from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# configurar el engine a SQLalchemy comunicarse con la base de datos

engine = create_engine("sqlite:///database/tareas.db")
# advertencia, crear el engine no conecta a la base de datos

# ahora creamos la sesion, lo que nos permite realizar transacciones( operaciones) en nuestra BD
Session = sessionmaker(bind=engine)
session = Session()

# vinculacion
# ahora vamos al fichero models.py y en los modelos (clases) donde queramos q se transformen en tablas,
# le agregamos esta varibale, y esto se encarga de mapear y vincular la clase a la tabla
Base = declarative_base()
