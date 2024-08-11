import uvicorn


def my_run():
    name = input("what's your name: ")
    print(f"Rodando seu projeto {name} !")


if __name__ == "__main__":
    # my_run()
    uvicorn.run(
        app="src.main:app", host="0.0.0.0", port=8000, log_level="info", reload=True
    )
