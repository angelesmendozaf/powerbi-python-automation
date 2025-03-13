import requests
import pandas as pd
import schedule
import time

# Función para obtener y guardar los datos desde la API
def actualizar_datos():
    print("🔄 Actualizando datos desde la API...")

    url = "https://fakestoreapi.com/products"  # URL de la API
    response = requests.get(url)  # Hacer la petición GET

    if response.status_code == 200:  # Si la respuesta es exitosa
        data = response.json()  # Convertir a JSON

        # Extraer los datos útiles
        productos_limpios = [
            {
                "Producto": p["title"],
                "Precio": p["price"],
                "Categoría": p["category"]
            }
            for p in data
        ]

        # Guardar en un DataFrame y exportar a CSV
        df = pd.DataFrame(productos_limpios)
        df.to_csv("productos.csv", index=False)

        print("✅ Datos actualizados y guardados en 'productos.csv'")

    else:
        print(f"❌ Error al conectar con la API. Código: {response.status_code}")

# Programar la actualización cada 24 horas
schedule.every(24).hours.do(actualizar_datos)

# Ejecutar la función una vez al inicio
actualizar_datos()

# Mantener el script en ejecución para verificar cada hora
while True:
    schedule.run_pending()
    time.sleep(3600)  # Esperar 1 hora antes de volver a chequear
