def count_words(filename):
    """
    Lee un archivo y retorna un diccionario con la frecuencia de cada palabra.
    """
    word_counts = {}
    
    # Abrimos el archivo. Si no existe, lanzará FileNotFoundError automáticamente.
    with open(filename, 'r', encoding='utf-8') as file:
        # Leemos todo el contenido del archivo
        content = file.read()
        
        # .lower() convierte todo el texto a minúsculas para que el conteo sea case-insensitive
        # .split() sin argumentos separa por cualquier espacio en blanco (espacios, tabs, \n)
        words = content.lower().split()
        
        # Iteramos sobre la lista de palabras generada por split()
        for word in words:
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1
                
    return word_counts