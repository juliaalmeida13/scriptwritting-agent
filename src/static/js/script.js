// Elementos da página
const btnGerarRoteiro = document.getElementById('gerarRoteiro');
const btnCopiarRoteiro = document.getElementById('copiarRoteiro');
const loadingElement = document.getElementById('loading');
const resultadoElement = document.getElementById('resultado');
const roteiroContentElement = document.getElementById('roteiroContent');

// Função para mostrar o indicador de carregamento
function mostrarLoading() {
    loadingElement.style.display = 'block';
    btnGerarRoteiro.disabled = true;
    resultadoElement.style.display = 'none';
}

// Função para esconder o indicador de carregamento
function esconderLoading() {
    loadingElement.style.display = 'none';
    btnGerarRoteiro.disabled = false;
}

// Função para mostrar o resultado
function mostrarResultado(roteiro) {
    resultadoElement.style.display = 'block';
    roteiroContentElement.innerHTML = formatarRoteiro(roteiro);
    // Rolar para o resultado
    resultadoElement.scrollIntoView({ behavior: 'smooth' });
}

// Função para formatar o roteiro (converte markdown para HTML básico)
function formatarRoteiro(texto) {
    if (!texto) return '';
    
    // Substituir quebras de linha por <br>
    let formatado = texto.replace(/\n/g, '<br>');
    
    // Substituir títulos markdown
    formatado = formatado.replace(/# (.*?)(<br>|$)/g, '<h3>$1</h3>');
    formatado = formatado.replace(/## (.*?)(<br>|$)/g, '<h4>$1</h4>');
    
    // Substituir negrito
    formatado = formatado.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
    
    // Substituir itálico
    formatado = formatado.replace(/\*(.*?)\*/g, '<em>$1</em>');
    
    return formatado;
}

// Função para gerar o roteiro
async function gerarRoteiro() {
    try {
        mostrarLoading();
        
        const response = await fetch('/gerar-roteiro', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            }
        });
        
        const data = await response.json();
        
        if (data.status === 'success') {
            mostrarResultado(data.roteiro);
        } else {
            throw new Error(data.message || 'Erro ao gerar roteiro');
        }
    } catch (error) {
        alert('Erro: ' + error.message);
        console.error('Erro:', error);
    } finally {
        esconderLoading();
    }
}

// Função para copiar o roteiro para a área de transferência
function copiarRoteiro() {
    // Criar um elemento temporário para copiar o texto sem formatação
    const textarea = document.createElement('textarea');
    textarea.value = roteiroContentElement.innerText;
    document.body.appendChild(textarea);
    textarea.select();
    
    try {
        document.execCommand('copy');
        alert('Roteiro copiado para a área de transferência!');
    } catch (err) {
        console.error('Erro ao copiar:', err);
        alert('Não foi possível copiar o roteiro. Por favor, selecione o texto e copie manualmente.');
    } finally {
        document.body.removeChild(textarea);
    }
}

// Adicionar eventos aos botões
btnGerarRoteiro.addEventListener('click', gerarRoteiro);
btnCopiarRoteiro.addEventListener('click', copiarRoteiro); 