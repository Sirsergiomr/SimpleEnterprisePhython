class Empleado():
    def __init__(self, nombre, apellidos,DNI,direccion,salario,supervisor):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor
    def Imprimir(self):
        print("|Nombre: ",self.nombre,"| Apellidos: ",self.apellidos,"| DNI: ",self.DNI,"| Salario: ",self.salario,"| Supervisor: ",self.supervisor,"|")


if __name__ == '__main__':
    NuevoEmpleado = Empleado("Empleado 1","Garcia",64564654,"Avenida los carmenes mº45",1200,"nulo")

    NuevoEmpleado.Imprimir()
