from crewai import Agent, Task, Crew


def create_script_agent(model="gpt-3.5-turbo"):
    """
    Cria um agente para gerar roteiros de vídeo.

    Args:
        model: Modelo de IA a ser utilizado

    Returns:
        Agente configurado para geração de roteiros
    """
    agent = Agent(
        role="Video Script Generator",
        goal="Criar roteiros curtos e empolgantes sobre as notas de atualização do League of Legends",
        backstory=("Um agente especializado em destacar as principais mudanças de "
                  "cada patch, de forma breve e atrativa."),

        system_template=(
            """<|start_header_id|>system<|end_header_id|>
            Você é um assistente especializado em criar roteiros de vídeo sobre as 
            notas de atualização do League of Legends.<|eot_id|>"""
        ),
        prompt_template=(
            """<|start_header_id|>user<|end_header_id|>
            {{ .Prompt }}<|eot_id|>"""
        ),
        response_template=(
            """<|start_header_id|>assistant<|end_header_id|>
            {{ .Response }}<|eot_id|>"""
        ),

        name="LoLPatchAgent",
        model=model,
        description="Agente para gerar roteiros de vídeo sobre o patch mais recente de LoL"
    )
    return agent


def create_script_task(agent, patch_text):
    """
    Cria uma tarefa para geração de roteiro.

    Args:
        agent: Agente que executará a tarefa
        patch_text: Texto das notas do patch a ser utilizado como referência

    Returns:
        Tarefa configurada para geração do roteiro
    """
    prompt = f"""
    Crie um roteiro de até 1 minuto e meio para um vídeo vertical
    sobre as principais mudanças do patch mais recente de League of Legends.
    Use o texto abaixo como base:
    {patch_text}

    Dê enfase às alterações dos campeões no patch, incluindo quais foram
    nerfados e quais foram buffados
    """
    task = Task(
        description=prompt,
        expected_output=(
            "Um roteiro deve ser empolgante, conciso e "
            "destacar as principais novidades."
        ),
        agent=agent,
    )
    return task


def run_script_generation(agent, task):
    """
    Executa a geração do roteiro utilizando a crew.

    Args:
        agent: Agente configurado para a geração
        task: Tarefa a ser executada

    Returns:
        Texto do roteiro gerado
    """
    roteiro_crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )

    response = roteiro_crew.kickoff()
    return response.raw
