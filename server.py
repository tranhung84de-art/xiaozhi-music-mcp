import os
import requests
from mcp.server.fastmcp import FastMCP

MUSIC_API_URL = os.environ.get(
    "MUSIC_API_URL",
    "https://hungtran.lovestoblog.com/xiaozhi-music/api/search.php"
)

MUSIC_API_KEY = os.environ.get("MUSIC_API_KEY", "1412190628013011")

mcp = FastMCP("Xiaozhi Music")


@mcp.tool()
def search_music(query: str) -> dict:
    """Search Vietnamese music by title, artist, album or genre."""

    if not MUSIC_API_KEY:
        return {
            "success": False,
            "error": "MUSIC_API_KEY is missing"
        }

    try:
        response = requests.get(
            MUSIC_API_URL,
            params={
                "key": MUSIC_API_KEY,
                "q": query
            },
            timeout=15
        )

        response.raise_for_status()

        return response.json()

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def main():
    mcp.run()


if __name__ == "__main__":
    main()
