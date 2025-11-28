class Animal:
    def __init__(self, nome):
        self.nome = nome
        
    def emitir_som(self):
        print(f'{self.nome} fez um som genérico')
        
class Cachorro(Animal):
    def emitir_som(self):
        print(f'{self.nome} está latindo: au au!')

class Gato(Animal):
    def emitir_som(self):
        print(f'{self.nome} está miando: miau!')
        
class Vaca(Animal):
    def emitir_som(self):
        print(f'{self.nome} está mugindo: muu!')
        
class Ave(Animal):
    def __init__(self, nome, envergadura):
        super().__init__(nome) #pega o nome do animal
        self.envergadura = envergadura
    
    def emitir_som(self):
        #chamando o método da classe pai
        super().emitir_som() #opcional
        print(f'{self.nome} está cantando: fiuuu!')
        print(f'{self.nome} tem {self.envergadura}m de envergadura.')


if __name__ == '__main__':
    animais = [
        Cachorro('Spike'),
        Gato('Khaleesi'),
        Vaca('Mimosa'),
        Ave('Loro', 1.98)
    ]
    
    for animal in animais:
        animal.emitir_som()