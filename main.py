from unicodedata import name
import discord
from discord.commands import Option
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), help_command=None)

@bot.event
async def on_ready():
    print("실행중")

@bot.slash_command(name="면접")
async def result(ctx, user: Option(discord.Member, name="유저", description="결과를 통지할 유저 맨션"), result: Option(str, name="결과", description="합격인지 불합격인지 골라주세요", choices=["합격","불합격"]), reason: Option(str, name="이유", description="이유도 적을꺼면 입력하고 안써도됨", required=False, default=None)):
    if result == "합격":
        embed = discord.Embed(title="OHB팀 면접 결과", color=discord.Color.green())
        embed.add_field(name="면접 결과는!!", value="__**합격**__입니다!", inline=False)
        await ctx.respond("면접결과를 보냈습니다")
        await user.send(embed=embed)
    if result == "불합격":
        if reason == None:
            embed = discord.Embed(title="OHB팀 면접 결과", color=discord.Color.red())
            embed.add_field(name="면접 결과는!!", value="__**불합격**__입니다...", inline=False)
            embed.add_field(name="이유", value="궁금하시면 직접 물어봐주세요!",inline=False)
            await ctx.respond("면접결과를 보냈습니다")
            await user.send(embed=embed)
        else:
            embed = discord.Embed(title="OHB팀 면접 결과", color=discord.Color.red())
            embed.add_field(name="면접 결과는!!", value="__**불합격**__입니다...", inline=False)
            embed.add_field(name="이유", value=f"{reason}",inline=False)
            await ctx.respond("면접결과를 보냈습니다")
            await user.send(embed=embed)




bot.run("MTAyNDYzNzQzMDM4NjY1NTI2Mg.GqqF7Q.gmRsdvpeaW9A0zIJwb5wj0EIdX9EChyIHA2xxI")
