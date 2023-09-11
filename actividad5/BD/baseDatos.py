from pymongo.mongo_client import MongoClient # lo primero es importar mongo para conectarnos a las base de datos de Mongo

#CONEXIÓN
def conexion(): #Después se define la función de datos de Mongo, este código lo copiamos de la pagina de Mongo
    uri = "mongodb+srv://cagomezj:1234@cluster0.cgumkrz.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    return MongoClient(uri)

#CREATE: con este código se añaden datos a nuestra base de datos de Mongo
""" Código necesario para crear un create en MongoDB"""


#READ : con este código vemos lo que se tiene en la base de mongo
""" Código necesario para crear un read en MongoDB"""
def lecturaDatos(): # Aquí creamos una función llamada lectura de datos donde nos muestra todo lo que tenemos en la base de Mongo
    client = conexion() # Llama a la función conexion para establecer conexión con la base de datos de Mongo, es decir client se conecta a Mongoclient
    db = client.actividad4.data_real # En esta línea se accede a la base de datos actividad4 y luego a la colección data real
    data_list = [] # Se crea una lista vacia donde se almacenarán documentos de la base de datos recuperados
    for data_real_bd in db.find(): # Se recuperan todos los documentos de la colección 
        data_list.append(data_real_bd) # cada vez que se itera, se agrega una lista a data_list, y se van acumulando.
    return data_list # Nos muestra todo lo relacionado anteriormente

#UPDATE
""" Código necesario para actualizar un dato en la BD""" # Espacio para funciones a futuro 

#DELETE
""" Código necesario para eliminar un dato en la BD""" # Espacio para borrar datos de la base a futuro 