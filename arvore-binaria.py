class NovoNo:
    def __init__(self, valor):
        self.esquerda = None
        self.direita = None
        self.valor = valor
        
class ArvoreBinaria:
    def __init__(self):
        self.raiz = None
        
    def inserirElementoNaArvore(self, valor):
        if self.raiz is None:
            print("###### Iniciado criação da árvore #####")
            
            self.raiz = NovoNo(valor)
            print(f"Inserido nó {self.raiz.valor} como raíz da árvore")
        else:
            self.inserirElementoEmNo(self.raiz, valor)
            
    def inserirElementoEmNo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = NovoNo(valor)
                print(f"Criado nó {no.esquerda.valor} à esquerda do nó {no.valor}")
            else:
                self.inserirElementoEmNo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = NovoNo(valor)
                print(f"Criado nó {no.direita.valor} à direita do nó {no.valor}")
            else:
                self.inserirElementoEmNo(no.direita, valor)
                
    def elementosOrdemCrescente(self):
        print("##### Iniciado percorrimento dos elementos da árvore pela raíz")
        
        listaOrdenada = []
        self.percorreElementosEmNo(self.raiz, listaOrdenada, "")
        return listaOrdenada
        
    def percorreElementosEmNo(self, no, listaOrdenada, _lado):
        if no is not None:
            print("Percorrento elementos à esquerda do nó: ", no.valor)
            self.percorreElementosEmNo(no.esquerda, listaOrdenada, "esquerdo")
            
            listaOrdenada.append(no.valor)
            print("-----> Adicionou valor a lista ordenada: ", no.valor)
            
            print("Percorrento elementos à direita do nó: ", no.valor)
            self.percorreElementosEmNo(no.direita, listaOrdenada, "direito")
        else:
            print(f"# Limite do lado {_lado} do nó atingido #")
   
##########################################################################             
                
elementos =  [10, 6, 14, 5, 8, 11, 18]  
            
arvore = ArvoreBinaria()

print("Elementos em ordem original: ", elementos,)

for elemento in elementos:
    arvore.inserirElementoNaArvore(elemento)
    
print("Elementos em ordem crescente: ", arvore.elementosOrdemCrescente())
    
        
        
        