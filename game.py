from flask import Flask, request, jsonify 
from flask_restful import Api, Resource
import random

session = {}
unknown_message = {"result": "UNKNOWN"}

#Dictionaries to define what beats what. 
base_rules = {
              "scissors": ("paper","lizard"),
              "paper": ("rock", "spock"),
              "rock" : ("lizard", "scissors")
             }
             
additional_rules = {
                    "lizard" : ("spock", "paper"),
                    "spock": ("scissors", "rock")
                   }

class Game(Resource):

    def get(self):
        return jsonify( {
                         "You": session["score"][0], 
                         "Computer": session["score"][1]
                        }
                      )

    def post(self):
        data = request.get_json(force=True)

        if "mode" in data:
            if reset(data["mode"].lower()):
                return jsonify(
                                "Game has been reset and mode changed to " + 
                                 data["mode"].upper()
                               )
            else: 
                return jsonify(unknown_message)

        if not "hand" in data:
            return jsonify(unknown_message)

        hand = data["hand"].lower()
        if hand not in session["hands"]:
            return jsonify(unknown_message)

        # Computer plays its hand
        computer_hand = random.choice(session["hands"])

        if computer_hand == hand:
            status = "DRAW" 
        elif computer_hand in session["rules"][hand]:
            status = "WON"
            session["score"] = (session["score"][0] + 1, session["score"][1])
        else:
            status = "LOST"
            session["score"] = (session["score"][0], session["score"][1] + 1)
             
        return jsonify({"result": status.upper(), "computerHand": computer_hand.upper()}) #

def reset(mode):
   
    if mode == "advanced":
        session["rules"] = {**base_rules, **additional_rules}
    elif mode == "classic":
        session["rules"] = base_rules
    else:
        return False

    session["score"] = (0, 0)
    session["hands"] = list(session["rules"].keys())
    return True


# by default it's runs in classic mode
reset("classic")

app = Flask(__name__)
api = Api(app)
api.add_resource(Game, "/game")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=4567)
