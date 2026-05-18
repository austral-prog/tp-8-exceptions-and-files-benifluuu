def read_lines(filename):
    """
    Lee un archivo de texto y retorna una lista con sus líneas procesadas.
    """
    lines = []
    
    # Abrimos el archivo en modo lectura ('r')
    # No capturamos el FileNotFoundError aquí para que se propague como pide la consigna
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # .strip() elimina espacios en blanco y saltos de línea (\n) al inicio y final
            clean_line = line.strip()
            
            # Solo agregamos a la lista si la línea resultante no está vacía
            if clean_line:
                lines.append(clean_line)
                
    return lines