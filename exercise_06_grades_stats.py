def grades_stats(filename):
    """
    Lee un archivo de notas y retorna un diccionario con estadísticas por estudiante.
    """
    stats_dict = {}
    
    # Abrimos el archivo. Si no existe, lanza FileNotFoundError automáticamente.
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Limpiamos la línea y verificamos si no está vacía
            clean_line = line.strip()
            if not clean_line:
                continue
                
            # Separamos el nombre de la cadena de notas
            # "Ana:8,9,7" -> ["Ana", "8,9,7"]
            parts = clean_line.split(':')
            student_name = parts[0]
            grades_str = parts[1]
            
            # Convertimos la cadena de notas en una lista de floats
            # "8,9,7" -> [8.0, 9.0, 7.0]
            grades = [float(n) for n in grades_str.split(',') if n.strip()]
            
            if grades:
                # Realizamos los cálculos solicitados
                avg = sum(grades) / len(grades)
                maximum = max(grades)
                minimum = min(grades)
                
                # Guardamos como tupla (promedio, maximo, minimo)
                stats_dict[student_name] = (avg, maximum, minimum)
                
    return stats_dict