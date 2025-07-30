import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/website_builder')
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')
    HUGGINGFACE_API_KEY = os.getenv('HUGGINGFACE_API_KEY', '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')
