# 🚀 PROJETA — Observatório de Projetos Integradores (Backend)

## 📝 Descrição do Sistema

O **Observatório de Projetos Integradores** é uma plataforma estratégica de governança acadêmica e vitrine tecnológica, concebida para centralizar o ciclo de vida da produção prática em instituições de ensino e estabelecer uma conexão direta com o mercado de trabalho.

Este repositório concentra exclusivamente a **camada de Backend (API e Persistência de Dados)**, responsável por fornecer os dados e regras de negócio para o ecossistema unificado, garantindo segurança, integridade e performance.

---

## ⚙️ Arquitetura e Estrutura do Projeto

O projeto segue uma arquitetura em camadas (baseada em separação de responsabilidades), estruturada da seguinte forma na pasta `app`:

- **`config/`**: Configurações gerais da aplicação e conexão com o banco de dados.
- **`routes/`**: Definição dos endpoints da API, agrupados por domínio.
- **`controllers/`**: Manipulação das requisições e respostas HTTP, servindo de ponte entre as rotas e os serviços.
- **`services/`**: Contém a lógica de negócio principal do sistema.
- **`repositories/`**: Camada de persistência, responsável pela comunicação e operações diretas com o banco de dados.
- **`models/`**: Definição das entidades e tabelas do banco de dados.
- **`schemas/`**: Esquemas de validação de dados utilizando Pydantic para tipagem de entrada (request) e saída (response).

### Domínios e Rotas da API

A API foi projetada para atender aos diferentes perfis de usuários mapeados no sistema, com endpoints divididos por domínios de negócio:

#### Entidades Principais

- **Alunos, Professores e Empresas**: Endpoints para gerenciamento de perfis, competências e informações institucionais.
- **Coordenação**: Gerenciamento e aprovação de usuários.
- **Projetos e Equipes**: Submissão de Projetos Integradores e acompanhamento.
- **Avaliações**: Acompanhamento, orientação e avaliação dos trabalhos submetidos pelos alunos.
- **Estatísticas**: Métricas globais e institucionais, visão geral estratégica sobre o andamento e uso da plataforma.

---

## 💻 Tecnologias Utilizadas

Este projeto foi construído utilizando as seguintes tecnologias:

- **[Python 3](https://www.python.org/)** - Linguagem de programação.
- **[FastAPI](https://fastapi.tiangolo.com/)** - Framework web moderno e rápido para construção de APIs.
- **[Uvicorn](https://www.uvicorn.org/)** - Servidor ASGI para alta performance.
- **[SQLite](https://www.sqlite.org/)** - Banco de dados relacional leve (banco padrão do projeto: `projeta.db`).
- **[Pydantic](https://docs.pydantic.dev/)** - Validação de dados e tipagem estática.

---

## 🚀 Como Executar o Projeto Localmente

### Pré-requisitos

- **[Python](https://www.python.org/)** (versão 3.8 ou superior recomendada).

### Passos para Instalação e Execução

1. Clone este repositório para a sua máquina local:

   ```bash
   git clone https://github.com/josevaldr/projeta-observatorio-pi-backend.git
   ```

2. Acesse a pasta do projeto pelo terminal:

   ```bash
   cd projeta-observatorio-pi-backend
   ```

3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv .venv
   ```

4. Ative o ambiente virtual:
   - **Windows:**
     ```bash
     .venv\Scripts\activate
     ```
   - **Linux/macOS:**
     ```bash
     source .venv/bin/activate
     ```

5. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

6. Inicie o servidor de desenvolvimento:

   ```bash
   fastapi dev app/main.py
   # Ou utilizando uvicorn diretamente:
   uvicorn app.main:app --reload
   ```

7. O servidor será iniciado. Acesse a documentação interativa da API (Swagger) no navegador:
   - **Swagger UI:** `http://localhost:8000/docs`
   - **ReDoc:** `http://localhost:8000/redoc`

---

## 🔗 Repositório do Frontend

A Interface do Usuário (UI) e as interações com esta API estão implementadas no Frontend da aplicação. Você pode acessar o repositório oficial no link abaixo:

- **Frontend Repository:** [https://github.com/josevaldr/projeta-observatorio-pi-frontend](https://github.com/josevaldr/projeta-observatorio-pi-frontend)
