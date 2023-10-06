## Requisitos de Ambiente

Para executar este projeto de Machine Learning, você precisará configurar um ambiente Python com as seguintes dependências:

- Python 3.7 ou superior
- Bibliotecas Python (listadas em `requirements.txt`)

### Configurando um Ambiente Virtual

Recomendamos o uso de um ambiente virtual para isolar as dependências deste projeto e evitar conflitos com outras bibliotecas Python em seu sistema.

Para criar um ambiente virtual, siga estas etapas:

1. Abra um terminal e navegue até o diretório raiz do projeto.

2. Execute o seguinte comando para criar um ambiente virtual chamado "venv" (você pode escolher um nome diferente, se preferir):

   python -m venv venv


3. Ative o ambiente virtual:

- No Windows:
  ```
  venv\Scripts\activate
  ```

- No macOS e Linux:
  ```
  source venv/bin/activate
  ```

### Instalando Dependências

Dentro do ambiente virtual, instale as dependências do projeto usando o comando pip:

pip install -r requirements.txt


Isso instalará todas as bibliotecas Python necessárias listadas no arquivo `requirements.txt`.

### Verificando a Instalação

Para verificar se todas as dependências foram instaladas corretamente, você pode executar o seguinte comando:

python -m pip freeze


Isso exibirá uma lista das bibliotecas Python e suas versões instaladas no ambiente virtual.


