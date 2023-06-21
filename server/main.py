from fastapi import FastAPI
from django.core.asgi import get_asgi_application

# Initialize FastAPI app
app = FastAPI()

# Settings DJANGO_SETTINGS_MODULE environment variable to describe place of settings
from os import environ
environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

# Mount Django ASGI app
django_app = get_asgi_application()
app.mount("/django", django_app)

# Define FastAPI endpoints
@app.get("/")
async def read_root():
    return {"Hello": "World"}

# Use Django ORM and models
from data.models import Stage
from django.core.serializers import serialize

@app.get("/grades/")
def read_grades():
    return {"grades": serialize('python', Stage.objects.all())}
