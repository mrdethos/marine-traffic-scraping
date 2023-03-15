# Scraping de dados (Marine Traffic) para ANTAQ
### Descrição
Este script Python usa o Jupyter Notebook para:
1. Fazer scraping dos dados de navios de uma API externa e armazenar os dados em um arquivo JSON.
2. Ler os dados do arquivo JSON e criar uma lista de objetos Navio.
3. Navegar até um site e preencher um formulário com os dados dos navios.

### Dependências
Este projeto requer a instalação dos seguintes pacotes:
* requests
* xmltodict
* selenium
* webdriver_manager

### Instalação
1. Clone este repositório: git clone https://github.com/seunome/projetonavios.git
2. Instale as dependências: pip install requests xmltodict selenium webdriver_manager

### Configuração
Antes de executar o projeto, é necessário fornecer a sua chave para acessar a API do MarineTraffic. Para isso, altere o valor da variável api_url no arquivo scraping.ipynb.
Caso não possua uma chave, os dados poderão ser obtidos através da célula que extrai diretamente os dados do site MarineTraffic.

### Nota
Este projeto foi criado apenas para fins educacionais. O uso indevido das informações obtidas por meio do scraping pode violar a lei e a ética. O autor não assume nenhuma responsabilidade pelo uso indevido deste código.
