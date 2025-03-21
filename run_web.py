from src.web_app import run_web_app

if __name__ == "__main__":
    print("Iniciando o servidor web na porta 5000...")
    print("Abra seu navegador e acesse: http://localhost:5000")
    run_web_app(debug=True)
