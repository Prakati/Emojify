from flask import Flask, render_template, request

app = Flask(__name__)

# Mapping prompts to emojis (You can extend this mapping as needed)
emoji_map = {
    "happy": "😊",
    "sad": "😢",
    "angry": "😡",
    "love": "❤️",
    "confused": "😕",
    "anxiety":"😨",
    "innocent":"😇",
    "sweat smile":"😅",
     "heart eye":"😍",
    "fun":"😆",
    "joy":"😂",
    "blush":"😊",
    "hug":"🤗",
    "crazy":"🤪",
    "think":"🤔",
    "cry":"😭",
    "danger":"☠️",
    "no expression":"😐",
    "confused":"😕",
    "sleep":"😴",
    "sick":"🤧",
    "ready to sleep":"🥱",
    "fear screaming":"😱",
    "kiss":"😗",
    "love you gesture":"🤟",
     "crossed finger":"🤞",
    "cold face":"🥶",
    # Add more prompts and corresponding emojis here
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emojify', methods=['POST'])
def emojify():
    prompt = request.form['prompt'].lower()

    # Check if the prompt exists in the emoji map
    if prompt in emoji_map:
        emoji = emoji_map[prompt]
    else:
        emoji = "❓"  # Default emoji for unknown prompts

    return render_template('index.html', emoji=emoji, prompt=prompt)

if __name__ == '__main__':
    app.run(debug=True)