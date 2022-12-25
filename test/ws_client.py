
import asyncio
import websockets

async def test_client():
    async with websockets.connect("ws://localhost:8000/ws/random-color") as ws:
        counter = 15
        while counter > 1: 
            number = await ws.recv()
            counter -= 1
            print(number)
        await ws.close()

print("start process")
asyncio.run(test_client())
print("end process")