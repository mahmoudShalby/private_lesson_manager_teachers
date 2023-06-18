from fastapi import FastAPI
from supabase import create_client as create_supabase_client

app = FastAPI()
supabase_client = create_supabase_client(
    'https://wopquuowrixjxvqhaxlz.supabase.co',
    'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndvcHF1dW93cml4anh2cWhheGx6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4NDg4MzI0OSwiZXhwIjoyMDAwNDU5MjQ5fQ.QoSS8Wl3C-WiNfuzE9eR8EwD2xqSwYMKg5MA-l2M5RI'
)


@app.get('/')
async def root():
    return {'message': 'Hello!'}
