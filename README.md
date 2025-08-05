# 🧮 Calculadora Otimizada

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Version](https://img.shields.io/badge/Version-2.0.0-orange.svg)](VERSION)

Uma calculadora avançada em Python com interface moderna, funcionalidades matemáticas completas e recursos adicionais como histórico, memória de variáveis e conversões de unidades.

## ✨ Funcionalidades

### 🔢 Operações Básicas
- **Adição, Subtração, Multiplicação, Divisão**
- **Potenciação** (`**`)
- **Módulo** (`%`)
- **Parênteses** para precedência

### 📐 Funções Matemáticas Avançadas
- **Trigonométricas**: `sin()`, `cos()`, `tan()`, `asin()`, `acos()`, `atan()`
- **Logarítmicas**: `log()` (base 10), `ln()` (natural)
- **Exponenciais**: `exp()`
- **Raiz quadrada**: `sqrt()`
- **Valor absoluto**: `abs()`
- **Arredondamento**: `round()`, `floor()`, `ceil()`

### 🔢 Constantes Matemáticas
- **π (Pi)**: `pi`
- **e (Número de Euler)**: `e`

### 💾 Recursos Adicionais
- **Histórico de cálculos** (últimos 50)
- **Memória de variáveis** (armazenamento temporário)
- **Conversões de unidades** (comprimento, peso, temperatura)
- **Interface colorida** com emojis
- **Validação de segurança** contra código malicioso
- **Tratamento robusto de erros**

### 🎯 Comandos Especiais
- `hist` - Visualizar histórico
- `mem` - Visualizar memória
- `clear` - Limpar histórico
- `help` - Exibir ajuda
- `quit` - Sair da calculadora

## 🚀 Instalação

### Pré-requisitos
- Python 3.7 ou superior
- Sistema operacional: Windows, macOS ou Linux

### Instalação Rápida

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/optimized-calculator.git
cd optimized-calculator
```

2. **Execute a calculadora:**
```bash
python calculadora.py
```

### Instalação via pip (futuro)
```bash
pip install optimized-calculator
```

## 📖 Como Usar

### Execução Básica
```bash
python calculadora.py
```

### Exemplos de Uso

#### Operações Básicas
```
🔢 Digite uma expressão ou comando: 2 + 3 * 4
📊 Resultado: 14.0

🔢 Digite uma expressão ou comando: (10 + 5) / 3
📊 Resultado: 5.0
```

#### Funções Matemáticas
```
🔢 Digite uma expressão ou comando: sin(pi/2)
📊 Resultado: 1.0

🔢 Digite uma expressão ou comando: sqrt(16)
📊 Resultado: 4.0

🔢 Digite uma expressão ou comando: log(100)
📊 Resultado: 2.0
```

#### Variáveis em Memória
```
🔢 Digite uma expressão ou comando: x = 5
✅ x = 5.0

🔢 Digite uma expressão ou comando: y = x * 2
✅ y = 10.0

🔢 Digite uma expressão ou comando: x + y
📊 Resultado: 15.0
```

#### Comandos Especiais
```
🔢 Digite uma expressão ou comando: hist
📋 HISTÓRICO DE CÁLCULOS:
============================================================
 1. 2 + 3 * 4 = 14.0
 2. sin(pi/2) = 1.0
 3. x = 5 = 5.0
============================================================

🔢 Digite uma expressão ou comando: mem
💾 VARIÁVEIS EM MEMÓRIA:
========================================
x = 5.0
y = 10.0
========================================
```

## 🌐 Interface Web

Para testar a calculadora via navegador, abra o arquivo `index.html` em qualquer navegador moderno:

```bash
# No Windows
start index.html

# No macOS
open index.html

# No Linux
xdg-open index.html
```

A interface web oferece:
- Interface gráfica intuitiva
- Botões para todas as operações
- Histórico visual
- Responsivo para dispositivos móveis

## 🛡️ Segurança

A calculadora implementa várias medidas de segurança:

- **Validação de entrada**: Verifica caracteres permitidos
- **Filtro de palavras-chave**: Bloqueia comandos perigosos
- **Namespace isolado**: Previne acesso a funções do sistema
- **Tratamento de exceções**: Captura e trata erros adequadamente

## 🧪 Testes

Execute os testes automatizados:

```bash
python -m pytest tests/
```

Ou execute o arquivo de teste manual:

```bash
python test_calculadora.py
```

## 📁 Estrutura do Projeto

```
optimized-calculator/
├── calculadora.py          # Arquivo principal
├── index.html              # Interface web
├── test_calculadora.py     # Testes automatizados
├── requirements.txt        # Dependências
├── LICENSE                 # Licença MIT
├── CONTRIBUTING.md         # Guia de contribuição
├── CHANGELOG.md           # Histórico de mudanças
├── VERSION                # Versão atual
└── README.md              # Este arquivo
```

## 🔧 Desenvolvimento

### Configuração do Ambiente
```bash
# Clone o repositório
git clone https://github.com/seu-usuario/optimized-calculator.git
cd optimized-calculator

# Crie um ambiente virtual (opcional)
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows

# Instale dependências de desenvolvimento
pip install -r requirements-dev.txt
```

### Executar Testes
```bash
# Testes unitários
python -m pytest tests/

# Testes com cobertura
python -m pytest --cov=calculadora tests/

# Testes de estilo
flake8 calculadora.py
black calculadora.py
```

## 🤝 Contribuindo

Contribuições são bem-vindas! Por favor, leia o [CONTRIBUTING.md](CONTRIBUTING.md) para detalhes sobre como contribuir.

### Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

### Tipos de Contribuição

- 🐛 **Bug fixes**
- ✨ **Novas funcionalidades**
- 📚 **Melhorias na documentação**
- 🧪 **Testes adicionais**
- 🎨 **Melhorias na interface**

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- Comunidade Python
- Contribuidores do projeto
- Bibliotecas open source utilizadas

## 📞 Suporte

Se você encontrar algum problema ou tiver sugestões:

- 📧 **Email**: seu-email@exemplo.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/seu-usuario/optimized-calculator/issues)
- 💬 **Discussions**: [GitHub Discussions](https://github.com/seu-usuario/optimized-calculator/discussions)

## 📈 Roadmap

- [ ] Interface gráfica com tkinter
- [ ] Mais funções matemáticas
- [ ] Gráficos e visualizações
- [ ] Integração com APIs externas
- [ ] Modo científico avançado
- [ ] Suporte a matrizes
- [ ] Cálculos estatísticos
- [ ] Exportação de resultados

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela no repositório!**
