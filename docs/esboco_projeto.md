# Esboço do Projeto  

## Objetivo  
Este projeto tem como objetivo garantir a segurança da comunicação entre funcionários de uma empresa, protegendo mensagens sensíveis contra acessos não autorizados. Para isso, serão utilizados métodos modernos de criptografia e autenticação, assegurando a integridade e confidencialidade dos dados.  

## Tecnologias Utilizadas  
As seguintes tecnologias serão aplicadas para garantir a segurança do sistema:  

✅ **[bcrypt (v4.2.1)](https://pypi.org/project/bcrypt/4.2.1/)** → Para hashing seguro de senhas, protegendo credenciais armazenadas.  
✅ **[PyJWT (v2.10.1)](https://pyjwt.readthedocs.io/en/stable/)** → Para autenticação via Tokens JWT, garantindo acesso seguro ao sistema.  
✅ **[cryptography (v42.0.0)](https://pypi.org/project/cryptography/)** → Para implementação da criptografia simétrica (AES) e assimétrica (RSA).  
✅ **hashlib, base64, os** → Para suporte auxiliar em operações de criptografia e manipulação de dados.  

## Fluxo Básico do Sistema  
1. **Cadastro de Usuário** → A senha fornecida pelo usuário é armazenada com bcrypt, garantindo que não seja salva em texto puro.  
2. **Login** → O usuário se autentica e recebe um Token JWT, que será utilizado para acessar funcionalidades seguras.  
3. **Envio de Mensagem** → A mensagem é criptografada com AES antes de ser armazenada, garantindo privacidade.  
4. **Descriptografia** → Apenas o destinatário correto pode descriptografar a mensagem utilizando sua chave privada RSA.  

Este fluxo garante que as mensagens sejam protegidas contra acessos não autorizados e que a autenticação dos usuários seja segura.  
