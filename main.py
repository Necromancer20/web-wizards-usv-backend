import uvicorn
from fastapi import FastAPI

from controllers.utilizatori import router_utiliziatori

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})
app.include_router(router_utiliziatori)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.10", port=8000)
