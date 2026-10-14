"""
Conversor de Temperatura
------------------------
Converte entre Celsius, Fahrenheit e Kelvin.
"""

def celsius_para_fahrenheit(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_para_celsius(fahrenheit: float) -> float:
    """Converte uma temperatura de Fahrenheit para Celsius."""
    return (fahrenheit - 32) * 5 / 9


def celsius_para_kelvin(celsius: float) -> float:
    """Converte uma temperatura de Celsius para Kelvin."""
    return celsius + 273.15


def kelvin_para_celsius(kelvin: float) -> float:
    """Converte uma temperatura de Kelvin para Celsius."""
    return kelvin - 273.15


def fahrenheit_para_kelvin(fahrenheit: float) -> float:
    """Converte uma temperatura de Fahrenheit para Kelvin."""
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)


def kelvin_para_fahrenheit(kelvin: float) -> float:
    """Converte uma temperatura de Kelvin para Fahrenheit."""
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)


# pragma: no cover
def menu():
    print("\nEscolha a conversão desejada:")
    print("1 - Celsius para Fahrenheit")
    print("2 - Fahrenheit para Celsius")
    print("3 - Celsius para Kelvin")
    print("4 - Kelvin para Celsius")
    print("5 - Fahrenheit para Kelvin")
    print("6 - Kelvin para Fahrenheit")
    print("7 - Sair")
    return input("Opção: ").strip()


# pragma: no cover
def main():
    print("=== Conversor de Temperatura ===")

    try:
        while True:
            opcao = menu()

            if opcao == "7":
                print("Encerrando o conversor. Até mais!")
                break

            if opcao not in ("1", "2", "3", "4", "5", "6"):
                print("Opção inválida. Escolha uma opção de 1 a 7.")
                continue

            entrada = input("Digite a temperatura (ou 'sair' para voltar ao menu): ")

            if entrada.strip().lower() == "sair":
                print("Voltando ao menu principal...")
                continue

            try:
                valor = float(entrada)
            except ValueError:
                print("Valor inválido. Digite um número (ex: 25.5).")
                continue

            if opcao == "1":
                res = celsius_para_fahrenheit(valor)
                print(f"{valor}°C equivalem a {res:.2f}°F")
            elif opcao == "2":
                res = fahrenheit_para_celsius(valor)
                print(f"{valor}°F equivalem a {res:.2f}°C")
            elif opcao == "3":
                res = celsius_para_kelvin(valor)
                print(f"{valor}°C equivalem a {res:.2f}K")
            elif opcao == "4":
                res = kelvin_para_celsius(valor)
                print(f"{valor}K equivalem a {res:.2f}°C")
            elif opcao == "5":
                res = fahrenheit_para_kelvin(valor)
                print(f"{valor}°F equivalem a {res:.2f}K")
            elif opcao == "6":
                res = kelvin_para_fahrenheit(valor)
                print(f"{valor}K equivalem a {res:.2f}°F")

    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário. Até mais!")


if __name__ == "__main__":
    main()
