import os

class Config:
    # Automatically create instance folder if it doesn't exist
    basedir = os.path.abspath(os.path.dirname(__file__))
    instance_path = os.path.join(basedir, '../instance')
    
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{os.path.join(instance_path, "app.db")}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False