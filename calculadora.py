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
#Função para verificar entradas numéricas inválidas
def entrada_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

#Função principal
def calculadora():
    historico = [] # Lista para armazenar as últimas 5 operações
    while True:
        print("\nSelecione a operação:")
        print("1- Soma")
        print("2- Subtração")
        print("3- Multiplicação")
        print("4- Divisão")
        print("5 - Exibir histórico")
        print("6 - Sair")

        escolha=input("Digite o número da operação desejada (1/2/3/4/5/6): ")
         #Verificar se a escolha é válida
        if escolha in ['1','2','3','4']:
            num1 = entrada_numero("Digite o primeiro número: ")
            num2 = entrada_numero("Digite o segundo número: ")

            if escolha == '1':
                resultado = soma(num1, num2)
                operacao = f"{num1} + {num2} = {resultado}"
                print(operacao)
            elif escolha == '2':
                resultado = subtracao(num1, num2)
                operacao = f"{num1} - {num2} = {resultado}"
                print(operacao)
            elif escolha == '3':
                resultado = multiplicacao(num1, num2)
                operacao = f"{num1} * {num2} = {resultado}"
                print(operacao)
            elif escolha == '4':
                resultado = divisao(num1, num2)
                operacao = f"{num1} / {num2} = {resultado}"
                print(operacao)
            #Armazenar a operação no histórico
            armazenar_operacao(operacao, historico)
        elif escolha == '5':
            # Exibir hisórico
            exibir_historico(historico)
        elif escolha == '6':
            # Sair do programa
            print("Encerrando a calculadora.")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")


# Executa a calculadora
calculadora()
