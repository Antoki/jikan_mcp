import pandas as pd
import requests
import json
from fastmcp import FastMCP


mcp = FastMCP("jikan_mcp_server")

BASE_API_URL = "https://api.jikan.moe/v4"


### ANIME ENDPOINTS ###
@mcp.tool()
def save_data_to_csv(data: dict, filename: str) -> dict:
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    return {"message": "Data saved to CSV successfully"}


@mcp.tool()
def get_full_anime_by_id(id: int) -> dict:
    """Get full anime data by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/full")
    return response.json()["data"]


@mcp.tool()
def get_anime_by_id(id: int) -> dict:
    """Get anime databy id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}")
    return response.json()["data"]


@mcp.tool()
def get_anime_characters(id: int) -> dict:
    """Get anime characters by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/characters")
    return response.json()["data"]


@mcp.tool()
def get_anime_staff(id: int) -> dict:
    """Get anime staff by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/staff")
    return response.json()["data"]


@mcp.tool()
def get_anime_episodes(id: int) -> dict:
    """Get anime episodes by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/episodes")
    return response.json()["data"]


@mcp.tool()
def get_anime_episode_by_id(id: int, episode: int) -> dict:
    """Get anime episodes by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/episodes/{episode}")
    return response.json()["data"]


@mcp.tool()
def get_anime_news(id: int) -> dict:
    """Get anime news by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/news")
    return response.json()["data"]


@mcp.tool()
def get_anime_forum(id: int) -> dict:
    """Get anime forum by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/forum")
    return response.json()["data"]


@mcp.tool()
def get_anime_videos(id: int) -> dict:
    """Get anime videos by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/videos")
    return response.json()["data"]


@mcp.tool()
def get_anime_video_episodes(id: int) -> dict:
    """Get anime episode videos related to the entry"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/videos/episodes")
    return response.json()["data"]


@mcp.tool()
def get_anime_pictures(id: int) -> dict:
    """Get anime pictures by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/pictures")
    return response.json()["data"]


@mcp.tool()
def get_anime_stats(id: int) -> dict:
    """Get anime stats by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/statistics")
    return response.json()["data"]


@mcp.tool()
def get_anime_more_info(id: int) -> dict:
    """Get anime more info by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/moreinfo")
    return response.json()["data"]


@mcp.tool()
def get_anime_recommendations(id: int) -> dict:
    """Get anime recommendations by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/recommendations")
    return response.json()["data"]


@mcp.tool()
def get_anime_user_updates(id: int) -> dict:
    """Get anime user updates by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/userupdates")
    return response.json()["data"]


@mcp.tool()
def get_anime_user_reviews(id: int) -> dict:
    """Get anime user reviews by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/reviews")
    return response.json()["data"]


@mcp.tool()
def get_anime_relations(id: int) -> dict:
    """Get anime relations by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/relations")
    return response.json()["data"]


@mcp.tool()
def get_anime_themes(id: int) -> dict:
    """Get anime themes by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/themes")
    return response.json()["data"]


@mcp.tool()
def get_anime_external(id: int) -> dict:
    """Get anime external by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/external")
    return response.json()["data"]


@mcp.tool()
def get_anime_streaming(id: int) -> dict:
    """Get anime streaming by id"""
    response = requests.get(f"{BASE_API_URL}/anime/{id}/streaming")
    return response.json()["data"]


### SEASONAL ANIME ENDPOINTS ###

@mcp.tool()
def get_season_now() -> dict:
    """Get the current season's anime list"""
    response = requests.get(f"{BASE_API_URL}/seasons/now")
    return response.json()["data"]


@mcp.tool()
def get_season_anime(year: int, season: str) -> dict:
    """Get the anime list for a specific season"""
    response = requests.get(f"{BASE_API_URL}/seasons/{year}/{season}")
    return response.json()["data"]


@mcp.tool()
def get_seasons_list() -> dict:
    """Get the list of all seasons"""
    response = requests.get(f"{BASE_API_URL}/seasons")
    return response.json()["data"]


@mcp.tool()
def get_season_upcoming() -> dict:
    """Get the list of all upcoming seasons"""
    response = requests.get(f"{BASE_API_URL}/seasons/upcoming")
    return response.json()["data"]


if __name__ == "__main__":
    mcp.run()
