# Sistema Seguro de Comunicação

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

## Estrutura do Repositório

/sistema-seguro-comunicacao │── README.md ← Explicação inicial do projeto │── /docs ← Armazena documentos do planejamento │ ├── esboco_projeto.md ← Documento com o objetivo e tecnologias do projeto │ ├── proposta_implementacao.md ← Explicação das tecnologias e etapas de implementação │ └── funcionalidades.md ← Descrição das funcionalidades do sistema │── /diagrams ← Guarda fluxogramas e desenhos do sistema │ └── fluxo_sistema.png ← Fluxograma básico do sistema │── /src ← Pasta para código-fonte


## Fluxo Básico do Sistema

1. **Cadastro de Usuário**: O usuário se cadastra, e sua senha é protegida com bcrypt.
2. **Login**: O usuário faz login e, caso a senha esteja correta, um Token JWT é gerado para autenticação.
3. **Envio de Mensagem**: O usuário envia uma mensagem, que é criptografada com AES (CBC).
4. **Recebimento de Mensagem**: O destinatário usa sua chave RSA para descriptografar a chave AES e acessar a mensagem.

## Como Executar

1. Clone este repositório:
    ```bash
    git clone https://github.com/SEU_USUARIO/sistema-seguro-comunicacao.git
    ```

2. Instale as dependências:
    ```bash
    pip install -r requirements.txt
    ```

3. Execute o sistema (exemplo de execução):
    ```bash
    python src/main.py
    ```

## Documentação

1. **Esboço do Projeto**: [docs/esboco_projeto.md](docs/esboco_projeto.md)
2. **Proposta de Implementação**: [docs/proposta_implementacao.md](docs/proposta_implementacao.md)
3. **Funcionalidades**: [docs/funcionalidades.md](docs/funcionalidades.md)

## Licença

Este projeto é licenciado sob a MIT License - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

