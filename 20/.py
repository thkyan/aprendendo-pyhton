# import webbrowser
# webbrowser.open('https://hastagtreinamentos.com')

# import webbrowser as wb
# wb.open('https://hastagtreinamentos.com')
# 
import time

# tempo_atual_segundos = time.time_ns()

# print(f'tempo atual: {tempo_atual_segundos} segundos desde a epoch')


# inicio = time.time()

# for i in range (100_100_100):
#     pass

# fim = time.time()

# print(f'tempo percorrido {fim - inicio} segundos')

# print ('iniciando a pausa')
# time.sleep(5)
# print ('pausa terminada')

# tempo_em_segundos = time.time()
# tempo_local = time.ctime(tempo_em_segundos)
# print(f'tempo local:{tempo_local}')

# tempo_em_segundos = time.time()
# tempo_local = time.localtime(tempo_em_segundos)

# print(f'tempo local: {tempo_local}')
# print(tempo_local.tm_year)
# print(tempo_local.tm_hour)
# print(tempo_local.tm_wday)
# print(tempo_local.tm_mday)

tempo_em_struct = time.localtime()

# print(time.strftime("%d %B %Y", tempo_em_struct ))
# print(time.strftime("%H:%M:%S", tempo_em_struct))

# tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S ", tempo_em_struct)
# print(f"tempo formatado: {tempo_formatado}")

import locale
import time

locale.setlocale(locale.LC_TIME, "pt_br.UTF-8")
# tempo_formatado = time.strftime("%A, %d de %B de %Y, %H:%M:%S ", tempo_em_struct)
# print(f"tempo formatado: {tempo_formatado}")
time.gmtime()
gmt_struck = time.gmtime()
print (f"tempo em UTC: {gmt_struck}")