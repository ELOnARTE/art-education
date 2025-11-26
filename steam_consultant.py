# Projeto ELOnARTE: Educação Transdisciplinar e Agenda 2030
# Prompt para o Copilot: "Crie um script em Python que atue como um consultor pedagógico, 
# recebendo uma disciplina escolar e sugerindo uma abordagem artística baseada em neurociência 
# e um Objetivo de Desenvolvimento Sustentável (ODS) correspondente."

def consultar_metodologia(disciplina):
    """
    Retorna a metodologia transdisciplinar baseada na disciplina informada.
    """
    # Base de conhecimento da ELOnARTE (Dicionário)
    base_conhecimento = {
        "matematica": {
            "arte": "Música e Ritmo",
            "neurociencia": "Estímulo do raciocínio lógico-temporal e frações através de partituras.",
            "ods": "ODS 4 - Educação de Qualidade"
        },
        "historia": {
            "arte": "Artes Visuais e Pintura",
            "neurociencia": "Memória visual e empatia cultural através da análise de obras de época.",
            "ods": "ODS 10 - Redução das Desigualdades"
        },
        "gestao": {
            "arte": "Teatro e Improvisação",
            "neurociencia": "Desenvolvimento de oratória, gestão de conflitos e inteligência emocional.",
            "ods": "ODS 8 - Trabalho Decente e Crescimento Econômico"
        },
        "biologia": {
            "arte": "Dança e Expressão Corporal",
            "neurociencia": "Consciência corporal e entendimento sistêmico da fisiologia.",
            "ods": "ODS 3 - Saúde e Bem-Estar"
        }
    }

    chave = disciplina.lower()
    
    if chave in base_conhecimento:
        metodo = base_conhecimento[chave]
        return (f"\n--- Consultoria ELOnARTE ---\n"
                f"📚 Disciplina: {disciplina.capitalize()}\n"
                f"🎨 Metodologia: {metodo['arte']}\n"
                f"🧠 Neurociência: {metodo['neurociencia']}\n"
                f"🌍 Impacto Social: {metodo['ods']}")
    else:
        return "Disciplina ainda não cadastrada na base STEAM da ELOnARTE."

# Simulação de Uso
print("Bem-vindo ao Sistema de Educação Transdisciplinar ELOnARTE")
entrada = input("Digite a disciplina que deseja ensinar (Matematica, Historia, Gestao, Biologia): ")
print(consultar_metodologia(entrada))
