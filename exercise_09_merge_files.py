def merge_files(file1, file2, output):
    """
    Concatena el contenido de file1 y file2 en un nuevo archivo llamado output.
    """
    # 1. Leemos el primer archivo
    # Si no existe, lanzará FileNotFoundError aquí y no seguirá adelante
    with open(file1, 'r', encoding='utf-8') as f1:
        content1 = f1.read()
    
    # 2. Leemos el segundo archivo
    # Si no existe, lanzará FileNotFoundError y el archivo output nunca se creará
    with open(file2, 'r', encoding='utf-8') as f2:
        content2 = f2.read()
    
    # 3. Solo si las dos lecturas fueron exitosas, abrimos el output para escribir
    # El modo 'w' sobreescribe si el archivo ya existe
    with open(output, 'w', encoding='utf-8') as out:
        out.write(content1)
        out.write(content2)
        
    # La función retorna None implícitamente