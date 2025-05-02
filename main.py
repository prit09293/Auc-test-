from pyrogram import Client
from handlers import auction, bidding, seller, admin, broadcast

app = Client(
    "pokemon_bot",
    bot_token=os.getenv("API_TOKEN"),
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
)

auction.register(app)
bidding.register(app)
seller.register(app)
admin.register(app)
broadcast.register(app)

app.run()
