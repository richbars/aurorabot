import asyncio
from fastapi import FastAPI
import uvicorn
from bot.main import Aurora

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "API está no ar 🚀"}

async def main():
    config = uvicorn.Config(app, host="0.0.0.0", port=8000, log_level="info")
    server = uvicorn.Server(config)
    api_task = asyncio.create_task(server.serve())
    bot_task = asyncio.create_task(Aurora().start())
    await asyncio.gather(api_task, bot_task)

if __name__ == "__main__":
    asyncio.run(main())
