class Rectangle:
    _nombre_de_rectangles = 0

    def __init__(self, longueur, largeur):
        self._longueur = longueur
        self._largeur = largeur
        Rectangle._nombre_de_rectangles += 1

    def obtenir_longueur(self):
        return self._longueur

    def definir_longueur(self, valeur):
        self._longueur = valeur

    def obtenir_largeur(self):
        return self._largeur

    def definir_largeur(self, valeur):
        self._largeur = valeur

    def surface(self):
        return self._longueur * self._largeur

    def perimetre(self):
        return 2 * (self._longueur + self._largeur)

    def __str__(self):
        return f"Rectangle(longueur={self._longueur}, largeur={self._largeur})"

class Parallelepipede(Rectangle):
    _nombre_de_parallelepipedes = 0

    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self._hauteur = hauteur
        Parallelepipede._nombre_de_parallelepipedes += 1

    def obtenir_hauteur(self):
        return self._hauteur

    def definir_hauteur(self, valeur):
        self._hauteur = valeur

    @staticmethod
    def nombre_de_parallelepipedes():
        return Parallelepipede._nombre_de_parallelepipedes

    def volume(self):
        return self.surface() * self._hauteur

    def __str__(self):
        return (f"Parallélépipède(longueur={self._longueur}, largeur={self._largeur}, "
                f"hauteur={self._hauteur})")

rect1 = Rectangle(10, 5)
rect2 = Rectangle(8, 4)
para1 = Parallelepipede(10, 5, 3)
para2 = Parallelepipede(8, 4, 2)

nombre_de_parallelepipedes = Parallelepipede.nombre_de_parallelepipedes()

print(rect1)
print(f"Nombre de parallélépipèdes: {nombre_de_parallelepipedes}")
