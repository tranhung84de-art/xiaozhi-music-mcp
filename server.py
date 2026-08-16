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
    """
    Search Vietnamese music by song title, artist, album or genre.
    """

    try:
        response = requests.get(
            MUSIC_API_URL,
            params={"q": query},
            timeout=15
        )

        response.raise_for_status()
        return response.json()

    except requests.RequestException as e:
        return {
            "success": False,
            "error": f"Music API error: {str(e)}"
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
def get_song(title: str) -> dict:
    """
    Search for a specific Vietnamese song by title.
    """

    return search_music(title)


def main():
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
