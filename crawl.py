from telethon import TelegramClient
import pandas as pd

if __name__ == "__main__":
    api_id = 1128915
    api_hash = "537286efa5287aaa39537fc44f1dc75c"
    group_username = "Der Corner des Grauens. Eine Einführung."
    client = TelegramClient('anon', api_id, api_hash)

    async def main():
        all_messages = []
        # You can print the message history of any chat:
        async for message in client.iter_messages(
                'Der Corner des Grauens. Eine Einführung.'):
            if message.date.year < 2019:
                break
            sender = await message.get_sender()
            all_messages.append(dict(name=sender.first_name, text=message.text,
                                     date=message.date))

        pd.DataFrame(all_messages).to_csv("data/corner_2019.csv")




    with client:
        client.loop.run_until_complete(main())
