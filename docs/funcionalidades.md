# Definição de Funcionalidades  

## 1. Cadastro de Usuário  
- O usuário cria uma conta fornecendo nome de usuário e senha.  
- A senha é protegida com bcrypt antes de ser armazenada no banco de dados.  
- Apenas o hash da senha é salvo, garantindo segurança contra vazamentos de credenciais.  

## 2. Login  
- O usuário informa suas credenciais para acessar o sistema.  
- A senha fornecida é comparada com o hash armazenado utilizando bcrypt.  
- Se a autenticação for bem-sucedida, um Token JWT é gerado e enviado ao usuário.  
- O Token JWT deve ser usado para acessar funcionalidades protegidas.  

## 3. Envio de Mensagem  
- O usuário escreve uma mensagem para outro usuário.  
- A mensagem é criptografada utilizando AES antes de ser armazenada.  
- A chave AES gerada para criptografia é protegida com a chave pública RSA do destinatário.  
- A mensagem criptografada e a chave AES protegida são armazenadas no banco de dados.  

## 4. Recebimento de Mensagem  
- O usuário acessa sua caixa de mensagens e escolhe uma mensagem para visualizar.  
- A chave AES protegida é descriptografada usando a chave privada RSA do usuário.  
- A mensagem é então descriptografada com a chave AES recuperada.  
- O usuário pode ler a mensagem original de forma segura.  

Com essa abordagem, garantimos que apenas o destinatário correto possa acessar o conteúdo da mensagem, garantindo privacidade e segurança na comunicação.  
