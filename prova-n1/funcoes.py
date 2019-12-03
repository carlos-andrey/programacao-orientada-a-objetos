def converte_tamanho(tamanho_bytes):
    tamanho_megabytes = tamanho_bytes/1000000
    return tamanho_megabytes
def percentual(tamanho_total, tamanho_utilizado):
    porcentagem = (100 * tamanho_utilizado)/tamanho_total  
    return porcentagem