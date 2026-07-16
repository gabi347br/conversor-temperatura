temperatura = float(input("Informe a temperatura em graus Celsius: "))
# Solicita ao usuário para que informe a temperatura em Celsius
# A resposta inserida é automaticamente convertida para decimal por meio do float()

conversao = (temperatura * 9/5) + 32
# Conversão matemática de Celsius para Fahrenheit utilizando fórmula

print(f"A conversão para Fahrenheit é {conversao:.1f}")
# Exibe o resultado para o usuário em formato de string
