import discord
from discord.ext import commands
import asyncio


# NOT: 1. sıradaki bot ana botdur . Komutları sadece o dinler ve yanıtlar.
BOT_TOKENS = [
    "ANA_BOT_TOKEN_BURAYA",  
    "TOKEN_2",               
    "TOKEN_3",               
    "TOKEN_4",               
    "TOKEN_5",           
    "TOKEN_6",               
    "TOKEN_7",               
    "TOKEN_8",               
    "TOKEN_9",               
    "TOKEN_10",             
    "TOKEN_11",              
    "TOKEN_12",              
    "TOKEN_13",              
    "TOKEN_14",             
    "TOKEN_15",              
    "TOKEN_16"               
]


active_spams = {}

bot_instances = []


intents = discord.Intents.default()
intents.message_content = True
intents.members = True

def create_bot(token, is_main=False):
    prefix = "." if is_main else None
    b = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)
    
    @b.event
    async def on_ready():
        role_title = "ANA BOT" if is_main else "YARDIMCI BOT"
        print(f"[{role_title}] -> {b.user.name} ({b.user.id}) Aktif!")
        await b.change_presence(activity=discord.Game(name=".yardım | EnesDev"))

    if is_main:
        @b.command(name="yardım")
        async def yardım(ctx):
            embed = discord.Embed(
                title="⚡ Çoklu Token DM Sistemi (16 Bot)",
                description=f"Sistemde toplam **{len(bot_instances)}** bot hazır durumda.\nKomutları sadece **Ana Bot** yanıtlar.",
                color=0x00f0ff # Siber Mavi
            )
            embed.add_field(name="📩 .dm <User_ID> <Mesaj>", value="16 bot birden hedef kişiye durmadan DM atmaya başlar.", inline=False)
            embed.add_field(name="🛑 .stop <User_ID>", value="Tüm botların o kullanıcıya mesaj atmasını durdurur.", inline=False)
            embed.set_footer(text="Enes tarafından yapılmıştır")
            await ctx.send(embed=embed)

        @b.command(name="dm")
        async def dm_baslat(ctx, user_id: int, *, mesaj: str = None):
            if not mesaj:
                await ctx.send("❌ **Mesaj içeriği girmedin!** Örn: `.dm 123456789 Selam`")
                return

            if user_id in active_spams and active_spams[user_id]:
                await ctx.send("⚠️ **Bu kullanıcıya zaten tüm botlar tarafından DM gönderiliyor!**")
                return

            active_spams[user_id] = True
            await ctx.send(f"🚀 **Ana Bot dahil toplam {len(bot_instances)} bot** ile `{user_id}` hedefine DM döngüsü başlatıldı!")

         
            for instance in bot_instances:
                asyncio.create_task(spam_loop(instance, user_id, mesaj))

        ### 3. DM DURDURMA (.stop)
        @b.command(name="stop")
        async def dm_durdur(ctx, user_id: int):
            if user_id in active_spams and active_spams[user_id]:
                active_spams[user_id] = False
                await ctx.send(f"🛑 `{user_id}` için tüm 16 botun döngüsü durduruldu.")
            else:
                await ctx.send("⚠️ Bu kullanıcıya ait aktif bir döngü bulunamadı.")

    return b

async def spam_loop(bot_instance, user_id, mesaj):
    while active_spams.get(user_id, False):
        try:
            # Bot kullanıcısını çek ve mesaj gönder
            target_user = await bot_instance.fetch_user(user_id)
            await target_user.send(mesaj)
            print(f"[{bot_instance.user.name}] -> Başarıyla gönderdi.")
            
     
            await asyncio.sleep(1.5) 
            
        except discord.Forbidden:
            print(f"[{bot_instance.user.name}] -> DM Kapalı/Engelli.")
            await asyncio.sleep(3)
        except discord.HTTPException as e:
            if e.status == 429: # Rate Limit (Hız Sınırı)
                print(f"[{bot_instance.user.name}] -> Hız sınırına takıldı! Bekleniyor...")
                await asyncio.sleep(5)
        except Exception as e:
            await asyncio.sleep(2)


async def main():
    tasks = []
    
    for index, token in enumerate(BOT_TOKENS):
        # İlk token (index 0) ise Ana Bot olarak işaretle
        is_main_bot = (index == 0)
        
        if token and token != f"TOKEN_{index+1}" and token != "ANA_BOT_TOKEN_BURAYA":
            bot_obj = create_bot(token, is_main=is_main_bot)
            bot_instances.append(bot_obj)
            tasks.append(bot_obj.start(token))
    
    if tasks:
        print(f"⚙️ {len(tasks)} adet bot sisteme yükleniyor...")
        await asyncio.gather(*tasks)
    else:
        print("❌ Lütfen BOT_TOKENS listesine geçerli tokenları ekle!")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("🔴 Sistem tamamen kapatıldı.")
