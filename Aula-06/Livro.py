class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    
    def exibir_detalhes(self):
        print(f"O livro {self.titulo} do autor {self.autor}")