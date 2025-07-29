# test_linkedin.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pytest
import time

# URL da página do LinkedIn a ser testada
LINKEDIN_URL = "https://www.linkedin.com/in/lucas-teixeira-67b08b47/"
# Nome que será pesquisado no corpo da página
NOME_PESQUISADO = "Lucas Teixeira"

# Fixture do pytest que inicializa o navegador Chrome antes do teste e fecha após
@pytest.fixture
def driver():
    print("Iniciando o ChromeDriver...")
    service = Service("C:/chromedriver/chromedriver.exe")  # Caminho para o ChromeDriver
    driver = webdriver.Chrome(service=service)
    yield driver  # Fornece o driver para o teste
    print("Encerrando o ChromeDriver...")
    driver.quit()  # Fecha o navegador após o teste

# Teste automatizado que verifica se o nome aparece na página do LinkedIn
def test_pesquisa_nome_linkedin(driver):
    print("Iniciando teste...")
    print(f"Abrindo URL: {LINKEDIN_URL}")
    driver.get(LINKEDIN_URL)
    print("Página carregada!")
    
    time.sleep(5)  # Espera fixa para garantir que a página foi completamente carregada
    body_text = driver.find_element(By.TAG_NAME, "body").text
    print("Texto da página capturado.")
    
    assert NOME_PESQUISADO in body_text, f"Nome '{NOME_PESQUISADO}' não encontrado na página!"
    print(f"Teste realizado com sucesso: '{NOME_PESQUISADO}' foi encontrado na página.")

# main
if __name__ == "__main__":
    import sys
    import datetime

    # Roda o teste e salva o código de saída
    resultado = pytest.main(["-v", "test_linkedin.py"])

    # Cria um resumo no txt com data/hora e resultado
    with open("resumo_resultado.txt", "w") as f:
        f.write(f"Execução: {datetime.datetime.now()}\n")
        f.write(f"Resultado do teste: {'SUCESSO' if resultado == 0 else 'FALHA'}\n")
