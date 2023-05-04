import time
import logging
from fastapi import FastAPI, Request, Depends,File,UploadFile, status, Response
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, HTMLResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.download import downloadfilesproduct, delete_file, read_html_from_file
from create_graph import create_draft
import pathlib
from uuid import uuid4

origins = ["*"]

logger = logging.getLogger(__name__)


def get_app() -> FastAPI:
    """
    Creates application and all dependable objects.
    """
    description = """"""

    application = FastAPI(
        title="SetiCource",
        description=description,
        docs_url="/swagger",
        openapi_url="/openapi",
        version="1.0.0",
    )
    return application


app = get_app()


@app.on_event("startup")
async def startup() -> None:
    pass


@app.on_event("shutdown")
async def shutdown() -> None:
    pass

@app.post('/file', response_class=HTMLResponse)
async def add_photo(upload_files: UploadFile = File(...),) -> JSONResponse:

    url = await downloadfilesproduct(upload_files)
    id = uuid4()
    file = create_draft(url,id)
    data = read_html_from_file(file)
    delete_file(file)
    delete_file(upload_files.filename)
    return data


@app.get('/file/{name}',response_class=HTMLResponse)
async def main(name):
    folder_path = pathlib.Path(__file__).parent.resolve()
    upload_path = folder_path.joinpath(pathlib.Path("assets"))
    photo_path = upload_path.joinpath(pathlib.Path(f"{name}"))
    with open(photo_path, 'r',encoding="utf8") as fh:
        data = fh.read()
    return data

@app.get("/",response_class=HTMLResponse)
async def root():
    return """<form id="uploadbanner" enctype="multipart/form-data" method="post" action="file">
   <input id="upload_files" name="upload_files" type="file" />
   <input type="submit" value="submit" id="submit" />
</form>"""

@app.middleware("http")
async def log_requst(request: Request, call_next):
    start_time = time.perf_counter()
    response = await call_next(request)
    process_time = time.perf_counter() - start_time
    formatted_process_time = "{0:.5f}".format(process_time)
    logger.info(
        f"""***INFO*** Date time: {time.ctime()}  path={request.url.path} Method {request.method}
                Completed_in = {formatted_process_time}s"""
    )
    return response


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(_request, exc):
    logger.error(f"***ERROR*** Status code 422 Message: {str(exc)}")
    return JSONResponse(status_code=422, content={"details": exc.errors()})


@app.exception_handler(StarletteHTTPException)
async def http_exception(_request, exc):
    logger.error(
        f"***ERROR*** Status code {exc.status_code} Message: {exc.detail}"
    )
    return JSONResponse(
        content={"detail": exc.detail},
        status_code=exc.status_code,
    )



app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)