# projeta-observatorio-pi-backend

## Autenticação e Login

O backend possui autenticação por token.

### Rota de login

Endpoint:

`POST /login`

A rota recebe o email e a senha do usuário.

Exemplo de requisição:

```json
{
  "email": "usuario@email.com",
  "senha": "123456"
}
```

Se os dados estiverem corretos, a API retorna um token de acesso:

```json
{
  "access_token": "token_gerado",
  "token_type": "bearer"
}
```

### Uso do token

Para acessar rotas protegidas, o token deve ser enviado no cabeçalho da requisição:

```text
Authorization: Bearer token_gerado
```

No Swagger, o token pode ser informado pelo botão **Authorize**.

### Fluxos de erro testados

* Usuário não encontrado: ocorre quando o email informado não existe no banco.
* Senha inválida: ocorre quando o email existe, mas a senha está incorreta.
* Token ausente: ocorre quando uma rota protegida é acessada sem autenticação.
* Token inválido: ocorre quando o token informado não é válido ou está incorreto.

### Observação sobre segurança

As senhas não devem ser salvas em texto puro no banco de dados. O sistema deve armazenar apenas a senha criptografada com hash.
