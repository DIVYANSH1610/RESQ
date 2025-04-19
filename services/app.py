from flask import Flask, request, jsonify, render_template
from groq import Groq
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
groq_api_key = os.getenv("GROQ_API_KEY")
# groq_api_key = "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"
client = Groq(api_key=groq_api_key)

@app.route('/')
# def home():
    # return render_template('Qchat.html')

@app.route('/get', methods=['GET'])
def get_bot_response():
    user_text = request.args.get('msg')
    if not user_text:
        return jsonify({'response': 'Please enter a message.'})

    try:
        # Call Groq API for response
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a Disaster Management Assistant, an expert AI designed to assist users during natural disasters "
                        "such as earthquakes, floods, hurricanes, wildfires, and other emergencies. Provide quick, accurate, and "
                        "actionable advice to ensure user safety and preparedness, including step-by-step guidance for evacuation, "
                        "first aid, emergency supplies, and communication with authorities. If the situation is unclear, ask clarifying "
                        "questions to provide the most relevant advice. Always prioritize safety and reliability, and avoid speculative "
                        "information.\n\n"
                        "You are also integrated into a disaster management web platform (RESQ/Emergency SOS Hub) with the following features:\n"
                        "- **Homepage (/RESQ/index.html)**: Main page with an overview and SOS button to send emergency alerts.\n"
                        "- **Interactive Map (/RESQ/sos.html)**: Shows Quell Zones (safe areas like Civil Hospital, Lohia Hospital, Community Shelter "
                        "in Lucknow), hospitals, and SOS points with navigation and real-time weather.\n"
                        "- **SOS Page (/RESQ/sos.html)**: Allows users to send emergency alerts and connect with volunteers via Q-Link.\n"
                        "- **AutoQ**: Predictive routing to guide users to the nearest Quell Zone (accessible via the map).\n"
                        "- **Q-Link**: Communication bridge for users, volunteers, and command centers (accessible via /RESQ/sos.html).\n"
                        "When users ask about using the platform, guide them to the relevant page or feature with clear instructions, "
                        "including URLs (e.g., '/RESQ/sos.html' for the map) or actions (e.g., 'Click the SOS button'). Use HTML links in responses "
                        "like <a href=\"/RESQ/sos.html\" data-action=\"open_map\">Go to Map</a> for navigation. For platform-related queries, keep "
                        "responses concise and include navigation tips. For disaster queries, focus on safety and actionable steps."
                    )
                },
                {"role": "user", "content": user_text}
            ],
            temperature=0.7,
            max_tokens=500
        )
        bot_response = response.choices[0].message.content
        return jsonify({'response': bot_response})
    except Exception as e:
        return jsonify({'response': f'Error: {str(e)}'})

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=False)