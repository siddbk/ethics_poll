"""
AI Ethics Poll Game - Utility Functions

This module provides helper functions for:
- Generating QR codes for voting links
- Calculating results from votes
- Network utilities for determining server address
"""

import os
import qrcode
import socket
from typing import List, Dict
from models import Response


def generate_qr_code(url: str, scenario_id: str) -> str:
    """
    Generate a QR code for the given URL.
    
    Args:
        url: The URL to encode in the QR code
        scenario_id: The ID of the scenario (used for filename)
        
    Returns:
        Path to the generated QR code image
    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Ensure the qrcodes directory exists
    os.makedirs(os.path.join('static', 'qrcodes'), exist_ok=True)
    
    # Save the QR code
    img_path = os.path.join('static', 'qrcodes', f"{scenario_id}.png")
    img.save(img_path)
    
    return img_path


def calculate_results(responses: List[Response], options: List[Dict[str, str]]) -> Dict[str, int]:
    """
    Calculate the distribution of votes for each option.
    
    Args:
        responses: List of participant responses
        options: List of available options
        
    Returns:
        Dictionary mapping option IDs to vote counts
    """
    results = {option['id']: 0 for option in options}
    
    for response in responses:
        if response.choice in results:
            results[response.choice] += 1
    
    return results


#def get_ip_address() -> str:
    # """
    # Get the local IP address of the machine.
    
    # Returns:
    #     IP address as string
    # """
    # try:
    #     # Create a socket connection to an external server
    #     s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     # Doesn't need to be reachable
    #     s.connect(('8.8.8.8', 1))
    #     ip_address = s.getsockname()[0]
    #     s.close()
    #     return ip_address
    # except Exception:
    #     # Fallback to localhost if we can't determine the IP
    #     return '127.0.0.1'


def get_ip_address() -> str:
    """
    Get the public URL for the application.
    
    Returns:
        Public URL as string
    """
    # Return your PythonAnywhere domain
    return "yourusername.pythonanywhere.com"

def generate_color_palette(num_colors: int) -> List[str]:
    """
    Generate a list of colors for charts.
    
    Args:
        num_colors: Number of colors needed
        
    Returns:
        List of HEX color codes
    """
    base_colors = [
        '#4285F4',  # Google Blue
        '#EA4335',  # Google Red
        '#FBBC05',  # Google Yellow
        '#34A853',  # Google Green
        '#673AB7',  # Purple
        '#3F51B5',  # Indigo
        '#2196F3',  # Light Blue
        '#009688',  # Teal
        '#FF5722',  # Deep Orange
        '#795548',  # Brown
    ]
    
    # If we need more colors than in our base set, just repeat them
    colors = []
    for i in range(num_colors):
        colors.append(base_colors[i % len(base_colors)])
    
    return colors