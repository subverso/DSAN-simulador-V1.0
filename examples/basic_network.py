"""
DSAN-Sim: Exemplo básico de rede.
Testa: identidade, mensagens assinadas, perda de rede.
"""

from dsan_sim.agent import DSANAgent
from dsan_sim.simulator import DSANSimulator

# Cria 4 agentes soberanos
print("🧬 Criando agentes...")
agents = [
    DSANAgent("totem-001"),
    DSANAgent("totem-002"),
    DSANAgent("totem-003"),
    DSANAgent("malicious")  # Para testes futuros
]

# Inicia simulador (10% perda de rede)
sim = DSANSimulator(agents, network_loss=0.1)

# Executa 8 steps
print("🌐 Executando simulação...")
sim.run(steps=8)

print("\n🎉 DSAN-Sim v0.1 funcionando!")
print("Baixe ZIP e rode localmente para ver logs completos.")
