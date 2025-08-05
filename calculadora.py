#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Calculadora Otimizada - Uma calculadora avançada em Python
Autor: Calculadora Team
Versão: 2.0.0
"""

import math
import re
import sys
from typing import Union, List, Dict, Any
import json
import os
from datetime import datetime

class CalculadoraOtimizada:
    """Classe principal da calculadora com funcionalidades avançadas."""
    
    def __init__(self):
        """Inicializa a calculadora com configurações padrão."""
        self.historico: List[Dict[str, Any]] = []
        self.memoria: Dict[str, float] = {}
        self.funcoes_disponiveis = {
            'sin': math.sin,
            'cos': math.cos,
            'tan': math.tan,
            'asin': math.asin,
            'acos': math.acos,
            'atan': math.atan,
            'sqrt': math.sqrt,
            'log': math.log10,
            'ln': math.log,
            'exp': math.exp,
            'abs': abs,
            'round': round,
            'floor': math.floor,
            'ceil': math.ceil,
            'pi': math.pi,
            'e': math.e
        }
        
    def limpar_tela(self):
        """Limpa a tela do terminal."""
        os.system('cls' if os.name == 'nt' else 'clear')
        
    def exibir_banner(self):
        """Exibe o banner da calculadora."""
        banner = """
╔══════════════════════════════════════════════════════════════╗
║                    CALCULADORA OTIMIZADA v2.0                ║
║                                                              ║
║  Funcionalidades:                                            ║
║  • Operações básicas (+, -, *, /, **, %)                    ║
║  • Funções trigonométricas (sin, cos, tan, etc.)            ║
║  • Funções logarítmicas (log, ln)                           ║
║  • Constantes matemáticas (π, e)                            ║
║  • Histórico de cálculos                                     ║
║  • Memória de variáveis                                      ║
║  • Conversões de unidades                                    ║
║                                                              ║
║  Comandos especiais:                                         ║
║  • 'hist' - Ver histórico                                   ║
║  • 'mem' - Ver memória                                      ║
║  • 'clear' - Limpar histórico                               ║
║  • 'help' - Ajuda                                           ║
║  • 'quit' - Sair                                            ║
╚══════════════════════════════════════════════════════════════╝
        """
        print(banner)
        
    def validar_expressao(self, expressao: str) -> bool:
        """Valida se a expressão matemática é segura para execução."""
        # Remove espaços em branco
        expressao = expressao.replace(' ', '')
        
        # Caracteres permitidos
        caracteres_permitidos = set('0123456789+-*/.()^%abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_')
        
        # Verifica se todos os caracteres são permitidos
        if not all(c in caracteres_permitidos for c in expressao):
            return False
            
        # Verifica se há palavras-chave perigosas
        palavras_perigosas = ['import', 'exec', 'eval', 'open', 'file', 'system', 'subprocess']
        for palavra in palavras_perigosas:
            if palavra in expressao.lower():
                return False
                
        return True
        
    def preparar_expressao(self, expressao: str) -> str:
        """Prepara a expressão para avaliação segura."""
        # Substitui operadores
        expressao = expressao.replace('^', '**')
        expressao = expressao.replace('×', '*')
        expressao = expressao.replace('÷', '/')
        
        # Adiciona funções matemáticas ao namespace
        namespace = self.funcoes_disponiveis.copy()
        namespace.update(self.memoria)
        
        return expressao, namespace
        
    def calcular(self, expressao: str) -> Union[float, str]:
        """Calcula o resultado de uma expressão matemática."""
        try:
            # Valida a expressão
            if not self.validar_expressao(expressao):
                return "Erro: Expressão inválida ou não permitida"
                
            # Prepara a expressão
            expressao_limpa, namespace = self.preparar_expressao(expressao)
            
            # Avalia a expressão
            resultado = eval(expressao_limpa, {"__builtins__": {}}, namespace)
            
            # Adiciona ao histórico
            self.adicionar_ao_historico(expressao, resultado)
            
            return resultado
            
        except ZeroDivisionError:
            return "Erro: Divisão por zero"
        except ValueError as e:
            return f"Erro: Valor inválido - {str(e)}"
        except SyntaxError:
            return "Erro: Sintaxe inválida"
        except Exception as e:
            return f"Erro: {str(e)}"
            
    def adicionar_ao_historico(self, expressao: str, resultado: Any):
        """Adiciona um cálculo ao histórico."""
        self.historico.append({
            'expressao': expressao,
            'resultado': resultado,
            'timestamp': datetime.now().isoformat()
        })
        
        # Mantém apenas os últimos 50 cálculos
        if len(self.historico) > 50:
            self.historico.pop(0)
            
    def exibir_historico(self):
        """Exibe o histórico de cálculos."""
        if not self.historico:
            print("\n📋 Histórico vazio")
            return
            
        print("\n📋 HISTÓRICO DE CÁLCULOS:")
        print("=" * 60)
        for i, calc in enumerate(self.historico[-10:], 1):  # Mostra apenas os últimos 10
            print(f"{i:2d}. {calc['expressao']} = {calc['resultado']}")
        print("=" * 60)
        
    def exibir_memoria(self):
        """Exibe as variáveis em memória."""
        if not self.memoria:
            print("\n💾 Memória vazia")
            return
            
        print("\n💾 VARIÁVEIS EM MEMÓRIA:")
        print("=" * 40)
        for var, valor in self.memoria.items():
            print(f"{var} = {valor}")
        print("=" * 40)
        
    def limpar_historico(self):
        """Limpa o histórico de cálculos."""
        self.historico.clear()
        print("\n✅ Histórico limpo com sucesso!")
        
    def converter_unidades(self, valor: float, de_unidade: str, para_unidade: str) -> Union[float, str]:
        """Converte unidades de medida."""
        conversoes = {
            'comprimento': {
                'm': 1.0,
                'km': 1000.0,
                'cm': 0.01,
                'mm': 0.001,
                'mi': 1609.34,
                'yd': 0.9144,
                'ft': 0.3048,
                'in': 0.0254
            },
            'peso': {
                'kg': 1.0,
                'g': 0.001,
                'mg': 0.000001,
                'lb': 0.453592,
                'oz': 0.0283495
            },
            'temperatura': {
                'celsius': lambda x: x,
                'fahrenheit': lambda x: (x - 32) * 5/9,
                'kelvin': lambda x: x - 273.15
            }
        }
        
        # Implementação básica - pode ser expandida
        try:
            if de_unidade in conversoes['comprimento'] and para_unidade in conversoes['comprimento']:
                metros = valor * conversoes['comprimento'][de_unidade]
                return metros / conversoes['comprimento'][para_unidade]
            else:
                return "Unidades não suportadas"
        except:
            return "Erro na conversão"
            
    def exibir_ajuda(self):
        """Exibe a ajuda da calculadora."""
        ajuda = """
📖 AJUDA DA CALCULADORA:

🔢 OPERAÇÕES BÁSICAS:
   + : Adição
   - : Subtração
   * : Multiplicação
   / : Divisão
   ** : Potenciação
   % : Módulo

📐 FUNÇÕES MATEMÁTICAS:
   sin(x), cos(x), tan(x) : Trigonométricas
   asin(x), acos(x), atan(x) : Trigonométricas inversas
   sqrt(x) : Raiz quadrada
   log(x) : Logaritmo base 10
   ln(x) : Logaritmo natural
   exp(x) : Exponencial
   abs(x) : Valor absoluto
   round(x) : Arredondamento
   floor(x) : Piso
   ceil(x) : Teto

🔢 CONSTANTES:
   pi : π (3.14159...)
   e : Número de Euler (2.71828...)

💾 COMANDOS ESPECIAIS:
   hist : Ver histórico
   mem : Ver memória
   clear : Limpar histórico
   help : Esta ajuda
   quit : Sair

💡 EXEMPLOS:
   2 + 3 * 4
   sin(pi/2)
   sqrt(16)
   log(100)
   x = 5 (armazena na memória)
        """
        print(ajuda)
        
    def executar(self):
        """Executa o loop principal da calculadora."""
        self.limpar_tela()
        self.exibir_banner()
        
        while True:
            try:
                print("\n" + "="*60)
                entrada = input("🔢 Digite uma expressão ou comando: ").strip()
                
                if not entrada:
                    continue
                    
                # Comandos especiais
                if entrada.lower() == 'quit':
                    print("\n👋 Obrigado por usar a Calculadora Otimizada!")
                    break
                elif entrada.lower() == 'hist':
                    self.exibir_historico()
                    continue
                elif entrada.lower() == 'mem':
                    self.exibir_memoria()
                    continue
                elif entrada.lower() == 'clear':
                    self.limpar_historico()
                    continue
                elif entrada.lower() == 'help':
                    self.exibir_ajuda()
                    continue
                    
                # Verifica se é uma atribuição de variável
                if '=' in entrada and not entrada.startswith('='):
                    partes = entrada.split('=', 1)
                    if len(partes) == 2:
                        var = partes[0].strip()
                        valor_expr = partes[1].strip()
                        
                        if var.isidentifier():
                            resultado = self.calcular(valor_expr)
                            if isinstance(resultado, (int, float)):
                                self.memoria[var] = resultado
                                print(f"✅ {var} = {resultado}")
                            else:
                                print(f"❌ {resultado}")
                            continue
                            
                # Cálculo normal
                resultado = self.calcular(entrada)
                print(f"📊 Resultado: {resultado}")
                
            except KeyboardInterrupt:
                print("\n\n👋 Calculadora interrompida pelo usuário!")
                break
            except EOFError:
                print("\n\n👋 Fim do arquivo de entrada!")
                break
            except Exception as e:
                print(f"❌ Erro inesperado: {str(e)}")

def main():
    """Função principal."""
    try:
        calc = CalculadoraOtimizada()
        calc.executar()
    except Exception as e:
        print(f"❌ Erro fatal: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()