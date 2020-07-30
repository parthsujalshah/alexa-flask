from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter
from hello_world import sb

app = Flask(__name__)

skill_adapter = SkillAdapter(skill=sb.create(), skill_id=1, app=app)

@app.route("/", methods=['GET', 'POST'])
def invoke_skill():
    return skill_adapter.dispatch_request()

if __name__ == "__main__":
    app.run(debug=True, port='443')