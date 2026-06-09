from src.telemetria import coletar
from src.alertas import avaliar
from pathlib import Path
from dotenv import load_dotenv
from ollama import Client
import os

load_dotenv()

client = Client(
    host="https://ollama.com",
    headers={
        "Authorization": f"Bearer {os.getenv('OLLAMA_API_KEY')}"
    }
)

class MissionEngine:
    def __init__(self):
        self.system_prompt = Path(
            "prompts/system_prompt.md"
        ).read_text(encoding="utf-8")

    def is_ready(self):
        return True

    def status_snapshot(self):
        return str(coletar())

    def analyze(self, pergunta):
        dados = coletar()
        alertas = avaliar(dados)

        acoes = []

        if dados["energia"] < 20:
            acoes.append("Ativar modo economia")

        if dados["buffer_imagens"] > 80:
            acoes.append("Priorizar transmissão de imagens críticas")

        prompt = f"""
Dados da missão:

{dados}

Alertas detectados:

{alertas}

Ações automáticas:

{acoes}

Pergunta do operador:
{pergunta}
"""

        try:
            resposta = client.chat(
                model="gpt-oss:120b",
                messages=[
                    {
                        "role": "system",
                        "content": self.system_prompt
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )

            return resposta["message"]["content"]

        except Exception as e:
            return f"Erro ao consultar IA: {e}"