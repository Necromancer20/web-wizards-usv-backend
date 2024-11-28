import uvicorn
from fastapi import FastAPI

from controllers.utilizatori import router_utiliziatori
from controllers.specializari import router_specializari
from controllers.programari_examen import router_programari_examen
from controllers.materii import router_materii
from controllers.grupe import router_grupe
from controllers.facultati import router_facultati

app = FastAPI(swagger_ui_parameters={"syntaxHighlight": True})
app.include_router(router_utiliziatori)
app.include_router(router_specializari)
app.include_router(router_programari_examen)
app.include_router(router_materii)
app.include_router(router_grupe)
app.include_router(router_facultati)

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.10", port=8000)
