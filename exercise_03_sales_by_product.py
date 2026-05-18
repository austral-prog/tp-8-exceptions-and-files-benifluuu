def read_sales(filename):
    """
    Lee un archivo con formato producto:valor; y agrupa montos en listas.
    """
    sales_data = {}
    
    # Abrimos el archivo. Si no existe, propaga FileNotFoundError automáticamente.
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read().strip()
        
        # Primero separamos los registros por el punto y coma
        # Ejemplo: ["producto1:100", "producto2:200", ""]
        records = content.split(';')
        
        for record in records:
            # Ignoramos registros vacíos (común si el archivo termina en ;)
            if record:
                # Separamos el nombre del producto del valor
                # Ejemplo: "producto1:100" -> ["producto1", "100"]
                product, value = record.split(':')
                amount = float(value)
                
                # Agrupamos en el diccionario
                if product in sales_data:
                    sales_data[product].append(amount)
                else:
                    # Si es nuevo, inicializamos la lista con el primer monto
                    sales_data[product] = [amount]
                    
    return sales_data

def process_sales(data):
    """
    Calcula totales y promedios, e imprime con formato de dos decimales.
    """
    for product, amounts in data.items():
        total = sum(amounts)
        # Calculamos el promedio (evitando división por cero por seguridad)
        count = len(amounts)
        average = total / count if count > 0 else 0
        
        # Usamos :.2f para asegurar exactamente dos decimales
        print(f"{product}: ventas totales ${total:.2f}, promedio ${average:.2f}")