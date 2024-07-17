from csv import reader
from collections import defaultdict
import time

from pathlib import Path

PATH_DO_TXT = 'data/measurements.txt'

def processar_temperaturas(path_do_arquivo: Path):
    print('Processando temperaturas...')

    start_time = time.time()
    temperatura_por_station = defaultdict(list)

    with open(path_do_arquivo, 'r', encoding="utf-8") as file:
        _reader = reader(file, delimiter=';')
        for row in _reader:
            nome_da_station, temperatura = str(row[0]), float(row[1])
            temperatura_por_station[nome_da_station].append(temperatura)
    print('Dados carregados. Calculando estatisticas...')

    results = {}

    for station, temperatures in temperatura_por_station.items():
        min_temp = min(temperatures)
        mean_temp = sum(temperatures) / len(temperatures)
        max_temp = max(temperatures)
        results[station] = (min_temp, mean_temp, max_temp)

    print('Estatisticas calculadas. Salvando resultados...')
    sorted_results = dict(sorted(results.items()))

    end_time = time.time()
    print(f"Tempo total: {end_time - start_time:.3f} segundos")
    
    return sorted_results


dados_processados = processar_temperaturas(PATH_DO_TXT)
print(dados_processados)


    