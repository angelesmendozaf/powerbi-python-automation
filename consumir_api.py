import requests  # Importamos la librería para hacer peticiones HTTP
import pandas as pd  # Para guardar los datos en un CSV

# URL de la API Fake Store
url = "https://fakestoreapi.com/products"

# Hacer la petición GET a la API
response = requests.get(url) #guardamos la peticion 

# Verificar si la respuesta es exitosa (código 200)
if response.status_code == 200:
    print("✅ Conexión exitosa a la API")

    # Convertir la respuesta en JSON (lista de productos)
    data = response.json()
#-------------------------------------------------------------------------------------------------------
   #Mostrar los primeros 2 productos completos para ver la estructura
   # print("\n🔍 Mostrando estructura de los datos:")
   # print(data[:2])  # Muestra solo los primeros 2 productos

    # Extraer y mostrar información clave de los primeros 5 productos
   # print("\n🔍 Mostrando los primeros 5 productos:")
    #for producto in data[:5]:  # Solo mostramos 5 productos para no llenar la pantalla
       # print(f"📦 Producto: {producto['title']}")
        #print(f"💰 Precio: ${producto['price']}")
        #print(f"🏷 Categoría: {producto['category']}")
       # print(f"🖼 Imagen: {producto['image']}")
       # print("-" * 40)  # Separador para mayor claridad

#---------------------------------------------------------------------------------------

 # Crear una lista para almacenar los datos limpios
    productos_limpios = []
 # Extraer y organizar la información clave
    for producto in data:
        productos_limpios.append({
            "Producto": producto["title"],
            "Precio": producto["price"],
            "Categoría": producto["category"],
            "Imagen": producto["image"]
        })

    # Convertir la lista en un DataFrame de pandas
    df = pd.DataFrame(productos_limpios)

    # Guardar el DataFrame en un archivo CSV
    df.to_csv("productos.csv", index=False)

    print("✅ Datos guardados en 'productos.csv'")


else:
    print(f"❌ Error al conectar con la API. Código: {response.status_code}")