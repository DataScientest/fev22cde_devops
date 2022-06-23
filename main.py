from fastapi import FastAPI
import random

api = FastAPI(
    title="Mon API pour les fev22cde"
)


@api.get(
    "/",
    tags=["inutile", "hello world"],
    responses={
        200: {
            "description": "Tout va bien !!!!"
        }
    })
def get_index():
    """FOnction qui ne fait pas grand grand chose
    """
    print("Hello world")
    return {
        "Hello": "World"
    }


@api.post("/mon_post")
def fonction1():
    return {
        "prediction": random.randint(0, 3)
    }


@api.get("/health")
def ma_fonction():
    return {
        "status": 1
    }


@api.delete("/users")
def delete_user():
    return {
        "action": "user deleted",
        "user_id": random.randint(0, 10000)
    }


@api.get("/bye")
def get_bye():
    """Fonction pour dire au revoir
    """
    return {
        "bye": "bye"
    }
