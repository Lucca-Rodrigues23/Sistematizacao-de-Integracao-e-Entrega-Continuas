from conversor_temperatura import celsius_para_fahrenheit, fahrenheit_para_celsius, menu, main


def simular_entradas(monkeypatch, entradas):
    """Simula o usuário digitando cada valor da lista, em ordem."""
    iterador = iter(entradas)
    monkeypatch.setattr("builtins.input", lambda _="": next(iterador))


def test_celsius_para_fahrenheit():
    assert celsius_para_fahrenheit(0) == 32
    assert celsius_para_fahrenheit(100) == 212
    assert celsius_para_fahrenheit(-40) == -40


def test_fahrenheit_para_celsius():
    assert fahrenheit_para_celsius(32) == 0
    assert fahrenheit_para_celsius(212) == 100
    assert fahrenheit_para_celsius(-40) == -40


def test_menu_retorna_opcao(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["  1  "])
    assert menu() == "1"
    assert "Celsius para Fahrenheit" in capsys.readouterr().out


def test_main_celsius_para_fahrenheit(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["1", "100", "3"])
    main()
    assert "100.0°C equivalem a 212.00°F" in capsys.readouterr().out


def test_main_fahrenheit_para_celsius(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["2", "212", "3"])
    main()
    assert "212.0°F equivalem a 100.00°C" in capsys.readouterr().out


def test_main_opcao_invalida(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["9", "3"])
    main()
    assert "Opção inválida" in capsys.readouterr().out


def test_main_voltar_ao_menu(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["1", "sair", "3"])
    main()
    assert "Voltando ao menu principal" in capsys.readouterr().out


def test_main_valor_invalido(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["1", "abc", "3"])
    main()
    assert "Valor inválido" in capsys.readouterr().out


def test_main_encerrar(monkeypatch, capsys):
    simular_entradas(monkeypatch, ["3"])
    main()
    assert "Encerrando o conversor" in capsys.readouterr().out


def test_main_interrompido_pelo_usuario(monkeypatch, capsys):
    def levantar_interrupcao(_=""):
        raise KeyboardInterrupt

    monkeypatch.setattr("builtins.input", levantar_interrupcao)
    main()
    assert "Programa interrompido" in capsys.readouterr().out
