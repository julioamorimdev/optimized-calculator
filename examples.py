#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplos de uso da Calculadora Otimizada
Autor: Calculadora Team
Versão: 2.0.0
"""

from calculadora import CalculadoraOtimizada

def exemplo_operacoes_basicas():
    """Exemplo de operações matemáticas básicas."""
    print("🔢 EXEMPLOS DE OPERAÇÕES BÁSICAS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    exemplos = [
        ("2 + 3", "Adição"),
        ("10 - 4", "Subtração"),
        ("5 * 6", "Multiplicação"),
        ("15 / 3", "Divisão"),
        ("2 ** 3", "Potenciação"),
        ("17 % 5", "Módulo"),
        ("(2 + 3) * 4", "Parênteses"),
        ("10 + 5 * 2 - 3", "Precedência")
    ]
    
    for expressao, descricao in exemplos:
        resultado = calc.calcular(expressao)
        print(f"{descricao:15} | {expressao:15} = {resultado}")
    
    print()

def exemplo_funcoes_matematicas():
    """Exemplo de funções matemáticas."""
    print("📐 EXEMPLOS DE FUNÇÕES MATEMÁTICAS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    exemplos = [
        ("sin(0)", "Seno de 0"),
        ("cos(0)", "Cosseno de 0"),
        ("tan(0)", "Tangente de 0"),
        ("sin(pi/2)", "Seno de π/2"),
        ("sqrt(16)", "Raiz quadrada de 16"),
        ("log(100)", "Log base 10 de 100"),
        ("ln(1)", "Log natural de 1"),
        ("abs(-5)", "Valor absoluto de -5"),
        ("round(3.7)", "Arredondamento de 3.7"),
        ("floor(3.7)", "Piso de 3.7"),
        ("ceil(3.2)", "Teto de 3.2")
    ]
    
    for expressao, descricao in exemplos:
        resultado = calc.calcular(expressao)
        print(f"{descricao:20} | {expressao:15} = {resultado}")
    
    print()

def exemplo_constantes():
    """Exemplo de constantes matemáticas."""
    print("🔢 EXEMPLOS DE CONSTANTES MATEMÁTICAS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    exemplos = [
        ("pi", "π (Pi)"),
        ("e", "e (Número de Euler)"),
        ("2 * pi", "2π"),
        ("e ** 2", "e²"),
        ("sin(pi)", "Seno de π"),
        ("ln(e)", "Log natural de e")
    ]
    
    for expressao, descricao in exemplos:
        resultado = calc.calcular(expressao)
        print(f"{descricao:20} | {expressao:15} = {resultado}")
    
    print()

def exemplo_memoria_variaveis():
    """Exemplo de uso de memória de variáveis."""
    print("💾 EXEMPLOS DE MEMÓRIA DE VARIÁVEIS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    # Simula atribuições de variáveis
    calc.memoria['x'] = 5.0
    calc.memoria['y'] = 10.0
    calc.memoria['raio'] = 3.0
    
    exemplos = [
        ("x + y", "Soma de variáveis"),
        ("x * y", "Produto de variáveis"),
        ("2 * pi * raio", "Perímetro do círculo"),
        ("pi * raio ** 2", "Área do círculo"),
        ("sqrt(x**2 + y**2)", "Hipotenusa")
    ]
    
    for expressao, descricao in exemplos:
        resultado = calc.calcular(expressao)
        print(f"{descricao:25} | {expressao:20} = {resultado}")
    
    print()

def exemplo_conversoes():
    """Exemplo de conversões de unidades."""
    print("🔄 EXEMPLOS DE CONVERSÕES DE UNIDADES")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    # Conversões de comprimento
    print("📏 COMPRIMENTO:")
    print(f"1000 m → km: {calc.converter_unidades(1000, 'm', 'km')}")
    print(f"1 km → m: {calc.converter_unidades(1, 'km', 'm')}")
    print(f"100 cm → m: {calc.converter_unidades(100, 'cm', 'm')}")
    print(f"1 mi → km: {calc.converter_unidades(1, 'mi', 'km')}")
    
    print()

def exemplo_historico():
    """Exemplo de uso do histórico."""
    print("📋 EXEMPLO DE HISTÓRICO")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    # Faz alguns cálculos
    calc.calcular("2 + 3")
    calc.calcular("5 * 4")
    calc.calcular("sqrt(16)")
    calc.calcular("sin(pi/2)")
    
    print("Histórico de cálculos:")
    calc.exibir_historico()
    
    print()

def exemplo_tratamento_erros():
    """Exemplo de tratamento de erros."""
    print("⚠️ EXEMPLOS DE TRATAMENTO DE ERROS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    exemplos_erro = [
        ("10 / 0", "Divisão por zero"),
        ("sqrt(-1)", "Raiz de número negativo"),
        ("log(-1)", "Log de número negativo"),
        ("invalid", "Expressão inválida"),
        ("import os", "Comando perigoso")
    ]
    
    for expressao, descricao in exemplos_erro:
        resultado = calc.calcular(expressao)
        print(f"{descricao:25} | {expressao:15} → {resultado}")
    
    print()

def exemplo_expressoes_complexas():
    """Exemplo de expressões matemáticas complexas."""
    print("🧮 EXEMPLOS DE EXPRESSÕES COMPLEXAS")
    print("=" * 40)
    
    calc = CalculadoraOtimizada()
    
    exemplos = [
        ("((2 + 3) * (4 - 1)) / 3", "Expressão aninhada"),
        ("sin(pi/2) + cos(0)", "Funções trigonométricas"),
        ("sqrt(16) + log(100)", "Funções mistas"),
        ("2 * pi * 5", "Cálculo de perímetro"),
        ("e ** (ln(10))", "Propriedades logarítmicas"),
        ("abs(-5) + round(3.7)", "Funções de arredondamento")
    ]
    
    for expressao, descricao in exemplos:
        resultado = calc.calcular(expressao)
        print(f"{descricao:30} | {expressao:25} = {resultado}")
    
    print()

def main():
    """Executa todos os exemplos."""
    print("🧮 CALCULADORA OTIMIZADA - EXEMPLOS DE USO")
    print("=" * 50)
    print()
    
    exemplo_operacoes_basicas()
    exemplo_funcoes_matematicas()
    exemplo_constantes()
    exemplo_memoria_variaveis()
    exemplo_conversoes()
    exemplo_historico()
    exemplo_tratamento_erros()
    exemplo_expressoes_complexas()
    
    print("✅ Todos os exemplos foram executados com sucesso!")
    print("\n💡 Dica: Execute 'python calculadora.py' para usar a calculadora interativamente.")

if __name__ == "__main__":
    main() 