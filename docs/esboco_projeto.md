# Esboço do Projeto

## Objetivo  
O objetivo deste projeto é garantir a segurança da comunicação entre funcionários de uma empresa, protegendo mensagens sensíveis contra acessos não autorizados. Para isso, será desenvolvido um sistema interno que implementa métodos modernos de autenticação e criptografia, garantindo a confidencialidade, integridade e autenticidade das informações.

## Tecnologias Utilizadas  
Para alcançar os requisitos de segurança do sistema, utilizaremos as seguintes tecnologias:

- **bcrypt** → Para hashing seguro de senhas, garantindo que senhas armazenadas não possam ser recuperadas em caso de vazamento de dados.  
- **PyJWT** → Para autenticação via Tokens JWT, permitindo que usuários autenticados possam acessar o sistema de forma segura.  
- **cryptography** → Para implementar criptografia simétrica (AES) e assimétrica (RSA), garantindo a proteção das mensagens armazenadas.  

## Fluxo Básico do Sistema  
O sistema seguirá as seguintes etapas para garantir a segurança das comunicações:

1. **Cadastro de usuário** → A senha fornecida pelo usuário será armazenada de forma segura, utilizando bcrypt para hashing.  
2. **Login** → O usuário autentica-se no sistema, e se as credenciais estiverem corretas, um Token JWT é gerado para permitir o acesso.  
3. **Envio de mensagem** → A mensagem será criptografada utilizando AES antes de ser armazenada no sistema.  
4. **Recebimento e leitura da mensagem** → Apenas o destinatário correto poderá descriptografar a mensagem, utilizando sua chave privada RSA para recuperar a chave AES e, em seguida, descriptografar o conteúdo.  

Este fluxo garante que apenas usuários autorizados tenham acesso às informações trocadas dentro do sistema, reforçando a segurança das comunicações.  
