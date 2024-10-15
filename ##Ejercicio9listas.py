##Ejercicio9listas.py

planificacion_vuelos = [
   [      # Lunes
        ["08:00", "Aerolínea A", "2 horas", "Boeing 737"],
        ["12:00", "Aerolínea B", "1.5 horas", "Airbus A320"]
    ],
    [
        # Martes
        ["09:00", "Aerolínea C", "3 horas", "Embraer 190"],
        ["14:00", "Aerolínea A", "2 horas", "Boeing 737"]
    ],
    [
        # Miércoles
        ["10:00", "Aerolínea B", "1.5 horas", "Airbus A320"],
        ["15:00", "Aerolínea C", "3 horas", "Embraer 190"]
    ],
    [
        # Jueves
        ["11:00", "Aerolínea A", "2 horas", "Boeing 737"],
        ["16:00", "Aerolínea B", "1.5 horas", "Airbus A320"]
    ],
    [
        # Viernes
        ["12:00", "Aerolínea C", "3 horas", "Embraer 190"],
        ["17:00", "Aerolínea A", "2 horas", "Boeing 737"]
    ],
    [
        # Sábado
        ["13:00", "Aerolínea B", "1.5 horas", "Airbus A320"],
        ["18:00", "Aerolínea C", "3 horas", "Embraer 190"]
    ],
    [
        # Domingo
        ["14:00", "Aerolínea A", "2 horas", "Boeing 737"],
        ["19:00", "Aerolínea B", "1.5 horas", "Airbus A320"]
    ]
]

# Días de la semana
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

# Función para mostrar la planificación
def mostrar_planificacion():
    for i, dia in enumerate(dias):
        print(f"\n{dia}:")
        for vuelo in planificacion_vuelos[i]:
            horario, compania, duracion, tipo_avion = vuelo
            print(f"  Hora: {horario}, Compañía: {compania}, Duración: {duracion}, Tipo de avión: {tipo_avion}")

# Llamar a la función para mostrar la planificación
mostrar_planificacion()
