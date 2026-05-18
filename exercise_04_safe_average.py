def safe_average(filename):
    """
    Lee un archivo, calcula el promedio de los números que contiene
    e ignora las líneas que no son numéricas.
    """
    numbers = []
    
    # 1. El test espera que si el archivo no existe, se lance FileNotFoundError
    # Al no usar try/except en el open, la excepción se propaga sola.
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.strip()
            if clean_line:
                try:
                    # Intentamos convertir la línea a número
                    num = float(clean_line)
                    numbers.append(num)
                except ValueError:
                    # Si no es un número (ej: "hola"), el test pide ignorarlo
                    continue
    
    # 2. Si después de leer todo no encontramos NINGÚN número válido,
    # el test espera un ValueError (según los fallos que mostraste).
    if not numbers:
        raise ValueError("No se encontraron números válidos en el archivo")
    
    # 3. Retornamos el promedio
    return sum(numbers) / len(numbers)