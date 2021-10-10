#    DARK - UserBot
#    (c) @ZedThon

U = "𓆰 𝑺𝑶𝑼𝑹𝑪𝑬 DARKTHON - 𝑪𝑶𝑴𝑴𝑬𝑵𝑫𝑺 𓆪\n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n**⌔∮ قائـمه اوامر الالعاب :** \n⪼ `.بلاي` لعرض قائمـة الالعـاب الاحترافيـه\n⪼ `.اكس او`\n⪼ `.سهم`\n⪼ `.نرد`\n⪼ `.سلة`\n⪼ `.قدم`\n⪼ `.حظ` \n𓍹ⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧⵧ𓍻\n𓆩 𝙎𝙊𝙐𝙍𝘾𝞝 𝙕𝞝𝘿𝙏𝙃𝙊𝙉 - [𝘿𝙀𝙑](t.me/ZedThon) 𓆪"

@bot.on(admin_cmd(pattern="م22"))
@bot.on(sudo_cmd(pattern="م22", allow_sudo=True))
async def wspr(kimo):
    await eor(kimo, U)

@bot.on(admin_cmd(pattern="اكس او$"))
@bot.on(sudo_cmd(pattern="اكس او$", allow_sudo=True))
async def gamez(event):
    if event.fwd_from:
        return
    botusername = "@xobot"
    noob = "play"
    if event.reply_to_msg_id:
        await event.get_reply_message()
    tap = await bot.inline_query(botusername, noob)
    await tap[0].click(event.chat_id)
    await event.delete()
