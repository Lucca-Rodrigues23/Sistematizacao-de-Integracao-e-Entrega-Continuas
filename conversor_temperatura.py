"""
Conversor de Temperatura
------------------------
Converte entre Celsius, Fahrenheit e Kelvin.
"""

def celsius_para_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32

def fahrenheit_para_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9

def celsius_para_kelvin(celsius: float) -> float:
    return celsius + 273.15

def kelvin_para_celsius(kelvin: float) -> float:
    return kelvin - 273.15

def fahrenheit_para_kelvin(fahrenheit: float) -> float:
    celsius = fahrenheit_para_celsius(fahrenheit)
    return celsius_para_kelvin(celsius)

def kelvin_para_fahrenheit(kelvin: float) -> float:
    celsius = kelvin_para_celsius(kelvin)
    return celsius_para_fahrenheit(celsius)
