import os
from src.app import create_app
from config import config_by_name

env_name = os.environ.get('FLASK_ENV', 'development')
app = create_app(config_by_name[env_name])

if __name__ == '__main__':
    app.run(host='localhost', port=5000, use_reloader = False)