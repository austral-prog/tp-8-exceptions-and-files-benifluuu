def parse_log(filename):
    """
    Lee un archivo de log y agrupa los mensajes por nivel de severidad.
    """
    log_data = {}
    
    # 1. Abrimos el archivo. Si no existe, propaga FileNotFoundError automáticamente.
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Ignoramos líneas que solo contienen espacios o están vacías
            clean_line = line.strip()
            if not clean_line:
                continue
            
            # 2. Verificamos si la línea es válida (debe contener ':')
            if ':' not in clean_line:
                raise ValueError("invalid log line")
            
            # 3. Dividimos por el PRIMER ':' que aparezca
            # El parámetro 1 en split garantiza que si el mensaje contiene :, no se rompa
            level, message = clean_line.split(':', 1)
            
            # Limpiamos espacios sobrantes del nivel y del mensaje
            level = level.strip()
            message = message.strip()
            
            # 4. Agrupamos en el diccionario de listas
            if level in log_data:
                log_data[level].append(message)
            else:
                log_data[level] = [message]
                
    return log_data