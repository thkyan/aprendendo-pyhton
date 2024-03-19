import time
import locale
# print("Vai começar em 10 segundos.")

# time.sleep(1)
# print("1")
# time.sleep(1)
# print("2")
# time.sleep(1)
# print("3")
# time.sleep(1)
# print("4")
# time.sleep(1)
# print("5")
# time.sleep(1)
# print("6")
# time.sleep(1)
# print("7")
# time.sleep(1)
# print("8")
# time.sleep(1)
# print("9")
# time.sleep(1)
# print("10")
# time.sleep(1)

# print("Fim.")


# tempo_em_struct = time.localtime()
# locale.setlocale(locale.LC_TIME, "pt_br.UTF-8")

# print(time.strftime("%d de %B do ano %Y"))

tempo_atual = time.localtime()
print(tempo_atual.tm_year)
tempo_ano_novo = (tempo_atual.tm_year+1, 1, 1, 0, 0, 0, 0, 0)
print(tempo_ano_novo)

segundos_restantes = int(time.mktime(tempo_ano_novo ) - time.mktime(tempo_atual))
print(segundos_restantes)