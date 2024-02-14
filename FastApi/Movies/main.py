from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

# Instanciamos FastAPI

app = FastAPI()

# Cambiamos la documentacion
app.title = "API De Peliculas"
app.version = "1.0"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion"
    },
    {
        "id": 2,
        "title": "Die Hard",
        "overview": "Un policía de Nueva York intenta salvar a su esposa y otros rehenes ...",
        "year": "1988",
        "rating": 8.2,
        "category": "Acción"
    },
    {
        "id": 3,
        "title": "Titanic",
        "overview": "Una joven de la alta sociedad aborda el Titanic para huir de un matrimonio ...",
        "year": "1997",
        "rating": 7.8,
        "category": "Romance"
    },
    {
        "id": 4,
        "title": "The Notebook",
        "overview": "Una joven conoce a un chico del que se enamora, pero su amor es puesto a prueba ...",
        "year": "2004",
        "rating": 7.8,
        "category": "Romance"
    },
    {
        "id": 5,
        "title": "Inception",
        "overview": "Un ladrón que roba secretos corporativos a través del uso del ...",
        "year": "2010",
        "rating": 8.8,
        "category": "Ciencia Ficción"
    },
    {
        "id": 6,
        "title": "Interstellar",
        "overview": "Un grupo de exploradores viaja a través de un agujero de gusano en el espacio ...",
        "year": "2014",
        "rating": 8.6,
        "category": "Ciencia Ficción"
    },
    {
        "id": 7,
        "title": "The Shawshank Redemption",
        "overview": "Dos hombres dentro de una cárcel encuentran la redención ...",
        "year": "1994",
        "rating": 9.3,
        "category": "Drama"
    },
    {
        "id": 8,
        "title": "Forrest Gump",
        "overview": "Un hombre con un coeficiente intelectual bajo lleva una vida extraordinaria ...",
        "year": "1994",
        "rating": 8.8,
        "category": "Drama"
    }
]


# Creamos los endpoints
@app.get("/",tags=["home"])
def message():
    return HTMLResponse(
        content="""
    <h1>Esta es mi aplicación de peliculas<h1>
    <p>Aqui puedes consultar todas las peliculas<p>
    """
    )
    
# Creamos un endpoint para obtener todas las peliculas
@app.get("/movies", tags=["movies"])
def getMovies():
    return movies

# Creamos un endpoin para obtener una pelicula por su id
@app.get("/movies/{id}", tags=["movies"])
def getMovie(id: int):
    for movie in movies:
        if movie["id"] == id:
            return movie
    return {"message": "Pelicula no encontrada"}

# Creamos un endpoint para obtener una pelicula por su categoria
@app.get("/movies/category/{category}", tags=["movies"])
def getMovieByCategory(category: str):
    movieList = []  # Creamos una lista vacia para almacenar las peliculas con la categoria solicitada
    for movie in movies:            #Iteramos sobre todas las peliculas
        if movie["category"] == category:
            movieList.append(movie)     #Si la categoria conincide con la solicitada, agregamos la pelicula a la lista
    if len(movieList) > 0:  #Si la lista no esta vacia, retornamos la lista
        return movieList
    return {"message": "No se encontraron peliculas en esa categoria"}


