days = int(input())
year = int(days / 365)
days %= 365
month = int(days / 30)
days %= 30
print(year, "ano(s)")
print(month, "mes(es)")
print(days, "dia(s)")
