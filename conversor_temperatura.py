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
