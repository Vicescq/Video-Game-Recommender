from flaskapi import create_app
from flaskapi.routes import main_bp

if __name__ == "__main__":
    app = create_app(main_bp)
    app.run()