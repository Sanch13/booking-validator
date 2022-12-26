from aiogram.types import ChatMember


def check_sub_channel(chat_member: ChatMember) -> bool:
    """Return True if user is in group otherwise False"""
    return chat_member['status'] != 'left'


def get_all_bot_commands(commands: dict) -> str:
    """Return all the bot commands"""
    return ''.join(["\n/" + command for command in commands.values()])
