# Sistema Seguro de Comunicação 🔒
![Python](https://img.shields.io/badge/Python-v3.10.0-%2338BDF8)
![Last Commit](https://img.shields.io/github/last-commit/leoferamos/sistema-seguro-comunicacao)
![Project Status](https://img.shields.io/badge/Status-Andamento-yellow)



## Descrição do Projeto

Este projeto tem como objetivo implementar criptografia e autenticação segura em um sistema de comunicação interna para uma empresa. O foco é garantir a segurança das credenciais dos usuários e das mensagens trocadas, utilizando métodos modernos de criptografia e autenticação.

### Tecnologias Utilizadas:
- **bcrypt**: Para hashing seguro de senhas.
- **PyJWT**: Para autenticação via Tokens JWT.
- **cryptography**: Para implementar criptografia simétrica (AES) e assimétrica (RSA).
- **hashlib, base64, os**: Suporte auxiliar para criptografia e manipulação de dados.

### Funcionalidades Implementadas:
- **Cadastro de Usuário**: A senha do usuário é armazenada de forma segura, utilizando hashing com o algoritmo bcrypt.
- **Login**: O sistema autentica o usuário e gera um Token JWT caso as credenciais estejam corretas.
- **Envio de Mensagens**: As mensagens enviadas são criptografadas utilizando AES antes de serem armazenadas.
- **Recebimento de Mensagens**: O destinatário correto pode descriptografar a mensagem utilizando sua chave RSA, garantindo a segurança do conteúdo.

## Fluxo Básico do Sistema

1. **Cadastro de Usuário**: O usuário se cadastra, e sua senha é protegida com bcrypt.
2. **Login**: O usuário faz login e, caso a senha esteja correta, um Token JWT é gerado para autenticação.
3. **Envio de Mensagem**: O usuário envia uma mensagem, que é criptografada com AES (CBC).
4. **Recebimento de Mensagem**: O destinatário usa sua chave RSA para descriptografar a chave AES e acessar a mensagem.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/leoferamos/sistema-seguro-comunicacao.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o sistema:
    ```bash
    python main.py
    ```

## Documentação

1. **Esboço do Projeto**: [docs/esboco_projeto.md](docs/esboco_projeto.md)
2. **Proposta de Implementação**: [docs/proposta_implementacao.md](docs/proposta_implementacao.md)
3. **Funcionalidades**: [docs/funcionalidades.md](docs/funcionalidades.md)

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

