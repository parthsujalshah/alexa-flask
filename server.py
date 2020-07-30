from flask import Flask
from flask_ask_sdk.skill_adapter import SkillAdapter
from hello_world import sb

app = Flask(__name__)

skill_adapter = SkillAdapter(skill=sb.create(), skill_id='amzn1.ask.skill.41125c2b-0229-4ff4-8ea4-5290ad3830ea', app=app)

# @app.route("/", methods=['GET', 'POST'])
# def invoke_skill():
#     return skill_adapter.dispatch_request()

skill_adapter.register(app=app, route="/")

@app.route("/test", methods=['GET', 'POST'])
def test():
    return 'hello world'

if __name__ == "__main__":
    app.run(debug=True, port='443')