# Sistema Seguro de Comunicação 🔒
![Python](https://img.shields.io/badge/Python-v3.10.0-%2338BDF8)
![Last Commit](https://img.shields.io/github/last-commit/leoferamos/sistema-seguro-comunicacao)
![Project Status](https://img.shields.io/badge/Status-Andamento-yellow)

## Descrição do Projeto

Este projeto tem como objetivo implementar criptografia e autenticação segura em um sistema de comunicação interna para uma empresa. O foco é garantir a segurança das credenciais dos usuários e das mensagens trocadas, utilizando métodos modernos de criptografia e autenticação.

## Requisitos

- Python 3.x
- pip (Python package installer)

## Instalação

1. Clone este repositório:
    ```sh
    git clone https://github.com/leoferamos/sistema-seguro-comunicacao.git
    cd sistema-seguro-comunicacao
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):
    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

## Uso

1. Execute o script principal:
    ```sh
    python src/main.py
    ```

2. Siga as instruções no terminal para registrar um novo usuário, fazer login, listar usuários ou sair.

## Bibliotecas Utilizadas

- `bcrypt`: Para hashing de senhas.
- `pyotp`: Para geração e verificação de códigos TOTP.
- `qrcode`: Para geração de códigos QR.
- `pillow`: Biblioteca de suporte para `qrcode`.
- `python-dotenv`: Para carregar variáveis de ambiente de um arquivo `.env`.

## Segurança

- As senhas são armazenadas de forma segura usando hashing com `bcrypt`.
- A autenticação multifator (MFA) é implementada usando TOTP com o Microsoft Authenticator.
- Tokens JWT são usados para autenticação de sessões.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

## Documentação

1. **Esboço do Projeto**: [docs/esboco_projeto.md](docs/esboco_projeto.md)
2. **Proposta de Implementação**: [docs/proposta_implementacao.md](docs/proposta_implementacao.md)
3. **Funcionalidades**: [docs/funcionalidades.md](docs/funcionalidades.md)

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

