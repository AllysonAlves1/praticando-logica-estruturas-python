class No:
     def __init__(self, key, dir, esq):
          self.item = key
          self.dir = dir
          self.esq = esq

class Tree:

     def __init__(self):
          self.root = No(None,None,None)
          self.root = None

     def inserir(self, v):
          novo = No(v,None,None)
          if self.root == None:
               self.root = novo
          else:
               atual = self.root
               while True:
                    anterior = atual
                    if v <= atual.item:
                         atual = atual.esq
                         if atual == None:
                                anterior.esq = novo
                                return

                    else:
                         atual = atual.dir
                         if atual == None:
                                 anterior.dir = novo
                                 return

     def buscar(self, chave):
         if self.root == None:
              return None
         atual = self.root
         while atual.item != chave:
               if chave < atual.item:
                    atual = atual.esq
               else:
                    atual = atual.dir
               if atual == None:
                    return None
         return atual   

     def nosucessor(self, apaga):
          paidosucessor = apaga
          sucessor = apaga
          atual = apaga.dir 
          while atual != None: 
               paidosucessor = sucessor
               sucessor = atual
               atual = atual.esq
          if sucessor != apaga.dir:
               paidosucessor.esq = sucessor.dir
               sucessor.dir = apaga.dir
          return sucessor

     def remover(self, v):
         if self.root == None:
               return False
         atual = self.root
         pai = self.root
         filho_esq = True

         while atual.item != v:
               pai = atual
               if v < atual.item:
                    atual = atual.esq
                    filho_esq = True
               else:
                    atual = atual.dir 
                    filho_esq = False
               if atual == None:
                    return False

         if atual.esq == None and atual.dir == None:
               if atual == self.root:
                    self.root = None
               else:
                    if filho_esq:
                         pai.esq =  None
                    else:
                         pai.dir = None

         elif atual.dir == None:
               if atual == self.root:
                    self.root = atual.esq
               else:
                    if filho_esq:
                         pai.esq = atual.esq
                    else:
                         pai.dir = atual.esq
         
         elif atual.esq == None:
               if atual == self.root:
                    self.root = atual.dir
               else:
                    if filho_esq:
                         pai.esq = atual.dir
                    else:
                         pai.dir = atual.dir

         else:
               sucessor = self.nosucessor(atual)
               if atual == self.root:
                    self.root = sucessor
               else:
                    if filho_esq:
                         pai.esq = sucessor
                    else:
                         pai.dir = sucessor
               sucessor.esq = atual.esq
         return True

     def inOrder(self, atual):
         if atual != None:
              self.inOrder(atual.esq)
              print(atual.item,end=" ")
              self.inOrder(atual.dir)
  
     def preOrder(self, atual):
         if atual != None:
              print(atual.item,end=" ")
              self.preOrder(atual.esq)
              self.preOrder(atual.dir)
       
     def posOrder(self, atual):
         if atual != None:
              self.posOrder(atual.esq)
              self.posOrder(atual.dir)
              print(atual.item,end=" ")

     def caminhar(self):
          print(" Exibindo em ordem: ",end="")
          self.inOrder(self.root)
          print("\n Exibindo em pos-ordem: ",end="")
          self.posOrder(self.root)
          print("\n Exibindo em pre-ordem: ",end="")
          self.preOrder(self.root)
          print()

     def obter_filhos(self, valor):
          no = self.buscar(valor)
          if no is None:
               return "ERRO"
          filhos = [str(valor)]
          if no.esq is not None:
               filhos.append(str(no.esq.item))
          else:
               filhos.append("#")
          if no.dir is not None:
               filhos.append(str(no.dir.item))
          else:
               filhos.append("#")
          return " ".join(filhos)
     
entrada = input().split()
valores = list(map(int, entrada))

arvore = Tree()
for valor in valores:
    arvore.inserir(valor)

valor_no = int(input())

filhos = arvore.obter_filhos(valor_no)

print(filhos)
