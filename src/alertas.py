def avaliar(d):
    a=[]
    if d['temperatura']>70: a.append('Temperatura crítica')
    if d['energia']<20: a.append('Energia crítica')
    if d['buffer_imagens']>80: a.append('Buffer quase cheio')
    if d['precisao_geolocalizacao']<85: a.append('Baixa precisão geográfica')
    return a
