# Steam Fun AI

Este projeto Python interage com as APIs da Steam e do Google Gemini para gerar textos divertidos e personalizados sobre o perfil de jogos de um usuário da Steam. Ele recupera informações como o nickname do usuário, o número total de jogos e os jogos mais jogados, e então utiliza inteligência artificial para criar uma descrição bem-humorada baseada nesses dados.


## Funcionalidades

- **Integração com a API da Steam:** Obtém dados do perfil do usuário, incluindo lista de jogos e tempo de jogo.
- **Integração com a API Google Gemini:** Utiliza um modelo de IA generativa para criar textos criativos e engraçados.
- **Análise de Perfil de Jogador:** Identifica o nickname do usuário, a quantidade de jogos e os jogos mais jogados com suas respectivas horas.
- **Geração de Conteúdo Personalizado:** Gera um texto único e divertido, adaptado às estatísticas de jogo do usuário.


## Como Usar

Para utilizar este projeto, siga os passos abaixo:

### 1. Pré-requisitos

Certifique-se de ter o Python instalado em sua máquina. Este projeto foi desenvolvido com Python 3.x.

### 2. Instalação das Dependências

Instale as bibliotecas necessárias utilizando `pip`:

```bash
pip install requests google-generativeai
```

### 3. Obtenção das Chaves de API

Você precisará de duas chaves de API:

-   **Steam Web API Key:**
    1.  Acesse [https://steamcommunity.com/dev/apikey](https://steamcommunity.com/dev/apikey).
    2.  Faça login com sua conta Steam.
    3.  Registre um domínio (pode ser qualquer um, como `localhost` ou o nome do seu projeto).
    4.  Copie a chave gerada.

-   **Google Gemini API Key:**
    1.  Acesse [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey).
    2.  Faça login com sua conta Google.
    3.  Crie uma nova chave de API ou utilize uma existente.
    4.  Copie a chave gerada.

### 4. Executando o Projeto

1.  Salve o código fornecido (o arquivo `pasted_content.txt` que você me enviou) como `main.py` (ou qualquer outro nome de sua preferência) no seu computador.
2.  Abra o terminal ou prompt de comando na pasta onde você salvou o arquivo.
3.  Execute o script:

    ```bash
    python main.py
    ```

4.  O script solicitará que você insira sua **KEY da API da Steam** e o **ID da conta da Steam** (SteamID64) que deseja analisar. Você pode encontrar seu SteamID64 em sites como [SteamID I/O](https://steamid.io/).
5.  Em seguida, ele pedirá sua **Key do Gemini 2.5-Flash**.
6.  Após fornecer as informações, o programa processará os dados e exibirá o texto divertido gerado pela IA.




## Estrutura do Código

O código é composto por duas funções principais:

-   `Steam()`:
    -   Responsável por interagir com a API da Steam.
    -   Solicita a chave da API da Steam e o SteamID do usuário.
    -   Busca informações sobre os jogos do usuário e seu perfil.
    -   Calcula o tempo de jogo dos títulos mais jogados.
    -   Retorna o nickname do usuário, a quantidade de jogos e os dados dos jogos mais jogados.
    -   Inclui tratamento de erros para chaves inválidas ou perfis privados.

-   `ConsultaIA()`:
    -   Responsável por interagir com a API do Google Gemini.
    -   Solicita a chave da API do Gemini.
    -   Configura o modelo `gemini-2.5-flash`.
    -   Cria um prompt dinâmico com base nos dados do usuário da Steam.
    -   Gera e imprime o texto divertido utilizando o modelo de IA.

O fluxo principal do programa chama `Steam()` para obter os dados e, em seguida, `ConsultaIA()` para gerar o texto com base nesses dados.# SteamFunIA
