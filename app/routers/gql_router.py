import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class Cosa:
    nombre : str
    edad : int
    def __init__(self, nombre:str, edad: int) -> None:
        self.nombre = nombre
        self.edad = edad
        pass

def booksResolver():
    return [
        Cosa("COSA 1", 700),
        Cosa("COSA 2", 600),
        Cosa("COSA 3", 000),
    ]

@strawberry.type
class Query:
    @strawberry.field
    def cosas()-> list[Cosa]:
        return booksResolver()
    
    @strawberry.field
    def cosa(nombre : str) -> Cosa:
        return Cosa(
            nombre= nombre,
            edad= 9000
        )



schema = strawberry.Schema(Query)

graphQLAPP = GraphQLRouter(schema)




