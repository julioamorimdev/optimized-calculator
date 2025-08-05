# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para a **Calculadora Otimizada**! Este documento fornece diretrizes e informações importantes para contribuidores.

## 📋 Índice

- [Como Contribuir](#como-contribuir)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Padrões de Código](#padrões-de-código)
- [Processo de Pull Request](#processo-de-pull-request)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Funcionalidades](#sugerindo-funcionalidades)
- [Código de Conduta](#código-de-conduta)

## 🚀 Como Contribuir

### Tipos de Contribuição

- 🐛 **Bug fixes** - Correção de problemas existentes
- ✨ **Novas funcionalidades** - Adição de recursos
- 📚 **Documentação** - Melhorias na documentação
- 🧪 **Testes** - Adição ou melhoria de testes
- 🎨 **Interface** - Melhorias na interface do usuário
- 🔧 **Refatoração** - Melhorias no código existente
- ⚡ **Performance** - Otimizações de performance

### Antes de Começar

1. **Verifique se já existe uma issue** relacionada ao que você quer fazer
2. **Leia a documentação** do projeto
3. **Familiarize-se** com o código existente
4. **Discuta grandes mudanças** em uma issue antes de implementar

## 🔧 Configuração do Ambiente

### Pré-requisitos

- Python 3.7 ou superior
- Git
- Editor de código (VS Code, PyCharm, etc.)

### Configuração Inicial

1. **Fork o repositório**
```bash
# Vá para https://github.com/seu-usuario/optimized-calculator
# Clique em "Fork"
```

2. **Clone seu fork**
```bash
git clone https://github.com/seu-usuario/optimized-calculator.git
cd optimized-calculator
```

3. **Configure o upstream**
```bash
git remote add upstream https://github.com/original-owner/optimized-calculator.git
```

4. **Crie um ambiente virtual**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate
```

5. **Instale dependências**
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt  # Para desenvolvimento
```

### Estrutura do Projeto

```
optimized-calculator/
├── calculadora.py          # Código principal
├── index.html              # Interface web
├── test_calculadora.py     # Testes
├── requirements.txt        # Dependências
├── requirements-dev.txt    # Dependências de desenvolvimento
├── docs/                   # Documentação
├── examples/               # Exemplos de uso
└── README.md              # Documentação principal
```

## 📝 Padrões de Código

### Python

- **PEP 8** - Siga as convenções de estilo do Python
- **Type hints** - Use type hints quando apropriado
- **Docstrings** - Documente todas as funções e classes
- **Nomes descritivos** - Use nomes claros para variáveis e funções

### Exemplo de Código

```python
from typing import Union, List, Dict, Any

def calcular_expressao(expressao: str) -> Union[float, str]:
    """
    Calcula o resultado de uma expressão matemática.
    
    Args:
        expressao (str): Expressão matemática para calcular
        
    Returns:
        Union[float, str]: Resultado do cálculo ou mensagem de erro
        
    Raises:
        ValueError: Se a expressão for inválida
    """
    try:
        # Validação da entrada
        if not expressao.strip():
            return "Erro: Expressão vazia"
            
        # Processamento
        resultado = eval(expressao, {"__builtins__": {}}, {})
        return float(resultado)
        
    except Exception as e:
        return f"Erro: {str(e)}"
```

### HTML/CSS/JavaScript

- **HTML5 semântico** - Use tags apropriadas
- **CSS organizado** - Mantenha o CSS bem estruturado
- **JavaScript modular** - Separe responsabilidades
- **Responsividade** - Garanta que funcione em dispositivos móveis

## 🔄 Processo de Pull Request

### 1. Preparação

```bash
# Atualize seu fork
git fetch upstream
git checkout main
git merge upstream/main

# Crie uma branch para sua feature
git checkout -b feature/nova-funcionalidade
```

### 2. Desenvolvimento

- **Faça commits pequenos e frequentes**
- **Use mensagens de commit descritivas**
- **Teste suas mudanças**
- **Mantenha o código limpo**

### 3. Mensagens de Commit

Use o formato convencional:

```
tipo(escopo): descrição curta

Corpo da mensagem (opcional)

Rodapé (opcional)
```

**Tipos:**
- `feat`: Nova funcionalidade
- `fix`: Correção de bug
- `docs`: Documentação
- `style`: Formatação
- `refactor`: Refatoração
- `test`: Testes
- `chore`: Tarefas de manutenção

**Exemplos:**
```
feat(calculator): adiciona função de conversão de unidades
fix(web): corrige erro de cálculo em expressões complexas
docs(readme): atualiza instruções de instalação
```

### 4. Pull Request

1. **Push suas mudanças**
```bash
git push origin feature/nova-funcionalidade
```

2. **Crie o Pull Request**
   - Vá para o GitHub
   - Clique em "New Pull Request"
   - Selecione sua branch
   - Preencha o template

3. **Template do Pull Request**
```markdown
## Descrição
Breve descrição das mudanças

## Tipo de Mudança
- [ ] Bug fix
- [ ] Nova funcionalidade
- [ ] Documentação
- [ ] Teste
- [ ] Refatoração

## Testes
- [ ] Testes unitários passando
- [ ] Testes de integração passando
- [ ] Interface testada

## Checklist
- [ ] Código segue os padrões do projeto
- [ ] Documentação atualizada
- [ ] Testes adicionados/atualizados
- [ ] Não quebra funcionalidades existentes
```

## 🐛 Reportando Bugs

### Antes de Reportar

1. **Verifique se já existe uma issue**
2. **Teste na versão mais recente**
3. **Reproduza o problema**

### Template de Bug Report

```markdown
## Descrição do Bug
Descrição clara e concisa do problema

## Passos para Reproduzir
1. Vá para '...'
2. Clique em '...'
3. Digite '...'
4. Veja o erro

## Comportamento Esperado
O que deveria acontecer

## Comportamento Atual
O que realmente acontece

## Screenshots
Se aplicável, adicione screenshots

## Ambiente
- OS: [ex: Windows 10]
- Python: [ex: 3.9.0]
- Versão: [ex: 2.0.0]

## Informações Adicionais
Qualquer contexto adicional
```

## 💡 Sugerindo Funcionalidades

### Template de Feature Request

```markdown
## Descrição da Funcionalidade
Descrição clara da nova funcionalidade

## Problema que Resolve
Qual problema esta funcionalidade resolve?

## Solução Proposta
Como você sugere implementar?

## Alternativas Consideradas
Outras soluções que você considerou

## Contexto Adicional
Qualquer contexto adicional
```

## 📋 Código de Conduta

### Nossos Padrões

- **Seja respeitoso** - Trate todos com respeito
- **Seja construtivo** - Critique ideias, não pessoas
- **Seja inclusivo** - Bem-vindo a todos os níveis de experiência
- **Seja colaborativo** - Trabalhe em conjunto

### Comportamentos Inaceitáveis

- Linguagem ofensiva ou discriminatória
- Assédio ou bullying
- Spam ou propaganda
- Violação de privacidade

### Como Reportar

Se você testemunhar ou sofrer comportamento inaceitável:
- Envie um email para: [email@exemplo.com]
- Ou abra uma issue privada no GitHub

## 🏆 Reconhecimento

Contribuidores serão reconhecidos de várias formas:

- **Mencionados no README**
- **Listados nos releases**
- **Badges de contribuidor**
- **Agradecimentos especiais**

## 📞 Suporte

Se você tiver dúvidas sobre contribuição:

- **Issues**: Para bugs e funcionalidades
- **Discussions**: Para perguntas gerais
- **Email**: Para assuntos privados
- **Documentação**: Para informações técnicas

## 🙏 Agradecimentos

Obrigado por contribuir para tornar a Calculadora Otimizada melhor para todos!

---

**Lembre-se**: Cada contribuição, por menor que seja, é valiosa e apreciada! 🎉 