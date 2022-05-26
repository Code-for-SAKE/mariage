import uvicorn
import main

if __name__ == "__main__":
    uvicorn.run(app=main.app, host="0.0.0.0", port=3040)