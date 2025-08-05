# Makefile para Calculadora Otimizada
# Autor: Calculadora Team
# Versão: 2.0.0

.PHONY: help install test run clean lint format docs examples web

# Variáveis
PYTHON = python3
PIP = pip3
PROJECT_NAME = calculadora-otimizada
VERSION = 2.0.0

# Cores para output
RED = \033[0;31m
GREEN = \033[0;32m
YELLOW = \033[1;33m
BLUE = \033[0;34m
PURPLE = \033[0;35m
CYAN = \033[0;36m
WHITE = \033[1;37m
NC = \033[0m # No Color

help: ## Mostra esta ajuda
	@echo "$(CYAN)🧮 Calculadora Otimizada - Comandos Disponíveis$(NC)"
	@echo "$(YELLOW)================================================$(NC)"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "$(GREEN)%-15s$(NC) %s\n", $$1, $$2}'

install: ## Instala dependências do projeto
	@echo "$(BLUE)📦 Instalando dependências...$(NC)"
	$(PIP) install -r requirements.txt
	@echo "$(GREEN)✅ Dependências instaladas com sucesso!$(NC)"

install-dev: ## Instala dependências de desenvolvimento
	@echo "$(BLUE)🔧 Instalando dependências de desenvolvimento...$(NC)"
	$(PIP) install -r requirements-dev.txt
	@echo "$(GREEN)✅ Dependências de desenvolvimento instaladas!$(NC)"

run: ## Executa a calculadora
	@echo "$(PURPLE)🚀 Iniciando Calculadora Otimizada...$(NC)"
	$(PYTHON) calculadora.py

test: ## Executa os testes
	@echo "$(YELLOW)🧪 Executando testes...$(NC)"
	$(PYTHON) test_calculadora.py

test-coverage: ## Executa testes com cobertura
	@echo "$(YELLOW)🧪 Executando testes com cobertura...$(NC)"
	$(PIP) install pytest-cov
	$(PYTHON) -m pytest --cov=calculadora --cov-report=html --cov-report=term

lint: ## Executa verificação de estilo de código
	@echo "$(BLUE)🔍 Verificando estilo de código...$(NC)"
	$(PIP) install flake8 black
	flake8 calculadora.py test_calculadora.py examples.py
	@echo "$(GREEN)✅ Verificação de estilo concluída!$(NC)"

format: ## Formata o código automaticamente
	@echo "$(BLUE)🎨 Formatando código...$(NC)"
	$(PIP) install black
	black calculadora.py test_calculadora.py examples.py
	@echo "$(GREEN)✅ Código formatado!$(NC)"

docs: ## Gera documentação
	@echo "$(BLUE)📚 Gerando documentação...$(NC)"
	@echo "$(YELLOW)Documentação disponível em:$(NC)"
	@echo "  - README.md"
	@echo "  - CONTRIBUTING.md"
	@echo "  - CHANGELOG.md"
	@echo "  - LICENSE"

examples: ## Executa exemplos de uso
	@echo "$(PURPLE)💡 Executando exemplos...$(NC)"
	$(PYTHON) examples.py

web: ## Abre a interface web no navegador
	@echo "$(CYAN)🌐 Abrindo interface web...$(NC)"
	@if command -v xdg-open > /dev/null; then \
		xdg-open index.html; \
	elif command -v open > /dev/null; then \
		open index.html; \
	else \
		echo "$(YELLOW)Abra o arquivo index.html no seu navegador$(NC)"; \
	fi

clean: ## Limpa arquivos temporários
	@echo "$(RED)🧹 Limpando arquivos temporários...$(NC)"
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name "htmlcov" -exec rm -rf {} +
	rm -rf build/ dist/ *.egg-info/
	@echo "$(GREEN)✅ Limpeza concluída!$(NC)"

check: ## Executa verificações de qualidade
	@echo "$(BLUE)🔍 Executando verificações de qualidade...$(NC)"
	@make lint
	@make test
	@echo "$(GREEN)✅ Todas as verificações passaram!$(NC)"

setup: ## Configura o ambiente de desenvolvimento
	@echo "$(BLUE)⚙️ Configurando ambiente de desenvolvimento...$(NC)"
	@make install-dev
	@make format
	@echo "$(GREEN)✅ Ambiente configurado!$(NC)"

version: ## Mostra a versão atual
	@echo "$(CYAN)📋 Versão atual: $(VERSION)$(NC)"

package: ## Cria pacote de distribuição
	@echo "$(BLUE)📦 Criando pacote...$(NC)"
	$(PYTHON) setup.py sdist bdist_wheel
	@echo "$(GREEN)✅ Pacote criado!$(NC)"

install-local: ## Instala o projeto localmente
	@echo "$(BLUE)📦 Instalando projeto localmente...$(NC)"
	$(PIP) install -e .
	@echo "$(GREEN)✅ Projeto instalado!$(NC)"

uninstall: ## Remove instalação local
	@echo "$(RED)🗑️ Removendo instalação local...$(NC)"
	$(PIP) uninstall $(PROJECT_NAME) -y
	@echo "$(GREEN)✅ Projeto removido!$(NC)"

# Comandos específicos para Windows
ifeq ($(OS),Windows_NT)
web:
	@echo "$(CYAN)🌐 Abrindo interface web...$(NC)"
	start index.html
endif

# Comandos específicos para macOS
ifeq ($(shell uname),Darwin)
web:
	@echo "$(CYAN)🌐 Abrindo interface web...$(NC)"
	open index.html
endif

# Comandos específicos para Linux
ifeq ($(shell uname),Linux)
web:
	@echo "$(CYAN)🌐 Abrindo interface web...$(NC)"
	xdg-open index.html
endif 