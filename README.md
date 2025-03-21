# Gerador de Roteiros para Vídeos de League of Legends

Este projeto é um gerador automático de roteiros para vídeos curtos sobre as atualizações mais recentes (patches) do jogo League of Legends. Ele utiliza a biblioteca CrewAI para criar agentes de IA que analisam as notas de patch oficiais e criam roteiros concisos e empolgantes para vídeos verticais.

## Funcionalidades

- Busca automática das notas do patch mais recente no site oficial do LoL
- Extração e processamento do conteúdo das notas de patch
- Geração de roteiros para vídeos verticais de até 1 minuto e meio
- Foco nas alterações de campeões (buffs e nerfs)
- Interface web amigável para geração de roteiros com um clique

## Requisitos

- Python 3.8+
- Chave de API da OpenAI

## Instalação

1. Clone este repositório:
```bash
git clone https://github.com/juliaalmeida13/scriptwritting-agent.git
cd scriptwritting-agent
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure suas credenciais da OpenAI:
   - Crie um arquivo `.env` na raiz do projeto
   - Adicione sua chave API da OpenAI: `OPENAI_API_KEY=sua_chave_aqui`

## Uso

### Interface Web (Recomendado)

Para usar a interface web, execute:

```bash
python run_web.py
```

Em seguida, abra seu navegador e acesse:
```
http://localhost:5000
```

Na interface web, basta clicar no botão "Gerar Roteiro" e esperar alguns instantes. O roteiro será exibido na página, com a opção de copiá-lo para a área de transferência.

### Linha de Comando

Se preferir usar o modo de linha de comando, execute:

```bash
python run.py
```

O roteiro gerado será salvo no arquivo `roteiro_gerado.md` na raiz do projeto.

## Estrutura do Projeto

```
lol-script-generator/
├── .env                   # Arquivo de variáveis de ambiente (não versionado)
├── .env.example           # Exemplo das variáveis de ambiente necessárias
├── requirements.txt       # Dependências do projeto
├── LICENSE                # Licença MIT do projeto
├── README.md              # Documentação do projeto
├── run.py                 # Ponto de entrada para versão CLI
├── run_web.py             # Ponto de entrada para versão Web
├── src/                   # Código-fonte do projeto
│   ├── __init__.py        # Torna o diretório um pacote Python
│   ├── lol_data.py        # Funções para obtenção de dados do LoL
│   ├── script_agents.py   # Definição dos agentes e tarefas
│   ├── main.py            # Lógica principal da aplicação CLI
│   ├── web_app.py         # Aplicação web usando Flask
│   ├── templates/         # Templates HTML
│   │   └── index.html     # Página principal da interface web
│   └── static/            # Arquivos estáticos
│       ├── css/           # Estilos CSS
│       │   └── style.css  # Estilos da interface web
│       └── js/            # Scripts JavaScript
│           └── script.js  # Interatividade da interface web
└── roteiro_gerado.md      # Arquivo de saída com o roteiro gerado (versão CLI)
```

## Personalização

Você pode personalizar o comportamento do gerador de roteiros:

- Altere o modelo de IA em `src/main.py` ou `src/web_app.py` (padrão: "gpt-3.5-turbo")
- Modifique o prompt em `src/script_agents.py` para obter resultados diferentes
- Ajuste os parâmetros do agente para alterar seu estilo ou comportamento
- Personalize o visual da interface web editando os arquivos em `src/static/css`

## Origem

Este projeto foi transformado de um notebook Jupyter/Colab para uma estrutura de projeto Python adequada, visando melhor organização e manutenção do código.

## Licença

Este projeto está sob a licença MIT.
