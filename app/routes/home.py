
from app.common.database.repositories import plays, messages

from flask import Blueprint, redirect
from typing import Optional

import utils

router = Blueprint("home", __name__)

@router.get("/")
def root():
    return utils.render_template(
        "home.html",
        css="home.css",
        title="Welcome - Titanic",
        description="Titanic » A private server for osu! that lets you experience the early days of the game.",
        news=[
            {
                "date": "24.12.2023",
                "link": "#",
                "title": "Accounts Update",
                "author": "Lekuru",
                "text": "Merry Christmas, everyone! After a long period of development, the accounts update is finally here! "
                        "We hope to speed up development in the future. Enjoy customizing your user profile!"
            },
            {
                "date": "08.10.2023",
                "link": "#",
                "title": "Welcome!",
                "author": "Lekuru",
                "text": "This website is currently in development, so enjoy this placeholder message!"
            }
        ],
        beatmapsets=[(p.count, p.beatmapset) for p in plays.fetch_most_played()],
        messages=messages.fetch_recent()
    )

# Redirect index.* to root
@router.get('/index')
@router.get('/index<extension>')
def index(extension: Optional[str] = None):
    return redirect('/')
