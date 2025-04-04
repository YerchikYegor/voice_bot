from datetime import timezone
from email.message import MIMEPart
from sched import scheduler

from aiogram import Bot, Dispatcher, Router
from config.token import TOKEN
import sqlite3

from apscheduler.schedulers.asyncio import AsyncIOScheduler



router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(TOKEN)
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

FORBIDDEN_WORDS = [
    'спам',
    'реклама',
    'взлом',
]

user_violations = {}
MAX_VIOLATIONS = 3
MUTE_DURATION = 10