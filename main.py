from telethon import TelegramClient
import pyperclip
import asyncio
import time

# Вставьте свои данные
API_ID = '24275090'
API_HASH = '8a5114253d99c03553ca1755fc9441f0'
PHOTO_PATH = 'photo.jpg'  # Укажите путь к фото


async def main():
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        dialogs = await client.get_dialogs()

        folders = {}
        for dialog in dialogs:
            if dialog.folder_id is not None:
                if dialog.folder_id not in folders:
                    folders[dialog.folder_id] = []
                folders[dialog.folder_id].append(dialog)



        folder_list = list(folders.keys())
        for idx, folder_id in enumerate(folder_list, start=1):
            print(f"{idx}. Папка {folder_id} (Чатов: {len(folders[folder_id])})")

        folder_number = 1
        selected_folder_id = folder_list[folder_number - 1]
        chats_in_folder = folders[selected_folder_id]

        interval = 300

        while True:
            message = """⭑･ﾟﾟ･::･｡⋆💫⋆｡･::･ﾟﾟ･⭑
                    ✨ Продажа Telegram Stars ✨
                    💫 через бота — @starwand_bot 💫

                    📌 Курс: 1🌟 = 1.58₽
                    💳 Оплата: карта, криптобот и другие способы
                    🤝 Иду на бесплатного гаранта при крупной сумме

                    ⭑･ﾟﾟ･::･｡⋆📎⋆｡･::･ﾟﾟ･⭑

                    ⚡ Также продаю софт для спама — 80₽ ⚡️

                    ⭑･ﾟﾟ･::･｡⋆💫⋆｡･::･ﾟﾟ･⭑"""
            if not message:
                print("Буфер обмена пуст! Ожидаю новое сообщение...")
                time.sleep(interval)
                continue

            print(f"Рассылка сообщения в {len(chats_in_folder)} чатов из папки {selected_folder_id}:\n{message}\n")

            for chat in chats_in_folder:
                try:
                    await client.send_file(chat.entity, PHOTO_PATH, caption=message)
                    print(f"Сообщение с фото отправлено в {chat.name}")
                except Exception as e:
                    print(f"Ошибка отправки в {chat.name}: {e}")

            print("Ожидание перед следующей отправкой...")
            time.sleep(interval)


if __name__ == "__main__":
    asyncio.run(main())
