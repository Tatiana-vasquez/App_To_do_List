from sqlalchemy import Column, Integer, String, Boolean
import db


class Tarea(db.Base):
    __tablename__ = 'persona'  # nombre de la tabla
    __table_args__ = {'sqlite_autoincrement': True}  # PK se convierte en autoincremento ID_use
    id_tarea = Column(Integer, primary_key=True)
    contenido = Column(String(200), nullable=False)  # esto hace q el campo no pueda estar vacio
    hecha = Column(Boolean)

    def __init__(self, contenido, hecha):
        self.contenido = contenido
        self.hecha = hecha

    def __str__(self):
        return 'Tarea({},{},{})'.format(self.id_tarea, self.contenido, self.hecha)