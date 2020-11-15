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
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario, "| Supervisor: ", self.supervisor, "| Antiguedad: ",self.antiguedad,"|")
class Jefe(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, salario,CocheEmpresa,secretario,incremento=20):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.incremento = incremento
        self.CocheEmpresa = CocheEmpresa
        self.secretario = secretario
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario,"| Cargo: JEFE DE ZONA")
        self.CocheEmpresa.Imprimir()
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
    def __init__(self, nombre, apellidos,DNI,direccion,salario,supervisor,antiguedad,incremento=5):
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor
        self.incremento= incremento
        self.antiguedad = antiguedad
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario, "| Supervisor: ", self.supervisor, "| Antiguedad: ",self.antiguedad,"|")
class CocheEmpresa():
    def __init__(self, matricula, marca, modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
    def Imprimir(self):
        print("|Matricula: ",self.matricula,"| Marca: ",self.marca,"| Modelo: ",self.modelo)
class Vendedor(Empleado):
    def __init__(self,nombre, apellidos,DNI,direccion,salario,supervisor,antiguedad,CocheEmpresa,telefono,areaVenta,lista_clientes,comision,incremento=10):
        self.telefono = telefono
        self.areaVenta = areaVenta
        self.lista_clientes = lista_clientes
        self.comision = comision
        self.incremento = incremento
        self.CocheEmpresa = CocheEmpresa
        self.nombre = nombre
        self.apellidos = apellidos
        self.DNI = DNI
        self.direccion = direccion
        self.salario = salario
        self.supervisor = supervisor
        self.antiguedad = antiguedad
    def Incremento(self):
        Sueldo = self.salario + ((self.salario*self.incremento)/100)
        Sueldo_Final = Sueldo
        if self.comision > 0:
            Sueldo_Final = Sueldo + ((self.salario*self.comision)/100)
        print("| Sueldo Base = ",self.salario,"|")
        print("| Suedo Final = ",Sueldo_Final,"|")
    def Imprimir(self):
        print("|Nombre: ", self.nombre, "| Apellidos: ", self.apellidos, "| DNI: ", self.DNI, "| Salario: ",self.salario, "| Supervisor: ", self.supervisor, "| Antiguedad: ", self.antiguedad, "|")
        print("|Telefono: ",self.telefono,"| Area de Venta", self.areaVenta,self.comision,self.incremento)
        self.CocheEmpresa.Imprimir()
        print("Lista de Clientes")
        for c in lista_clientes:
            c.Imprimir()
    def AltaCliente(self):
        Nombre = input("Ingrese Nombre del Cliente >>")
        DNI = input("Ingrese DNI >>")
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
    NuevoSupervisor = Supervisor("Empleado 1","Lopez",4654654,"Calle San Marcos nº15",1500,"nulo",1)
    lista_empleados.append(NuevoSupervisor)
    NuevoEmpleado = Empleado("Empleado 2","Garcia",64564654,"Avenida los carmenes mº45",1200,NuevoSupervisor.nombre,2)
    lista_empleados.append(NuevoEmpleado)
    NuevoSecretario = Secretario("Empleado 3","Muñoz",65465454,"Calle la Tula",1400,NuevoSupervisor.nombre,3)
    lista_empleados.append(NuevoSecretario)
    NuevoEmpleado2 = Empleado("Empleado 4", "Garcia", 64564654, "Avenida los carmenes mº45", 1200,NuevoSupervisor.nombre, 2)
    lista_empleados.append(NuevoEmpleado2)
    cochejefe = CocheEmpresa("7895Asd","Seat Cupra","x")
    Jefe  = Jefe("Jefe","Navarro",65464556,"Avenida los Patos nº20",2000,cochejefe,NuevoSecretario,1)
    lista_empleados.append(Jefe)

    Cliente1 = Cliente("Juan","1")
    lista_clientes.append(Cliente1)
    Cliente2 = Cliente("Juan","2")
    lista_clientes.append(Cliente2)
    Cliente3 = Cliente("Juan","3")
    lista_clientes.append(Cliente3)

    coche1= CocheEmpresa("54654AfD","Opel","Corsa")

    NuevoVendedor = Vendedor("Vendedor 1","Paco",345345345,"Calle Amapola",1700,NuevoSupervisor.nombre,2,coche1,64656465,"Granada",lista_clientes,6,1)
    lista_empleados.append(NuevoVendedor)

    for i in lista_empleados:
                i.Imprimir()
    NuevoVendedor.Incremento()
    NuevoVendedor.BajaCliente()

    for i in lista_clientes:
                i.Imprimir()

    NuevoVendedor.AltaCliente()

    for i in lista_clientes:
                i.Imprimir()

    print("Alta de un vendedor")

    Jefe.AltaVendedor()

    for Vendedor in lista_vendedores:
                i.Imprimir()