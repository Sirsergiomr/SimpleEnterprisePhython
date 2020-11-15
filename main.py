lista_empleados = []
lista_clientes = []
lista_vendedores = []
class Empleado():
    def __init__(self, nombre, apellidos,DNI,direccion,salario,supervisor,antiguedad):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor
        self.antiguedad = antiguedad
    def Incremento(self):
        Sueldo_Final = (self.salario * (self.incremento*self.antiguedad))/100
        print("| Suedo Final = ",Sueldo_Final)
    def Supervisor(self):
        nuevoSupervisor = input("Nombre del supervisor")
class Jefe(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, salario,cocheDeEmpresa,secretario,incremento=20):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.incremento = incremento
        self.cocheDeEmpresa = cocheDeEmpresa
        self.secretario = secretario
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario,"| Cargo: JEFE DE ZONA")
    def CambiarCoche(self):
        matricula = input("Matricla del coche: ")
        marca = input("Marca del vehiculo: ")
        modelo = input("Modelo: ")

        self.cocheDeEmpresa = CocheEmpresa(matricula, marca, modelo)
    def CambiaSecretario(self):
        DNIEmpleado = input("DNI del Empleado >>")
        for i in lista_empleados:
           if i.DNI == DNIEmpleado:
               self.secretario = i
    def AltaVendedor(self):
        DNIVendedor = input("Ingrese DNI")

        for i in lista_empleados:
            if i.DNI == DNIVendedor:
                lista_vendedores.append(i)
    def BajaVendedor(self):
        DNIVendedor = input("Ingrese DNI")

        for i in lista_empleados:
            if i.DNI == DNIVendedor:
                lista_vendedores.remove(i)
class Supervisor(Empleado):
                print()
class Secretario(Empleado):
    def __init__(self, nombre, apellidos,DNI,direccion,salario,supervisor,incremento=5):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor
        self.incremento= incremento
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario, "| Supervisor: ", self.supervisor, "| SalarioAnual: ",self.salarioAnual,"|")
class CocheEmpresa():
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
    def Imprimir(self):
        print("|Matricula: ",self.matricula,"| Marca: ",self.marca,"| Modelo: ",self.modelo)
class Vendedor(Empleado):
    def __init__(self,cocheDeEmpresa,telefono,areaVenta,listadeclientes,comision,incremento=10):
        self.telefono = telefono
        self.areaVenta = areaVenta
        self.listaclientes = listadeclientes
        self.comision = comision
        self.incremento = incremento
        self.cocheDeEmpresa = cocheDeEmpresa
    def Incremento(self):
        Sueldo = (self.salario * (self.incremento*self.antiguedad))/100
        Sueldo_Final = Sueldo
        if self.comision > 0:
            Sueldo_Final = (Sueldo * self.comision)/100
        print("| Suedo Final = ",Sueldo_Final)
    def Imprimir(self):
        print("|Telefono: ",self.telefono,"| Area de Venta", self.areaVenta,self.listaclientes,self.comision,self.incremento)

    def AltaCliente(self):
        Nombre = input("Ingrese Nombre del Cliente >>")
        DNI = input("Ingrese DNI")
        Nuevo_Cliente = Cliente(Nombre, DNI)
        lista_clientes.append(Nuevo_Cliente)
    def BajaCliente(self):
        DNI = input("DNI del CLiente que quiere dar de Baja >>")

        for Cliente in lista_clientes:
            if Cliente.DNI == DNI:
                lista_clientes.remove(Cliente)
class Cliente():
    def __init__(self,Nombre, DNI):
        self.Nombre = Nombre
        self.DNI = DNI
    def Imprimir(self):
        print("|Nombre: ",self.Nombre,"| DNI: ",self.DNI,"|")

if __name__ == '__main__':
    NuevoSupervisor = Supervisor("Empleado 1","Lopez",4654654,"Calle San Marcos nº15",1500,"nulo")
    lista_empleados.append(NuevoSupervisor)
    NuevoEmpleado = Empleado("Empleado 2","Garcia",64564654,"Avenida los carmenes mº45",1200,NuevoSupervisor.nombre)
    NuevoEmpleado.Imprimir()
    lista_empleados.append(NuevoEmpleado)
    NuevoSecretario = Secretario("Empleado 3","Muñoz",65465454,"Calle la Tula",1400,NuevoSupervisor.nombre,5)
    lista_empleados.append(NuevoSecretario)
    for i in lista_empleados:
                i.Imprimir()
