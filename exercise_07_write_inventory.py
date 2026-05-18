def write_inventory(filename, inventory):
    """
    Escribe el inventario en un archivo, ordenado alfabéticamente por item.
    """
    # 1. Obtenemos las claves (items) y las ordenamos alfabéticamente
    sorted_items = sorted(inventory.keys())
    
    # 2. Abrimos el archivo en modo escritura ('w')
    # Esto creará el archivo si no existe, o lo sobrescribirá si ya existe.
    with open(filename, 'w', encoding='utf-8') as file:
        for item in sorted_items:
            quantity = inventory[item]
            # 3. Escribimos con el formato item:cantidad seguido de salto de línea
            file.write(f"{item}:{quantity}\n")
            
    # La función no necesita un return explícito para devolver None