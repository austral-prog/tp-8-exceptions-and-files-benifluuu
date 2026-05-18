def find_longest_word(filename):
    """
    Lee un archivo y retorna la palabra más larga.
    En caso de empate en longitud, retorna la primera aparición.
    """
    # 1. Abrimos el archivo. Si no existe, lanza FileNotFoundError.
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        
        # 2. Obtenemos todas las palabras (separa por espacios, tabs y \n)
        words = content.split()
        
        # 3. Si no hay palabras, lanzamos ValueError según la consigna
        if not words:
            raise ValueError("file has no words")
            
        # 4. Buscamos la palabra más larga
        longest = words[0]
        
        for word in words:
            # Usamos > para que en caso de empate (longitudes iguales)
            # no reemplace la primera palabra encontrada.
            if len(word) > len(longest):
                longest = word
                
        return longest