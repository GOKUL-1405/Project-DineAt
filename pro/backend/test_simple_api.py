#!/usr/bin/env python
"""
Simple API test
"""

import os
import sys
from decouple import config

# Add the project directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

try:
    import google.generativeai as genai
    print("✅ google-generativeai package imported successfully")
except ImportError as e:
    print(f"❌ Failed to import google-generativeai: {e}")
    sys.exit(1)

# Test API key
api_key = config('GEMINI_API_KEY', default=None)
if not api_key:
    print("❌ GEMINI_API_KEY not found")
    sys.exit(1)

print(f"✅ API key found: {api_key[:20]}...")

# Test with different models
models_to_try = [
    'models/gemini-1.5-flash',
    'models/gemini-1.5-pro',
    'models/gemini-pro',
    'gemini-1.5-flash',
    'gemini-pro'
]

for model_name in models_to_try:
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(model_name)
        print(f"✅ Gemini model '{model_name}' initialized successfully")
        
        # Test a simple query
        response = model.generate_content("Hello! Please respond with 'API test successful'.")
        print(f"✅ API test response: {response.text}")
        print(f"🎉 Model '{model_name}' works!")
        break
        
    except Exception as e:
        print(f"❌ Model '{model_name}' failed: {e}")
        continue
else:
    print("❌ All models failed. Chatbot will use fallback responses.")
