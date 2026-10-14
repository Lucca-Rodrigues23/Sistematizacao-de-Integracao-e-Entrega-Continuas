from conversor_temperatura import (
    celsius_para_fahrenheit,
    fahrenheit_para_celsius,
    celsius_para_kelvin,
    kelvin_para_celsius,
    fahrenheit_para_kelvin,
    kelvin_para_fahrenheit
)

def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40

def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(-40) == -40

def test_celsius_para_kelvin():
    assert celsius_para_kelvin(0) == 273.15
    assert celsius_para_kelvin(100) == 373.15

def test_kelvin_para_celsius():
    assert kelvin_para_celsius(273.15) == 0
    assert kelvin_para_celsius(373.15) == 100

def test_fahrenheit_para_kelvin():
    assert fahrenheit_para_kelvin(32) == 273.15

def test_kelvin_para_fahrenheit():
    assert kelvin_para_fahrenheit(273.15) == 32
