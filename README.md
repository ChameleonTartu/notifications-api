[![Analytics](https://ga-beacon.appspot.com/G-R4W32GTLE2/notifications-api/readme)](https://github.com/igrigorik/ga-beacon)

This source code is part of the presentation about secure localhost tunneling.

Developed with [FastAPI](https://fastapi.tiangolo.com/)

It has 2 endpoints:

`GET /` - with predefined response {"message": "Pong"}

`POST /notification` - that returns incoming body and print notification to console

Note: Project developed with `poetry` dependency manager.

To run code: `poetry run uvicorn app:app --reload`
