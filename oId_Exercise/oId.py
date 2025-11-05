import requests
import sys
import time
import urllib.parse

# --- Configuração ---
TARGET_NAME = "Rodrigo Miguel Botelho Oliveira"
BASE_URL = "https://trainingserver.atec.pt/TrainingServer/Mulberry/JSON/Controls/Calendar/getCalendarDataSource.ashx"

# Intervalo de IDs a testar
ID_RANGE_START = 8000
ID_RANGE_END = 10000

# Timestamps para o período de interesse
START_TIMESTAMP = '1761523200'
END_TIMESTAMP = '1762128000'

# --- Fim da Configuração ---

print(f"Buscando 'oId' para: {TARGET_NAME}")
print(f"Apenas sessões como FORMADOR")
print(f"Intervalo de teste: {ID_RANGE_START} até {ID_RANGE_END}\n")

session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://trainingserver.atec.pt/TrainingServer/Default.aspx'
})

# Preparar variações do nome para uma busca mais abrangente
name_variations = [
    TARGET_NAME.lower(),
    "rodrigo oliveira",
    "rodrigo botelho",
    "botelho oliveira"
]

formador_ids_encontrados = []

for user_id in range(ID_RANGE_START, ID_RANGE_END + 1):
    current_oid = str(user_id)
    
    print(f"Testando ID {user_id:<5}...", end=" ")

    params = {
        'command': '_SelectAllSchedulesDataSetGivenByUserId',
        'oId': current_oid,
        'idField': 'DataValueField',
        'titleField': 'DataTextField',
        'startDateField': 'DataStartField',
        'endDateField': 'DataEndField',
        'backgroundColorField': '',
        'textColorField': 'textcolor',
        'eventColorField': 'color',
        'description': 'description',
        'picField': 'pic',
        'urlField': 'url',
        'start': START_TIMESTAMP,
        'end': END_TIMESTAMP,
        '_': int(time.time() * 1000)
    }

    try:
        response = session.get(BASE_URL, params=params, timeout=10)

        if not response.ok:
            print(f"❌ Erro HTTP {response.status_code}")
            continue

        try:
            events = response.json()
        except requests.exceptions.JSONDecodeError:
            print("❌ Resposta não-JSON")
            continue

        # Verificar se existem eventos e analisar o conteúdo
        if isinstance(events, list) and len(events) > 0:
            formador_encontrado = False
            matched_event = None
            
            for event in events:
                # Buscar o nome no título e na descrição do evento
                event_title = event.get('title', '').lower()
                event_description = event.get('description', '').lower()
                
                # Verificar se é SESSÃO COMO FORMADOR
                is_formador = "sessão como formador" in event_description
                
                # Verificar se o nome está presente
                name_match = any(name_var.lower() in event_title or 
                               name_var.lower() in event_description 
                               for name_var in name_variations)
                
                if name_match and is_formador:
                    formador_encontrado = True
                    matched_event = event
                    break
            
            if formador_encontrado:
                print(f"✅ FORMADOR ENCONTRADO!")
                
                # Verificar se este oId já foi encontrado antes
                if user_id not in formador_ids_encontrados:
                    formador_ids_encontrados.append(user_id)
                    
                    print(f"\n{'='*60}")
                    print(f"🎯 oId CONFIRMADO COMO FORMADOR: {user_id}")
                    print(f"📅 Evento: {matched_event.get('title', 'Sem título')}")
                    print(f"📝 Descrição: {matched_event.get('description', 'Sem descrição')[:150]}...")
                    print(f"{'='*60}\n")
                    
                    # Perguntar se quer continuar (pode haver mais do que um oId)
                    continuar = input("Deseja continuar a busca por mais IDs? (s/n): ")
                    if continuar.lower() != 's':
                        print(f"\n📊 Resumo: Encontrados {len(formador_ids_encontrados)} oIds como Formador")
                        for oid in formador_ids_encontrados:
                            print(f"   - oId: {oid}")
                        sys.exit(0)
            else:
                # Verificar se há eventos do nome mas como formando (para debug)
                name_only_found = False
                for event in events:
                    event_title = event.get('title', '').lower()
                    event_description = event.get('description', '').lower()
                    name_match = any(name_var.lower() in event_title or 
                                   name_var.lower() in event_description 
                                   for name_var in name_variations)
                    if name_match:
                        name_only_found = True
                        break
                
                if name_only_found:
                    print("👨‍🎓 Apenas como Formando (ignorado)")
                else:
                    print("📅 Eventos, mas nome não corresponde")
        else:
            print("❌ Sem eventos")

    except requests.exceptions.Timeout:
        print("⏰ Timeout")
    except requests.exceptions.RequestException as e:
        print(f"🌐 Erro: {e}")
        time.sleep(0.5)

print(f"\n{'='*50}")
print(f"BUSCA CONCLUÍDA")
print(f"Intervalo: {ID_RANGE_START}-{ID_RANGE_END}")
print(f"Total de oIds encontrados como Formador: {len(formador_ids_encontrados)}")
if formador_ids_encontrados:
    print("oIds confirmados:")
    for oid in formador_ids_encontrados:
        print(f"  → {oid}")
else:
    print("Nenhum oId encontrado como Formador no intervalo pesquisado.")
print(f"{'='*50}")