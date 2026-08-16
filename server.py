import os
import requests
from mcp.server.fastmcp import FastMCP

MUSIC_API_URL = os.environ.get(
    "MUSIC_API_URL",
    "https://hungtran.lovestoblog.com/xiaozhi-music/api/search.php"
)

mcp = FastMCP("Xiaozhi Music")


@mcp.tool()
def search_music(query: str) -> dict:
    """Search Vietnamese music by title, artist, album or genre."""

    try:
        response = requests.get(
            MUSIC_API_URL,
            params={
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


@mcp.tool()
def get_song(title: str) -> dict:
    """Find a specific song by title."""

    try:
        response = requests.get(
            MUSIC_API_URL,
            params={
                "q": title
            },
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        if not data.get("success"):
            return data

        return data

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


def main():
    mcp.run()


if __name__ == "__main__":
    main()
