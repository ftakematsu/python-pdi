import matplotlib.pyplot

class Histograma:
    def __init__(self):
        self.cinza = [0]*256
        self.frequencia = [0]*256
        self.probabilidade = [0]*256
        self.pixels = 1
        i=0
        while i<len(self.cinza):
            self.cinza[i] = i
            i+=1
        #print(self.cinza)
    
    def definirTotalPixels(self, pixels):
        self.pixels = pixels

    def definirFrequencia(self, tomCinza):
        if (tomCinza>=0 and tomCinza<256):
            # Incrementa 1 unidade naquele tom de cinza
            self.frequencia[tomCinza] += 1
            # Atualiza o percentual (probabilidade)
            self.probabilidade[tomCinza] = self.frequencia[tomCinza]/self.pixels
    
    def imprimirTabela(self):
        print("Cinza\tFrequencia\tProbabilidade")
        for i in range(256):
            print(f"{self.cinza[i]}\t{self.frequencia[i]}\t{self.probabilidade[i]}")

    def mostrarGrafico(self):
        matplotlib.pyplot.plot(self.cinza, self.probabilidade)
        matplotlib.pyplot.show()
