from flask import Flask, redirect

app = Flask(__name__)

DISCORD_INVITE = "https://discord.gg/HePGttY9N4"

@app.route('/')
def redirect_to_discord():
    return redirect(DISCORD_INVITE, code=302)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
