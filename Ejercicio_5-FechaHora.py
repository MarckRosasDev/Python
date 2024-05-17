from datetime import datetime, timedelta, timezone
import pytz

print('---Fecha y hora actual---')
fechaHora = datetime.now()
print(fechaHora)
print(type(fechaHora))
print(fechaHora.date())
print(fechaHora.time())

print('---Fecha---')
print(fechaHora.year)
print(fechaHora.month)
print(fechaHora.day)

print('---Hora---')
print(fechaHora.hour)
print(fechaHora.minute)
print(fechaHora.second)
print(fechaHora.microsecond)

print('---Con formato---')
print("{}:{}:{}".format(fechaHora.hour, fechaHora.minute, fechaHora.second))
print("{}/{}/{}".format(fechaHora.day, fechaHora.month, fechaHora.year))

print(fechaHora.strftime("%Y-%m-%d"))
print(fechaHora.strftime("%A-%d-%B %Y"))
print(fechaHora.strftime("%H:%M:%S"))
print(fechaHora.strftime('%d/%m/%Y %H:%M:%S')) # En español
print('---En inglés---')
print(fechaHora.strftime("%A %d %B %Y %I:%M")) # En inglés
print('---Formato ISO---')
print(fechaHora.isoformat()) # (Organización Internacional de Normalización)

print('---Fecha y hora específica---')
fecha_especifica = datetime(2024, 5, 17)
print(fecha_especifica)

fecha_hora_especifica = datetime(2024, 5, 17, 11, 24, 0)
print(fecha_hora_especifica)

fecha_hora_especifica = fecha_hora_especifica.replace(year=2030) # Reemplazar año específico
print(fecha_hora_especifica)

print('---Diferencia entre fechas---')
fecha_inicio = datetime(2024, 5, 10)
fecha_fin = datetime(2024, 5, 17)

diferencia_dias = fecha_fin - fecha_inicio
print(f'Diferencia en días: {diferencia_dias.days}')

diferencia_horas = fecha_fin - fecha_inicio
print(f'Diferencia en horas: {diferencia_horas.total_seconds()/3600}')

print('---Zonas horarias---')
print(pytz.all_timezones)

zona_horaria_elegida = datetime.now(pytz.timezone('Asia/Tokyo'))
print(zona_horaria_elegida.strftime('%A %d de %B del %Y - %H:%M')) # %I -> 12h  - %H -> 24h