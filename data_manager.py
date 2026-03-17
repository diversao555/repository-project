#!/usr/bin/env python3
data_manager.py
Gerenciador de dados informativos sobre animais surdos
Projeto Educacional - Alunos do Vicente Rijo - 2026
"""
vacoes = observacoes
        self.data_registro = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Converte objeto para dicionário"""
        return {
            'nome': self.nome,
            'especie': self.especie,
            'ida
import json
from datetime import datetime
from typing import Dict, List, Optional


class PetData:
    """Classe para representar informações sobre pets surdos"""
    
    def __init__(self, nome: str, especie: str, idade: float, 
                 tipo_surdez: str, observacoes: str = ""):
        self.nome = nome
        self.especie = especie.lower()  # 'cao' ou 'gato'
        self.idade = idade
        self.tipo_surdez = tipo_surdez  # 'congenita' ou 'adquirida'
        self.observacoes = observacoes
        self.data_registro = datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        """Converte objeto para dicionário"""
        return {
            'nome': self.nome,
            'especie': self.especie,
            'idade': self.idade,
            'tipo_surdez': self.tipo_surdez,
            'observacoes': self.observacoes,
            'data_registro': self.data_registro
        }
    
    def __repr__(self):
        return f"Pet({self.nome}, {self.especie}, {self.tipo_surdez})"


class DeafPetDatabase:
    """Banco de dados simples para informações educativas sobre pets surdos"""
    
    # Dados estatísticos educativos (fonte: estudos veterinários)
    ESTATISTICAS = {
        "caes_brancos_surdez_congenita": {
            "valor": "1 em 5",
            "descricao": "Cães brancos, especialmente das raças Dálmata, Bull Terrier e Pastor Australiano, têm maior predisposição à surdez congênita."
        },
        "gatos_brancos_olhos_azuis": {
            "valor": "~30%",
            "descricao": "Gatos brancos com olhos azuis apresentam maior probabilidade de nascerem com surdez devido à genética ligada à pigmentação."
        },
        "perda_auditiva_idosos": {
            "valor": "+10 anos",
            "descricao": "A perda auditiva relacionada à idade (presbiacusia) começa a aparecer em cães e gatos após os 10 anos."
        },
        "causas_adquiridas": [
            "Infecções de ouvido não tratadas",
            "Exposição a ruídos muito altos",
            "Traumas na cabeça ou ouvido",
            "Efeitos colaterais de medicamentos ototóxicos",
            "Tumores no canal auditivo"
        ]
    }
    
    # Desafios categorizados
    DESAFIOS_PETS = [
        {
            "titulo": "Segurança",
            "icone": "⚠️",
            "descricao": "Sem audição, o animal não percebe alertas sonoros como buzinas, chamados de emergência ou avisos de perigo."
        },
        {
            "titulo": "Ansiedade e Medo",
            "icone": "😰",
            "descricao": "A incapacidade de ouvir aproximações pode causar sustos frequentes e comportamentos defensivos."
        },
        {
            "titulo": "Comunicação Limitada",
            "icone": "🗣️",
            "descricao": "Comandos verbais não funcionam, dificultando o treinamento tradicional."
        },
        {
            "titulo": "Despertar Difícil",
            "icone": "😴",
            "descricao": "Acordar um animal surdo requer cuidado especial para não assustá-lo."
        }
    ]
    
    DESAFIOS_TUTORES = [
        {
            "titulo": "Aprendizado de Novas Técnicas",
            "icone": "🎓",
            "descricao": "Tutores precisam aprender métodos de treinamento baseados em sinais visuais e vibração."
        },
        {
            "titulo": "Supervisão Constante",
            "icone": "🔍",
            "descricao": "É necessário manter atenção redobrada em passeios para garantir a segurança do animal."
        },
        {
            "titulo": "Comunicação Adaptada",
            "icone": "💬",
            "descricao": "Desenvolver um vocabulário de gestos consistentes exige dedicação e paciência."
        }
    ]
    
    SOLUCOES = [
        {
            "titulo": "Coleiras com Sinais Visuais/Vibração",
            "descricao": "Permitem comunicação à distância de forma suave e não invasiva."
        },
        {
            "titulo": "Treinamento com Sinais Manuais",
            "descricao": "Ensinar comandos por gestos cria uma linguagem visual eficaz."
        },
        {
            "titulo": "Ambiente Seguro e Previsível",
            "descricao": "Manter rotina e layout consistentes reduz ansiedade e aumenta confiança."
        },
        {
            "titulo": "Identificação Atualizada",
            "descricao": "Plaquinhas, microchip e coleiras com contato visível são essenciais."
        }
    ]
    
    def __init__(self, arquivo_json: Optional[str] = None):
        self.arquivo = arquivo_json or "pets_surdos_dados.json"
        self.pets: List[PetData] = []
        self._carregar_dados()
    
    def _carregar_dados(self):
        """Carrega dados salvos anteriormente, se existirem"""
        try:
            with open(self.arquivo, 'r', encoding='utf-8') as f:
                dados = json.load(f)
                for item in dados:
                    pet = PetData(**item)
                    self.pets.append(pet)
        except FileNotFoundError:
            print(f"ℹ️  Arquivo {self.arquivo} não encontrado. Iniciando banco vazio.")
        except json.JSONDecodeError:
            print(f"⚠️  Erro ao ler {self.arquivo}. Iniciando banco vazio.")
    
    def salvar_dados(self):
        """Salva os dados atuais no arquivo JSON"""
        dados = [pet.to_dict() for pet in self.pets]
        with open(self.arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, ensure_ascii=False, indent=2)
        print(f"✅ Dados salvos em {self.arquivo}")
    
    def adicionar_pet(self, pet: PetData):
        """Adiciona um novo pet ao banco de dados"""
        self.pets.append(pet)
        self.salvar_dados()
        print(f"🐾 {pet.nome} registrado com sucesso!")
    
    def buscar_por_especie(self, especie: str) -> List[PetData]:
        """Busca pets por espécie (cao ou gato)"""
        return [p for p in self.pets if p.especie == especie.lower()]
    
    def buscar_por_tipo_surdez(self, tipo: str) -> List[PetData]:
        """Busca pets por tipo de surdez"""
        return [p for p in self.pets if p.tipo_surdez.lower() == tipo.lower()]
    
    def estatisticas_resumo(self) -> Dict:
        """Retorna estatísticas resumidas do banco"""
        total = len(self.pets)
        if total == 0:
            return {"total": 0, "mensagem": "Nenhum pet registrado ainda."}
        
        por_especie = {}
        por_tipo = {}
        
        for pet in self.pets:
            # Contagem por espécie
            especie = pet.especie
            por_especie[especie] = por_especie.get(especie, 0) + 1
            
            # Contagem por tipo de surdez
            tipo = pet.tipo_surdez
            por_tipo[tipo] = por_tipo.get(tipo, 0) + 1
        
        return {
            "total_registros": total,
            "por_especie": por_especie,
            "por_tipo_surdez": por_tipo,
            "ultima_atualizacao": datetime.now().strftime("%d/%m/%Y %H:%M")
        }
    
    def gerar_relatorio_educativo(self) -> str:
        """Gera um relatório textual com informações educativas"""
        relatorio = []
        relatorio.append("🐾 RELATÓRIO EDUCATIVO: ANIMAIS SURDOS")
        relatorio.append("=" * 50)
        relatorio.append(f"Gerado em: {datetime.now().strftime('%d/%m/%Y %H:%M')}\n")
        
        # Estatísticas gerais
        relatorio.append("📊 ESTATÍSTICAS GERAIS:")
        for key, info in self.ESTATISTICAS.items():
            if isinstance(info, dict) and 'valor' in info:
                relatorio.append(f"  • {info['valor']}: {info['descricao']}")
            elif isinstance(info, list):
                relatorio.append(f"  • {key.replace('_', ' ').title()}:")
                for item in info:
                    relatorio.append(f"    - {item}")
        relatorio.append("")
        
        # Resumo do banco
        resumo = self.estatisticas_resumo()
        relatorio.append("📋 RESUMO DO BANCO DE DADOS:")
        for chave, valor in resumo.items():
            relatorio.append(f"  • {chave}: {valor}")
        relatorio.append("")
        
        # Dicas rápidas
        relatorio.append("💡 DICAS RÁPIDAS PARA TUTORES:")
        for solucao in self.SOLUCOES:
            relatorio.append(f"  ✓ {solucao['titulo']}: {solucao['descricao']}")
        
        return "\n".join(relatorio)
    
    def exportar_para_site(self) -> Dict:
        """Exporta dados formatados para uso no frontend do site"""
        return {
            "estatisticas": self.ESTATISTICAS,
            "desafios_pets": self.DESAFIOS_PETS,
            "desafios_tutores": self.DESAFIOS_TUTORES,
            "solucoes": self.SOLUCOES,
            "resumo_banco": self.estatisticas_resumo()
        }


# ===== FUNÇÕES DE EXEMPLO PARA TESTE =====
def exemplo_uso():
    """Demonstra o uso básico da classe"""
    print("🚀 Iniciando exemplo de uso do Data Manager...\n")
    
    # Instancia o banco de dados
    db = DeafPetDatabase()
    
    # Adiciona alguns pets de exemplo
    pets_exemplo = [
        PetData("Thor", "cao", 3.5, "congenita", "Dálmata, responde bem a sinais manuais"),
        PetData("Luna", "gato", 2, "adquirida", "Perdeu audição após infecção, muito carinhosa"),
        PetData("Mel", "cao", 12, "adquirida", "Presbiacusia, idosa e calma"),
    ]
    
    for pet in pets_exemplo:
        db.adicionar_pet(pet)
    
    # Buscas de exemplo
    print("\n🔍 Buscando cães surdos:")
    caes = db.buscar_por_especie("cao")
    for c in caes:
        print(f"  - {c.nome} ({c.idade} anos, {c.tipo_surdez})")
    
    # Gera relatório
    print("\n📄 Gerando relatório educativo:")
    print(db.gerar_relatorio_educativo())
    
    # Exporta para o site
    print("\n🌐 Dados exportados para frontend:")
    dados_site = db.exportar_para_site()
    print(f"  • {len(dados_site['desafios_pets'])} desafios de pets")
    print(f"  • {len(dados_site['solucoes'])} soluções disponíveis")
    
    print("\n✅ Exemplo concluído!")


# ===== EXECUÇÃO DIRETA =====
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--exemplo":
        exemplo_uso()
    elif len(sys.argv) > 1 and sys.argv[1] == "--ajuda":
        print("""
🐾 Data Manager para Pets Surdos
================================

Uso:
  python data_manager.py              # Inicia sem ação (apenas carrega)
  python data_manager.py --exemplo    # Executa demonstração de uso
  python data_manager.py --ajuda      # Mostra esta mensagem

Funcionalidades:
  • Armazenamento de dados de pets surdos em JSON
  • Estatísticas educativas sobre surdez animal
  • Categorias de desafios e soluções
  • Exportação de dados para site frontend
  • Relatórios educativos em texto

Arquivo de dados: pets_surdos_dados.json
        """)
    else:
        print("🐾 Data Manager carregado. Use --exemplo para ver demonstração.")
        print("   Use --ajuda para mais informações.")