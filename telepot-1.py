import telepot

bot = telepot.Bot('1474600206:AAHdSqIOulOWNgP5584x6DIknVOmeRz69bU')
#메시지 보내기
bot.sendMessage('1272860274','안녕하세요')
bot.sendChatAction('1272860274','upload_photo')
bot.sendPhoto('1272860274',open('sky.jpeg','rb'),caption="하늘한컷")

