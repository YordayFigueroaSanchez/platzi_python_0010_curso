from store import get_categories
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/")
def get_list():
    return [1,2,3]

@app.get("/contact")
def get_contact():
    return {"name": "Platzi", "email": "contact@platzi.com", "phone": "123456789"}

@app.get("/html", response_class=HTMLResponse)
def get_html():
    return "<h1>Contact</h1>"
    
def main():
    print("Hello from web-server!")
    get_categories()


if __name__ == "__main__":
    main()
