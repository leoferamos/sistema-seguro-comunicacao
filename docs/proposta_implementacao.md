# Proposta de Implementação

## Introdução  
Esta proposta detalha como as tecnologias de criptografia e autenticação serão utilizadas para garantir a segurança do sistema de comunicação interna da empresa. O objetivo principal é proteger as credenciais dos usuários e as mensagens armazenadas contra acessos não autorizados.

## Tecnologias Utilizadas e Implementação  

### 1. Hashing Seguro de Senhas com bcrypt  
- O bcrypt será utilizado para armazenar as senhas dos usuários de forma segura.  
- Durante o cadastro, a senha será transformada em um hash antes de ser salva no banco de dados.  
- No momento do login, o hash armazenado será comparado com a senha fornecida pelo usuário.  

**Exemplo de implementação:**  
1. Usuário fornece uma senha.  
2. O sistema gera um hash seguro utilizando bcrypt.  
3. O hash é armazenado no banco de dados.  
4. No login, bcrypt verifica se a senha digitada corresponde ao hash salvo.  

### 2. Autenticação via Tokens JWT  
- O PyJWT será utilizado para gerenciar a autenticação dos usuários.  
- Quando um usuário faz login com sucesso, um Token JWT é gerado e enviado como resposta.  
- Esse token contém informações codificadas e uma assinatura para evitar fraudes.  
- O token será necessário para acessar recursos protegidos do sistema.  

**Fluxo:**  
1. Usuário faz login e fornece credenciais.  
2. O sistema valida a senha e gera um Token JWT.  
3. O Token JWT é enviado ao usuário e deve ser utilizado nas requisições futuras.  
4. O sistema valida o token antes de permitir qualquer acesso.  

### 3. Criptografia de Mensagens com AES  
- As mensagens enviadas pelos usuários serão criptografadas utilizando AES no modo CBC.  
- Uma chave AES será gerada para cada sessão de comunicação.  
- O IV (vetor de inicialização) será armazenado junto com a mensagem para possibilitar a descriptografia.  

**Fluxo:**  
1. Usuário escreve uma mensagem.  
2. O sistema gera uma chave AES única.  
3. A mensagem é criptografada com AES e armazenada no banco de dados.  
4. O destinatário recebe a mensagem criptografada.  

### 4. Proteção da Chave AES com RSA  
- Como a chave AES não pode ser armazenada em texto puro, utilizaremos criptografia assimétrica RSA para protegê-la.  
- Cada usuário terá um par de chaves RSA (pública e privada).  
- A chave AES utilizada para criptografar a mensagem será protegida com a chave pública do destinatário.  

**Fluxo:**  
1. O sistema gera uma chave AES para a sessão.  
2. A chave AES é criptografada usando a chave pública RSA do destinatário.  
3. A chave criptografada é armazenada junto com a mensagem.  
4. O destinatário utiliza sua chave privada RSA para recuperar a chave AES.  
5. A mensagem é descriptografada com a chave AES.  

### 5. Armazenamento Seguro de Dados  
- As senhas dos usuários serão armazenadas apenas em formato hash (bcrypt).  
- Tokens JWT terão um tempo de expiração para reduzir riscos.  
- As mensagens serão criptografadas antes de serem armazenadas.  
- As chaves AES serão protegidas com RSA, garantindo que apenas o destinatário possa acessá-las.  

## Conclusão  
Com essa implementação, garantimos que todas as informações sensíveis do sistema (senhas, mensagens e chaves) estarão protegidas contra acessos não autorizados. O uso de hashing, autenticação JWT e criptografia de dados assegura um alto nível de segurança para a comunicação entre os funcionários.  
