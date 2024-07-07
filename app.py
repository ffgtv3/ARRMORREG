from flask import Flask, request, render_template
import discord

app = Flask(__name__)

# Настройки Discord-бота
DISCORD_TOKEN = 'your_discord_bot_token'
DISCORD_CHANNEL_ID = '1213106308136304690'

# Инициализация Discord-клиента
client = discord.Client()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/support', methods=['POST'])
def support():
    message = request.json['message']
    send_discord_message(message)
    return 'OK'

def send_discord_message(message):
    @client.event
    async def on_ready():
        channel = client.get_channel(int(DISCORD_CHANNEL_ID))
        await channel.send(message)
        client.close()

    client.run(DISCORD_TOKEN)

if __name__ == '__main__':
    app.run()
