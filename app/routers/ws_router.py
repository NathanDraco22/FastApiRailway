import asyncio, pathlib, csv, random
from fastapi import APIRouter, WebSocket

websocket_router : APIRouter = APIRouter()

@websocket_router.websocket('/random-number')
async def websocket_endpoint(ws : WebSocket):
    await ws.accept()
    while True:
        await asyncio.sleep(0.8)
        a_number : int = random.randint(0,10000)
        await ws.send_text(str(a_number))
    
@websocket_router.websocket("/random-color")
async def websocket_color_endpoint(ws : WebSocket):
    await ws.accept()
    base_path = pathlib.Path(__file__).parent
    file_path = (base_path / "../db/colors.csv").resolve()
    file = open(file_path)
    colors_list = [color for color in csv.reader(file)]
    while True:
        await asyncio.sleep(1.0)
        rand_number = random.randint(0 , len(colors_list))
        current_color = colors_list[rand_number]
        await ws.send_json(
            {
                "name"  : current_color[0],
                "color" : current_color[1]
            }
        )
        
        
