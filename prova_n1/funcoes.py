def converte_tamanho(tamanho_bytes):
    tamanho_megabytes = tamanho_bytes/1048576
    return tamanho_megabytes
def percentual(usuario, total):
    porcentagem = (usuario[2]/total)*100  
    usuario.append(porcentagem)