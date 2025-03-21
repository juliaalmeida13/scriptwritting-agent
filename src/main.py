import os
import dotenv
from src.lol_data import fetch_latest_patch_notes_text
from src.script_agents import (
    create_script_agent,
    create_script_task,
    run_script_generation
)


def main():
    """
    Função principal que executa o fluxo completo de geração de roteiro.
    """
    # Carregar variáveis de ambiente
    dotenv.load_dotenv()

    # Verificar se a chave da API OpenAI está configurada
    if "OPENAI_API_KEY" not in os.environ:
        print("Erro: A chave da API OpenAI não foi configurada.")
        print("Crie um arquivo .env com sua chave OPENAI_API_KEY.")
        return

    # Definir o modelo a ser utilizado
    model = "gpt-3.5-turbo"

    # Obter as notas do patch mais recente
    print("Obtendo as notas do patch mais recente...")
    try:
        patch_text = fetch_latest_patch_notes_text()
        print("Notas de patch obtidas com sucesso!")
    except Exception as e:
        print(f"Erro ao obter as notas do patch: {e}")
        return

    # Criar o agente para geração do roteiro
    print("Criando agente para geração do roteiro...")
    agent = create_script_agent(model=model)

    # Criar a tarefa para o agente
    print("Configurando a tarefa de geração...")
    task = create_script_task(agent, patch_text)

    # Executar a geração do roteiro
    print("Gerando o roteiro...")
    roteiro = run_script_generation(agent, task)

    # Salvar o roteiro em um arquivo
    with open("roteiro_gerado.md", "w", encoding="utf-8") as f:
        f.write(roteiro)

    print("\nRoteiro gerado com sucesso e salvo em 'roteiro_gerado.md'!")


if __name__ == "__main__":
    main()
