import discord
from discord.ext import commands
import qrcode
import io
import requests

# Khởi tạo bot với prefix là '!'
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập thành công với tên {bot.user}')

@bot.command()
async def qr(ctx, *, text: str):
    """Tạo mã QR từ nội dung người dùng nhập và thêm hình ảnh nền"""
    img = qrcode.make(text)
    with io.BytesIO() as image_binary:
        img.save(image_binary, 'PNG')
        image_binary.seek(0)
        
        # Lấy hình ảnh từ URL
        image_url = "https://cdn.discordapp.com/attachments/1182359780279472148/1345030358395129870/image.png?ex=67c310a2&is=67c1bf22&hm=055195d878011d9a3fe588c3105ce3907bb8f8f7e97ff6839d08290e8301041a&"
        response = requests.get(image_url)
        if response.status_code == 200:
            with open("background.png", "wb") as f:
                f.write(response.content)
        
        await ctx.send(file=discord.File(fp=image_binary, filename='qrcode.png'))

# Chạy bot với token của bạn
bot.run('')
