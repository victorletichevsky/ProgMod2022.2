
from asyncio.windows_events import NULL
import interactions
import crypto

bot = interactions.Client(token="MTAyOTE2ODAzMDExMjAzMDgxMQ.GS4XI6.Js4J_UUiJth_FOvIUCdB9DtXFCgU8WNC8NoRsc")

@bot.command(
    name="cryptograph",
    description="This command crytographs the input string",
    scope=828690812296364093,
    options = [
        interactions.Option(
            name="text",
            description="This command crytographs the input string",
            type=interactions.OptionType.STRING,
            required=True,
        ),
		interactions.Option(
            name="key",
            description="If you have a specific key input it here",
            type=interactions.OptionType.STRING,
            required=False,
        )
    ],
)

async def EncryptCommand(ctx: interactions.CommandContext, text: str, Inputkey: str = NULL):
	Result = crypto.encrypt(text, key=Inputkey)
	await ctx.send(f"Your encrypted text is:\n `{Result[0]}` \n Your key is: \n`{Result[1]}`")

@bot.command(
    name="decryptograph",
    description="This command decrytographs the input string",
    scope=828690812296364093,
    options = [
        interactions.Option(
            name="text",
            description="This command decrytographs the input string",
            type=interactions.OptionType.STRING,
            required=True,
        ),
		interactions.Option(
            name="key",
            description="Input your key to decrypt the text",
            type=interactions.OptionType.STRING,
            required=True,
        )
    ],
)
async def DecryptCommand(ctx: interactions.CommandContext, text: str, key: str):
	Result = crypto.decrypt(text, key)
	await ctx.send(f"Your text is: `{Result}`!")

bot.start()
