import websocket
import _thread
import time

def on_message(ws, message):
    print(f"Received: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, code, reason):
    print("### closed ###")

def on_open(ws):
    def run(*args):
        ws.send("Hello from Python Client!")
        time.sleep(1)
        ws.close()
    _thread.start_new_thread(run, ())

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://10.5.12.106:8080/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
