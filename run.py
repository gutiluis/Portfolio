if __name__ == "__main__":  # no need for application conext manager
    from app import create_app

    app = create_app()
    app.run(host="127.0.0.1", debug=True, port=8000)
