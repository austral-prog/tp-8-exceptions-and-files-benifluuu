def csv_to_dict(filename):
    """
    Lee un archivo CSV y lo convierte en una lista de diccionarios.
    """
    result = []
    
    # Abrimos el archivo. Si no existe, lanza FileNotFoundError automáticamente.
    with open(filename, 'r', encoding='utf-8') as file:
        # Leemos todas las líneas y quitamos espacios/saltos de línea accidentales
        lines = [line.strip() for line in file if line.strip()]
        
        # Si el archivo está vacío o solo tiene la línea de cabecera (header)
        if len(lines) <= 1:
            return []
        
        # La primera línea son las claves: "name,age,city" -> ["name", "age", "city"]
        header = lines[0].split(',')
        
        # Recorremos desde la segunda línea en adelante
        for line in lines[1:]:
            values = line.split(',')
            
            # Creamos el diccionario para la fila actual
            # Realizamos el strip() a cada valor por seguridad
            row_dict = {
                header[0]: values[0].strip(),           # name (str)
                header[1]: int(values[1].strip()),      # age (int)
                header[2]: values[2].strip()            # city (str)
            }
            
            result.append(row_dict)
            
    return result