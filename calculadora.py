def calculadora():
    print("=== CALCULADORA ===")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = input("Escolha uma operação: ")

    if operacao not in ["1", "2", "3", "4"]:
        print("Operação inválida.")
        return

    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Erro: digite números válidos.")
        return

    if operacao == "1":
        resultado = numero1 + numero2
    elif operacao == "2":
        resultado = numero1 - numero2
    elif operacao == "3":
        resultado = numero1 * numero2
    elif operacao == "4":
        if numero2 == 0:
            print("Erro: não é possível dividir por zero.")
            return
        resultado = numero1 / numero2

    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    calculadora()

