class Neurona():

    def __init__(self, peso):
        self.peso = peso
        self.entrada = None
        self.salida = None

    def forward(self, entrada):
        self.entrada = entrada
        self.salida = self.entrada * self.peso
        return self.salida