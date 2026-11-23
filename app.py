
import os
from flask import Flask, render_template, request, jsonify

# Get the directory where app.py is located
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configure Flask folders
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static")
)

# Valorant questions and answers

QUESTIONS = [
    # GENERAL VALORANT QUESTIONS
    {
        "question": "Hii!",
        "keywords": ["hii", "helloo","hey"],
        "answer": "Hey! Locked in and online. What are we covering today—agent roles, map mechanics, weapon buys, or gameplay tips?"
    },
    {
        "question": "What is Valorant?",
        "keywords": ["valorant", "what is valorant"],
        "answer": "Valorant is a free-to-play 5v5 tactical first-person shooter developed by Riot Games."
    },
    {
        "question": "Who created Valorant?",
        "keywords": ["creator", "created", "developer", "riot games"],
        "answer": "Valorant was developed and published by Riot Games."
    },
    {
        "question": "What are the roles in Valorant?",
        "keywords": ["roles", "agent roles", "classes"],
        "answer": "Valorant has four agent roles: Duelist, Controller, Initiator, and Sentinel."
    },
    {
        "question": "What is a Duelist?",
        "keywords": ["duelist"],
        "answer": "Duelists are agents designed to take fights and create opportunities for their team."
    },
    {
        "question": "What is a Controller?",
        "keywords": ["controller"],
        "answer": "Controllers use smokes and other abilities to control areas and block enemy vision."
    },
    {
        "question": "What is an Initiator?",
        "keywords": ["initiator"],
        "answer": "Initiators help their team enter areas by gathering information and disrupting enemies."
    },
    {
        "question": "What is a Sentinel?",
        "keywords": ["sentinel"],
        "answer": "Sentinels specialize in defending areas, gathering information, and protecting teammates."
    },
    {
        "question": "What is Spike?",
        "keywords": ["spike", "plant spike"],
        "answer": "The Spike is the bomb attackers must plant and defend until it detonates."
    },
    {
        "question": "What is an Ace?",
        "keywords": ["ace"],
        "answer": "An Ace happens when one player eliminates all five opponents in a single round."
    },
    {
        "question": "How many players are in a match?",
        "keywords": ["players", "5v5", "five players"],
        "answer": "A standard Valorant match is played between two teams of five players."
    },

    # JETT QUESTIONS
    {
        "question": "Who is Jett?",
        "keywords": ["jett"],
        "answer": "Jett is a Duelist agent known for her mobility, quick movement, and aggressive playstyle."
    },
    {
        "question": "What are Jett's abilities?",
        "keywords": ["jett abilities", "jett skills"],
        "answer": "Jett's abilities are Cloudburst, Updraft, Tailwind, and her ultimate Blade Storm."
    },
    {
        "question": "What is Jett's ultimate ability?",
        "keywords": ["jett ultimate", "blade storm"],
        "answer": "Jett's ultimate Blade Storm equips throwing knives that can eliminate enemies with precise hits."
    },

    # REYNA QUESTIONS
    {
        "question": "Who is Reyna?",
        "keywords": ["reyna"],
        "answer": "Reyna is a Duelist who becomes stronger after eliminating enemies. She can heal and dismiss using soul orbs."
    },
    {
        "question": "What are Reyna's abilities?",
        "keywords": ["reyna abilities", "reyna skills"],
        "answer": "Reyna's abilities are Leer, Devour, Dismiss, and her ultimate Empress."
    },
    {
        "question": "What is Reyna's ultimate ability?",
        "keywords": ["reyna ultimate", "empress"],
        "answer": "Reyna's ultimate Empress enhances her combat abilities and makes her more effective in fights."
    },

    # SAGE QUESTIONS
    {
        "question": "Who is Sage?",
        "keywords": ["sage"],
        "answer": "Sage is a Sentinel who supports her team with healing, barriers, slows, and resurrection."
    },
    {
        "question": "What are Sage's abilities?",
        "keywords": ["sage abilities", "sage skills"],
        "answer": "Sage's abilities are Barrier Orb, Slow Orb, Healing Orb, and her ultimate Resurrection."
    },
    {
        "question": "What is Sage's ultimate ability?",
        "keywords": ["sage ultimate", "resurrection"],
        "answer": "Sage's ultimate Resurrection allows her to revive a fallen teammate."
    },

    # PHOENIX QUESTIONS
    {
        "question": "Who is Phoenix?",
        "keywords": ["phoenix"],
        "answer": "Phoenix is a Duelist who uses fire abilities to damage enemies and heal himself."
    },
    {
        "question": "What are Phoenix's abilities?",
        "keywords": ["phoenix abilities", "phoenix skills"],
        "answer": "Phoenix's abilities are Blaze, Curveball, Hot Hands, and his ultimate Run It Back."
    },
    {
        "question": "Can Phoenix heal himself?",
        "keywords": ["phoenix heal", "phoenix healing"],
        "answer": "Yes, Phoenix can heal himself by standing in his own fire abilities, such as Blaze and Hot Hands."
    },

    # RAZE QUESTIONS
    {
        "question": "Who is Raze?",
        "keywords": ["raze"],
        "answer": "Raze is a Duelist who uses explosive abilities to clear areas and eliminate enemies."
    },
    {
        "question": "What are Raze's abilities?",
        "keywords": ["raze abilities", "raze skills"],
        "answer": "Raze's abilities are Boom Bot, Blast Pack, Paint Shells, and her ultimate Showstopper."
    },
    {
        "question": "What is Raze's ultimate ability?",
        "keywords": ["raze ultimate", "showstopper"],
        "answer": "Raze's ultimate Showstopper equips a rocket launcher that deals powerful explosive damage."
    },

    # MAP QUESTIONS
    {
        "question": "What is the Ascent map?",
        "keywords": ["ascent", "ascent map"],
        "answer": "Ascent is a Valorant map featuring two bomb sites, open mid control, and mechanical doors."
    },
    {
        "question": "What is the Bind map?",
        "keywords": ["bind", "bind map"],
        "answer": "Bind is a map with two bomb sites and teleporters that allow players to rotate quickly."
    },
    {
        "question": "What is the Haven map?",
        "keywords": ["haven", "haven map"],
        "answer": "Haven is a unique Valorant map featuring three bomb sites: A, B, and C."
    },
    {
        "question": "What is the Split map?",
        "keywords": ["split", "split map"],
        "answer": "Split is a map known for vertical gameplay, ropes, and narrow pathways."
    },
    {
        "question": "What is the Lotus map?",
        "keywords": ["lotus", "lotus map"],
        "answer": "Lotus is a three-site map featuring rotating doors, destructible doors, and a silent drop."
    },
    {
        "question": "What is the Sunset map?",
        "keywords": ["sunset", "sunset map"],
        "answer": "Sunset is a two-site map featuring a central market area and important mid-control routes."
    },

    # WEAPON QUESTIONS
    {
        "question": "What are the weapon categories in Valorant?",
        "keywords": ["weapon categories", "gun types", "weapon types"],
        "answer": "Valorant weapons are divided into Sidearms, SMGs, Shotguns, Rifles, Sniper Rifles, Machine Guns, and Melee."
    },
    {
        "question": "What is the Vandal?",
        "keywords": ["vandal", "vandal weapon"],
        "answer": "Vandal is a powerful rifle that can eliminate an enemy with one headshot at any range."
    },
    {
        "question": "What is the Phantom?",
        "keywords": ["phantom", "phantom rifle"],
        "answer": "Phantom is an automatic rifle with a high fire rate, silenced shots, and a 30-round magazine."
    },
    {
        "question": "What is the Operator?",
        "keywords": ["operator", "operator sniper"],
        "answer": "Operator is a powerful sniper rifle that can eliminate most enemies with a single body shot."
    },
    {
        "question": "What is the Sheriff?",
        "keywords": ["sheriff", "sheriff pistol"],
        "answer": "Sheriff is a powerful sidearm known for its high damage and accurate headshots."
    },
    {
        "question": "Which is better, Vandal or Phantom?",
        "keywords": ["vandal vs phantom", "better rifle", "best rifle"],
        "answer": "Both are popular rifles. Vandal offers consistent damage at range, while Phantom has a higher fire rate and is easier to control in many close-range fights."
    }
]


# Normalize user input
def normalize_text(text):
    return text.lower().strip()


# Find the best matching answer
def find_answer(user_message):
    message = normalize_text(user_message)

    best_answer = None
    best_score = 0

    for item in QUESTIONS:
        score = 0

        for keyword in item["keywords"]:
            if keyword in message:
                score += len(keyword.split())

        if score > best_score:
            best_score = score
            best_answer = item["answer"]

    if best_answer:
        return best_answer

    return (
        "I don't have an answer for that yet! "
        "Try asking me about Valorant agents, abilities, "
        "roles, maps, or gameplay."
    )


# Home page
@app.route("/")
def home():
    return render_template("index.html")


# Chat API
@app.route("/api/chat", methods=["POST"])
def chat():

    data = request.get_json(silent=True) or {}

    message = data.get("message", "")

    if not isinstance(message, str):
        return jsonify({
            "reply": "Invalid message format."
        }), 400

    message = message.strip()

    if not message:
        return jsonify({
            "reply": "Please enter a message, Agent!"
        }), 400

    if len(message) > 300:
        return jsonify({
            "reply": "Please keep your message under 300 characters."
        }), 400

    answer = find_answer(message)

    return jsonify({
        "reply": answer
    })


# Suggested questions API
@app.route("/api/questions", methods=["GET"])
def get_questions():

    questions = [
        item["question"]
        for item in QUESTIONS
    ]

    return jsonify(questions)


# Run Flask application
if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True
    )
