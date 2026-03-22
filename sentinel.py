import os
import requests
import json

def analyze_logs(log_file):
    api_key = os.getenv('AI_API_KEY')
    if not api_key:
        print("Error: AI_API_KEY not found. Use 'export AI_API_KEY=your_key' in iSH.")
        return

    try:
        with open(log_file, 'r') as f:
            log_data = f.read()
    except FileNotFoundError:
        print(f"Error: {log_file} not found.")
        return

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={api_key}"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": "Analyze these logs for security threats and provide a concise summary:\n\n" + log_data}]
        }]
    }

    print("Status: Requesting threat analysis from Gemini 3...")
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        analysis = result['candidates'][0]['content']['parts'][0]['text']
        print("\n" + "="*20)
        print(" SENTINEL REPORT ")
        print("="*20)
        print(analysis)
    else:
        print(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":
    analyze_logs('mock_auth.log')
