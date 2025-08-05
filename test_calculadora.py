#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes automatizados para a Calculadora Otimizada
Autor: Calculadora Team
Versão: 2.0.0
"""

import unittest
import sys
import os
from unittest.mock import patch, MagicMock
from io import StringIO

# Adiciona o diretório atual ao path para importar o módulo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from calculadora import CalculadoraOtimizada

class TestCalculadoraOtimizada(unittest.TestCase):
    """Testes para a classe CalculadoraOtimizada."""
    
    def setUp(self):
        """Configuração inicial para cada teste."""
        self.calc = CalculadoraOtimizada()
        
    def tearDown(self):
        """Limpeza após cada teste."""
        self.calc.historico.clear()
        self.calc.memoria.clear()
        
    def test_inicializacao(self):
        """Testa se a calculadora é inicializada corretamente."""
        self.assertIsInstance(self.calc.historico, list)
        self.assertIsInstance(self.calc.memoria, dict)
        self.assertIsInstance(self.calc.funcoes_disponiveis, dict)
        self.assertEqual(len(self.calc.historico), 0)
        self.assertEqual(len(self.calc.memoria), 0)
        
    def test_operacoes_basicas(self):
        """Testa operações matemáticas básicas."""
        # Adição
        resultado = self.calc.calcular("2 + 3")
        self.assertEqual(resultado, 5.0)
        
        # Subtração
        resultado = self.calc.calcular("10 - 4")
        self.assertEqual(resultado, 6.0)
        
        # Multiplicação
        resultado = self.calc.calcular("5 * 6")
        self.assertEqual(resultado, 30.0)
        
        # Divisão
        resultado = self.calc.calcular("15 / 3")
        self.assertEqual(resultado, 5.0)
        
        # Potenciação
        resultado = self.calc.calcular("2 ** 3")
        self.assertEqual(resultado, 8.0)
        
        # Módulo
        resultado = self.calc.calcular("17 % 5")
        self.assertEqual(resultado, 2.0)
        
    def test_expressoes_complexas(self):
        """Testa expressões matemáticas complexas."""
        # Parênteses
        resultado = self.calc.calcular("(2 + 3) * 4")
        self.assertEqual(resultado, 20.0)
        
        # Múltiplas operações
        resultado = self.calc.calcular("10 + 5 * 2 - 3")
        self.assertEqual(resultado, 17.0)
        
        # Expressão aninhada
        resultado = self.calc.calcular("((2 + 3) * (4 - 1)) / 3")
        self.assertEqual(resultado, 5.0)
        
    def test_funcoes_matematicas(self):
        """Testa funções matemáticas."""
        # Trigonométricas
        resultado = self.calc.calcular("sin(0)")
        self.assertEqual(resultado, 0.0)
        
        resultado = self.calc.calcular("cos(0)")
        self.assertEqual(resultado, 1.0)
        
        resultado = self.calc.calcular("tan(0)")
        self.assertEqual(resultado, 0.0)
        
        # Logarítmicas
        resultado = self.calc.calcular("log(100)")
        self.assertEqual(resultado, 2.0)
        
        resultado = self.calc.calcular("ln(1)")
        self.assertEqual(resultado, 0.0)
        
        # Outras funções
        resultado = self.calc.calcular("sqrt(16)")
        self.assertEqual(resultado, 4.0)
        
        resultado = self.calc.calcular("abs(-5)")
        self.assertEqual(resultado, 5.0)
        
        resultado = self.calc.calcular("round(3.7)")
        self.assertEqual(resultado, 4.0)
        
    def test_constantes_matematicas(self):
        """Testa constantes matemáticas."""
        resultado = self.calc.calcular("pi")
        self.assertAlmostEqual(resultado, 3.141592653589793, places=10)
        
        resultado = self.calc.calcular("e")
        self.assertAlmostEqual(resultado, 2.718281828459045, places=10)
        
    def test_erros_matematicos(self):
        """Testa tratamento de erros matemáticos."""
        # Divisão por zero
        resultado = self.calc.calcular("10 / 0")
        self.assertIn("Divisão por zero", str(resultado))
        
        # Logaritmo de número negativo
        resultado = self.calc.calcular("log(-1)")
        self.assertIn("Erro", str(resultado))
        
        # Raiz quadrada de número negativo
        resultado = self.calc.calcular("sqrt(-1)")
        self.assertIn("Erro", str(resultado))
        
    def test_validacao_seguranca(self):
        """Testa validação de segurança."""
        # Expressões perigosas
        expressoes_perigosas = [
            "import os",
            "exec('print(1)')",
            "eval('__import__(\"os\")')",
            "open('file.txt')",
            "system('ls')"
        ]
        
        for expr in expressoes_perigosas:
            resultado = self.calc.calcular(expr)
            self.assertIn("inválida", str(resultado).lower())
            
    def test_historico(self):
        """Testa funcionalidade de histórico."""
        # Adiciona alguns cálculos
        self.calc.calcular("2 + 2")
        self.calc.calcular("3 * 4")
        self.calc.calcular("10 / 2")
        
        # Verifica se foram adicionados ao histórico
        self.assertEqual(len(self.calc.historico), 3)
        
        # Verifica estrutura do histórico
        for item in self.calc.historico:
            self.assertIn('expressao', item)
            self.assertIn('resultado', item)
            self.assertIn('timestamp', item)
            
    def test_memoria_variaveis(self):
        """Testa funcionalidade de memória de variáveis."""
        # Simula atribuição de variável
        self.calc.memoria['x'] = 5.0
        self.calc.memoria['y'] = 10.0
        
        # Testa uso de variáveis
        resultado = self.calc.calcular("x + y")
        self.assertEqual(resultado, 15.0)
        
        # Testa variável inexistente
        resultado = self.calc.calcular("z + 1")
        self.assertIn("Erro", str(resultado))
        
    def test_conversoes_unidades(self):
        """Testa conversões de unidades."""
        # Conversão de comprimento
        resultado = self.calc.converter_unidades(1000, 'm', 'km')
        self.assertEqual(resultado, 1.0)
        
        resultado = self.calc.converter_unidades(1, 'km', 'm')
        self.assertEqual(resultado, 1000.0)
        
        # Unidades não suportadas
        resultado = self.calc.converter_unidades(1, 'invalid', 'm')
        self.assertIn("não suportadas", str(resultado))
        
    def test_limpar_historico(self):
        """Testa limpeza do histórico."""
        # Adiciona alguns cálculos
        self.calc.calcular("1 + 1")
        self.calc.calcular("2 + 2")
        
        # Verifica que há histórico
        self.assertEqual(len(self.calc.historico), 2)
        
        # Limpa o histórico
        self.calc.limpar_historico()
        
        # Verifica que está vazio
        self.assertEqual(len(self.calc.historico), 0)
        
    def test_preparar_expressao(self):
        """Testa preparação de expressões."""
        # Testa substituição de símbolos
        expr, namespace = self.calc.preparar_expressao("2^3")
        self.assertEqual(expr, "2**3")
        
        expr, namespace = self.calc.preparar_expressao("5×3")
        self.assertEqual(expr, "5*3")
        
        expr, namespace = self.calc.preparar_expressao("10÷2")
        self.assertEqual(expr, "10/2")
        
        # Verifica se namespace contém funções
        self.assertIn('sin', namespace)
        self.assertIn('cos', namespace)
        self.assertIn('pi', namespace)
        
    def test_limite_historico(self):
        """Testa limite do histórico (50 itens)."""
        # Adiciona mais de 50 cálculos
        for i in range(55):
            self.calc.calcular(f"{i} + 1")
            
        # Verifica que mantém apenas os últimos 50
        self.assertEqual(len(self.calc.historico), 50)
        
        # Verifica que o primeiro item é o 6º cálculo (55 - 50 + 1)
        primeiro_item = self.calc.historico[0]
        self.assertIn("5 + 1", primeiro_item['expressao'])

class TestCalculadoraInterface(unittest.TestCase):
    """Testes para interface da calculadora."""
    
    def setUp(self):
        """Configuração inicial."""
        self.calc = CalculadoraOtimizada()
        
    @patch('builtins.input', return_value='quit')
    @patch('sys.stdout', new_callable=StringIO)
    def test_comando_quit(self, mock_stdout, mock_input):
        """Testa comando de saída."""
        with self.assertRaises(SystemExit):
            self.calc.executar()
            
    @patch('builtins.input', side_effect=['2 + 2', 'quit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_calculo_interativo(self, mock_stdout, mock_input):
        """Testa cálculo interativo."""
        try:
            self.calc.executar()
        except SystemExit:
            pass
            
        output = mock_stdout.getvalue()
        self.assertIn("Resultado: 4.0", output)
        
    @patch('builtins.input', side_effect=['hist', 'quit'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_comando_historico(self, mock_stdout, mock_input):
        """Testa comando de histórico."""
        try:
            self.calc.executar()
        except SystemExit:
            pass
            
        output = mock_stdout.getvalue()
        self.assertIn("Histórico vazio", output)

def run_tests():
    """Executa todos os testes."""
    # Configura o test runner
    loader = unittest.TestLoader()
    suite = loader.discover('.', pattern='test_*.py')
    
    # Executa os testes
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Retorna código de saída
    return 0 if result.wasSuccessful() else 1

if __name__ == '__main__':
    print("🧪 Executando testes da Calculadora Otimizada...")
    print("=" * 50)
    
    exit_code = run_tests()
    
    print("=" * 50)
    if exit_code == 0:
        print("✅ Todos os testes passaram!")
    else:
        print("❌ Alguns testes falharam!")
        
    sys.exit(exit_code) 