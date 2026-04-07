import os
import requests
import json

def analyze_logs(log_file):
    api_key = os.getenv('AI_API_KEY')
    if not api_key:
        print("Error: AI_API_KEY environment variable missing.")
        return

    try:
        with open(log_file, 'r') as f:
            log_data = f.read()
    except FileNotFoundError:
        print(f"Error: {log_file} not found.")
        return

    # Use Gemini 3 Flash for low-latency threat processing on mobile hardware
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent"
    
    headers = {'Content-Type': 'application/json'}
    payload = {
        "contents": [{
            "parts": [{"text": "Analyze these logs for brute-force or unauthorized access patterns:\n\n" + log_data}]
        }]
    }

    print("Status: Initiating AI Threat Analysis...")
    
    response = requests.post(url, headers=headers, json=payload)
    
    if response.status_code == 200:
        result = response.json()
        analysis = result['candidates'][0]['content']['parts'][0]['text']
        print("\n[ SENTINEL THREAT ASSESSMENT ]\n")
        print(analysis)
    else:
        print(f"API Error {response.status_code}")

if __name__ == "__main__":
    analyze_logs('mock_auth.log')
