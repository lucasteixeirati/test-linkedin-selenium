# Teste Automatizado com Selenium e Python

Este repositório contém um exemplo básico de teste automatizado usando Python com a biblioteca Selenium e o framework Pytest.

## 💡 Objetivo

Verificar automaticamente se um nome específico aparece no conteúdo de uma página do LinkedIn, simulando a navegação em um navegador real.

## 🛠️ Requisitos

- Python 3.8+
- Google Chrome instalado
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) compatível com a versão do seu Chrome
- Pacotes Python:
  - `selenium`
  - `pytest`

## 🧪 Como executar o teste

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/seu-repo.git
cd seu-repo


pip install -r requirements.txt

service = Service("C:/chromedriver/chromedriver.exe")

pytest -v test_linkedin.py

