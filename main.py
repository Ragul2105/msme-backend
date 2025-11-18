#!/usr/bin/env python3
"""
Production entry point for Plant Disease Detection API
Optimized for Render deployment
"""

import os
from plant_disease_app import app

if __name__ == '__main__':
    # Get port from environment variable (Render sets this)
    port = int(os.environ.get('PORT', 10000))
    
    print(f"🚀 Starting Plant Disease Detection API on port {port}")
    print("🌍 Production mode enabled")
    
    # Run the app
    app.run(
        host='0.0.0.0',
        port=port,
        debug=False  # Disable debug in production
    )