from pydantic import BaseModel

class FavoriteSong(BaseModel):
    song_id: str