#crie uma classe chamada forma, que possui os atributos area e perimetro
#independente as subclasses retangulo e triangulo, que devem conter os metodos calcularArea e calcularPerimetro
#a classe triangulo deve ter tambem o atributo altura
#no codigo teste crie umn objeto da classe triangulo e outro da classe retangulo.
#verifique se os odis sao instancias de forma (use instaceof), e calcule a area de cada um
class forma():

    def __init__(self):
        self.area = 0
        self.perimetro = 0

class retangulo():

    def __init__(self):
        
