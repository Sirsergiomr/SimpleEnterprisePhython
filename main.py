lista_empleados = []

class Empleado():
    def __init__(self, nombre, apellidos,DNI,direccion,salario,supervisor):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor

    def Imprimir(self):
            print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario,"| Supervisor: ",self.supervisor,"|")

    def Supervisor(self):
        nuevoSupervisor = input("Nombre del supervisor")

class Supervisor(Empleado):
    print()

if __name__ == '__main__':
    NuevoSupervisor = Supervisor("Empleado 1","Lopez",4654654,"Calle San Marcos nº15",1500,"nulo")
    lista_empleados.append(NuevoSupervisor)
    NuevoEmpleado = Empleado("Empleado 2","Garcia",64564654,"Avenida los carmenes mº45",1200,NuevoSupervisor.nombre)
    NuevoEmpleado.Imprimir()

    lista_empleados.append(NuevoEmpleado)

    for i in lista_empleados:
        i.Imprimir()
