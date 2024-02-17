from fastapi import FastAPI, Body ,Path, Query, HTTPException # Importamos la clase FastAPI para instanciar nuestra API y la clase Body para validar los datos
from pydantic import BaseModel, Field # Importamos la clase BaseModel para validar los datos y la clase field para definir los campos
from typing import Optional, List
from fastapi.responses import HTMLResponse, JSONResponse # Importamos las clases HTMLResponse y JSONResponse para cambiar el tipo de respuesta

# Instanciamos FastAPI

app = FastAPI()


# Creamos un schema para validar los datos 
class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(default="Mi Pelicula", min_length=5, max_length=30)
    overview: str = Field(default="Descripcion de la película", min_length=10, max_length=300)
    year: int = Field(default=2022, le=2022)
    rating: float = Field(default=10, ge=0, le=10)
    category: str = Field(default="Comedia", min_length=3, max_length=15)

class User(BaseModel):
    email: str
    password: str


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
@app.get("/movies", tags=["movies"], response_model=List[Movie], status_code=200)
def getMovies():
    return JSONResponse(status_code=200, content=movies)

# Creamos un endpoin para obtener una pelicula por su id

@app.get("/movies/{id}", tags=['movies'])
def getMovie(id: int = Path(ge=1, le=2000)):
    movie = next((movie for movie in movies if movie['id'] == id), None)
    if movie is not None:
        return movie
    else:
        raise HTTPException(status_code=404, detail="Movie not found")
    
# Creamos un endpoint para obtener una pelicula por su categoria
@app.get("/movies/", tags=['movies'], response_model=List[Movie], status_code = 200 )
def getMovieByCategory(category: str = Query(min_length=3, max_length=15)):
    getMovieByCategory = [movie for movie in movies if movie['category'] == category]
    return JSONResponse(status_code=200, content=getMovieByCategory)


# Craamos un endpoint para modificar una pelicula
@app.post("/movies", tags=['movies'])
def createMovie(movie: Movie):
    movies.append(movie)
    return JSONResponse(status_code=201, content={"message": "Movie created successfully"})
# Funcion para actualizar una pelicula
@app.put("/movies/{id}", tags=['movies'], response_model=dict, status_code=200)
def updateMovie(id: int,
                movie: Movie):
    for movie in movies:
        if movie['id'] == id:
            movie['title'] = movie.title
            movie['overview'] = movie.overview
            movie['year'] = movie.year
            movie['rating'] = movie.rating
            movie['category'] = movie.category
    return JSONResponse(content={"message": "Movie updated successfully"}, status_code=200)

# Funcion para eliminar una pelicula
@app.delete("/movies/{id}", tags=['movies'],response_model= dict,status_code=200)
def deleteMovie(id: int):
    for movie in movies:
        if movie['id'] == id:
            movies.remove(movie)
            break
    return JSONResponse(content={"message": "Movie deleted succesfully"}, status_code=200)


