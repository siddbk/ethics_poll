# created for pythonanywhere access and op

from app import app as application
import os

# Create required directories
base_dir = os.path.dirname(os.path.abspath(__file__))
os.makedirs(os.path.join(base_dir, 'static', 'qrcodes'), exist_ok=True)
os.makedirs(os.path.join(base_dir, 'static', 'exports'), exist_ok=True)