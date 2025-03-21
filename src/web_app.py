import os
import dotenv
from flask import Flask, render_template, jsonify
from src.lol_data import fetch_latest_patch_notes_text
from src.script_agents import create_script_agent, create_script_task, run_script_generation

# Carregar variáveis de ambiente
dotenv.load_dotenv()

app = Flask(__name__)

# Verificar se a chave da API OpenAI está configurada
if "OPENAI_API_KEY" not in os.environ:
    print("Aviso: A chave da API OpenAI não foi configurada.")
    print("Crie um arquivo .env com sua chave OPENAI_API_KEY.")

# Definir o modelo a ser utilizado
MODEL = "gpt-3.5-turbo"


@app.route('/')
def index():
    """Rota principal que renderiza a página inicial."""
    return render_template('index.html')


@app.route('/gerar-roteiro', methods=['POST'])
def gerar_roteiro():
    """
    Rota para gerar um roteiro a partir das notas de patch mais recentes.
    """
    try:
        # Verificar se a chave da API OpenAI está configurada
        if "OPENAI_API_KEY" not in os.environ:
            return jsonify({
                'status': 'error',
                'message': 'Chave da API OpenAI não configurada. Veja o README para instruções.'
            }), 500

        # Obter as notas do patch mais recente
        patch_text = fetch_latest_patch_notes_text()

        # Criar o agente para geração do roteiro
        agent = create_script_agent(model=MODEL)

        # Criar a tarefa para o agente
        task = create_script_task(agent, patch_text)

        # Executar a geração do roteiro
        roteiro = run_script_generation(agent, task)

        return jsonify({
            'status': 'success',
            'roteiro': roteiro
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Erro ao gerar roteiro: {str(e)}'
        }), 500


def run_web_app(host='0.0.0.0', port=5000, debug=False):
    """Inicia a aplicação web."""
    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    run_web_app(debug=True)
