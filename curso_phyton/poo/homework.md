# actividad del banco:
´´´python

class banco:
    def _init_(self, nombre, apellido, dni, numero_cuenta, saldo_inicial):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.numero_cuenta=numero_cuenta
        self.saldo_inial=saldo_inicial
    def depositar(self):
        print("realizando deposito")
    def retirar(self):
        print("realizando retiro")
    def estado (self):
        print("estado de la cuenta")
REDsenario-banco("serapio", "muaa",45856576586,2333-3234-4343,96.080)