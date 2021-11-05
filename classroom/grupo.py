from classroom.asignatura import Asignatura
from classroom.asignatura import Asignatura


class Grupo:

    grado = "Grado 12"

    def __init__(self, grupo="grupo predeterminado", asignaturas=None, estudiantes=None):
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):
        asignaturas = []
        for x in kwargs.values():
            asignaturas.append(Asignatura(x))
        self._asignaturas = asignaturas

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            lista = []
        lista.append(alumno)
        if self.listadoAlumnos is not None:
            self.listadoAlumnos = self.listadoAlumnos + lista
        else:
            self.listadoAlumnos = lista

    @ classmethod
    def asignarNombre(cls, nombre= "Grado 6"):
        cls.grado = nombre

    def __str__(self):
        return "Grupo de estudiantes: "+ self._grupo
