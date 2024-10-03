class personaje:
    #atributos
    def _init_(self, nombre, edad, usuario, bando, raza):
        self.nombre=nombre
        self.edad=edad
        self.usuario=usuario
        self.bando=bando
        self.raza=raza
    def mostrar_personaje(self):
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "usuario": self.usuario,
            "bando": self.bando,
            "raza": self.raza
        }
luffy=personaje("luffy", 18, "gomu gomu no", "pirata", "humano")
print(luffy.mostrar_personaje())
print(luffy.usuario)
cobby=personaje("cobby", 15, "no", "sword", "humano")
print(cobby.bando)
king=personaje("king", 40, "zoan mitologica", "pirata", "lunaria")
print(king.nombre)