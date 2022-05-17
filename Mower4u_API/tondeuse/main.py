from typing import List

from fastapi import Depends, FastAPI, HTTPException

from . import toolkit, schemas

import warnings

warnings.simplefilter(action="ignore", category=FutureWarning)

app = FastAPI()


@app.post("/attractiveness/", response_model=schemas.MowerAttractiveness)
def attractiveness(mower: schemas.Mower):
    mower_dict = mower.dict()
    mower_dict["attractiveness"] = toolkit.predict_attractiveness(mower_dict)
    return mower_dict
