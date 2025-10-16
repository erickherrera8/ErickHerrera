
from fastapi import FastAPI
from datetime import datetime
from zoneinfo import ZoneInfo

ahora = datetime.now()
horaAct = ahora.time()
app = FastAPI()

country_datezone = {
    "CO": "America/Bogota",
    "MX": "America/Mexico_City",
    "PE": "America/Lima",
    "AR": "America/Argentina/Buenos_Aires",
    "CL": "America/Santiago",
    "EC": "America/Guayaquil",
    "VE": "America/Caracas",
    "JP": "Asia/Tokyo",
    "ES": "Europe/Madrid"
}


@app.get("/")
async def root():
    return {"message": "Hello World! :))"}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_datezone.get(iso)
    tz = ZoneInfo(timezone_str)
    return {"time": datetime.now(tz).isoformat()}





@app.get("/weekday/{iso_code}")
async def weekday(iso_code: str):
    iso = iso_code.upper()
    timezone_str = country_datezone.get(iso)
    tz = ZoneInfo(timezone_str)
    day_name = datetime.now(tz).strftime("%A")
    return {"pais": iso, "dia_semana": day_name}
