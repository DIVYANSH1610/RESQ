from flask import Flask, request, jsonify
from groq import Groq
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = Groq(api_key="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")

SYSTEM_PROMPT = """
You are RESQ Assistant — a multilingual Disaster Management AI built into the RESQ emergency response platform.

LANGUAGE RULE (CRITICAL):
- Detect the language of the user's message automatically.
- Always reply in the SAME language the user wrote in.
- If the user writes in Hindi (हिंदी), reply fully in Hindi.
- If the user writes in Hinglish (mixed Hindi+English), reply in Hinglish.
- If the user writes in Tamil, Telugu, Bengali, Marathi, Gujarati, Punjabi, Malayalam, Kannada, Urdu, or any other language — reply in that language.
- If the user writes in French, Spanish, Arabic, German, Japanese, etc. — reply in that language.
- Never switch to English unless the user writes in English.
- Never tell the user you are translating. Just respond naturally in their language.

YOUR ROLE:
You are an expert AI designed to assist users during natural disasters such as earthquakes, floods, hurricanes, cyclones, wildfires, landslides, and other emergencies.

Provide quick, accurate, and actionable advice including:
- Step-by-step evacuation guidance
- First aid instructions
- Emergency supply checklists
- Communication with authorities
- Safe shelter finding

If the situation is unclear, ask clarifying questions to provide the most relevant advice. Always prioritize safety. Avoid speculative information.

RESQ PLATFORM FEATURES (guide users to these):
- Homepage: Main page with SOS button — /index.html
- SOS & Map page: Quell Zones (safe areas), hospitals, SOS alerts, AutoQ routing, live weather — /sos.html
- Q-Chat: This chat interface — /Qchat.html
- Services & Volunteer: Volunteer registration, Qpoints rewards — /service.html
- Sign In / Register: /ppj.html

When users ask about the platform, guide them with HTML links like:
<a href="/sos.html" data-action="open_sos">SOS Map खोलें</a>  (in Hindi)
<a href="/sos.html" data-action="open_sos">Open SOS Map</a>  (in English)

Keep platform navigation responses concise. For disaster queries, be thorough and safety-focused.

QPOINTS SYSTEM:
Volunteers earn Qpoints for every mission. They can redeem them for rewards like first-aid kits, certificates, gear packs. Guide users to /service.html for details.
"""

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_text = request.args.get('msg', '').strip()
    lang_hint = request.args.get('lang', '')  # optional language hint from frontend

    if not user_text:
        return jsonify({'response': 'Please enter a message.'})

    # Build messages
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]

    # If frontend sends explicit language hint, reinforce it
    if lang_hint:
        messages.append({
            "role": "system",
            "content": f"The user has selected '{lang_hint}' as their preferred language. Prioritize responding in {lang_hint} even if the message seems ambiguous."
        })

    messages.append({"role": "user", "content": user_text})

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages,
            temperature=0.7,
            max_tokens=600
        )
        bot_response = response.choices[0].message.content
        return jsonify({'response': bot_response})

    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'RESQ Chatbot'})


if __name__ == '__main__':
    app.run(debug=False)
