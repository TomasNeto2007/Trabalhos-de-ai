#Função de cada operação
def soma(x, y):
     return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
   if y !=0:
    return x / y
   else:
       return "Erro: Divisão por zero não é permitida"
        
# Função para armazenar as últimas 5 operações
def armazenar_operacao(operacao, historico):
    if len(historico)>=5:
        historico.pop(0)
    historico.append(operacao)  # Adiciona a nova operação

# Função para exibir o histórico
def exibir_historico(historico):
    if len(historico) == 0:
        print("Nenhuma operação armazenada.")
    else:
        print("\nHistórico das últimas 5 operações:")
        for i, op in enumerate(historico,1):
            print(f"{i}.{op}")
