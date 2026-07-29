"""
2Script de coleta inicial de dados da Riot API.
3Executar: python scripts/collect_data.py
4"""
5
6import os
7import sys
8
9# Adiciona src ao path para importações
10sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
11
12from dotenv import load_dotenv
13
14load_dotenv()
15
16
17def main():
18    print("=" * 50)
19    print("🎮 TFT Hub — Coleta de Dados")
20    print("=" * 50)
21
22    api_key = os.getenv("RIOT_API_KEY")
23    if not api_key:
24        print("❌ Erro: RIOT_API_KEY não encontrada!")
25        print("   Crie um arquivo .env com sua chave da Riot API.")
26        print("   Veja .env.example como referência.")
27        sys.exit(1)
28
29    print("✅ Chave da API encontrada!")
30    print("\n📋 Funcionalidades a implementar:")
31    print("   1. Buscar PUUIDs do elo Challenger (BR)")
32    print("   2. Coletar IDs de partidas recentes")
33    print("   3. Extrair detalhes de cada partida")
34    print("   4. Armazenar no banco SQLite")
35    print("\n🚧 Em construção — disponível na Etapa 2.")
36
37
38if __name__ == "__main__":
39    main()
