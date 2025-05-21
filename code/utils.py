from googleapiclient.discovery import build


# Inicializa y devuelve el cliente de la API de YouTube
def init_youtube(api_key):
    return build("youtube", "v3", developerKey=api_key)


# Obtiene una lista de videos recientes con el hashtag #MañaneraDelPueblo
def get_mananera_info(youtube, channel_id, max_results=5):
    response = youtube.search().list(
        q="#MañaneraDelPueblo",
        channelId=channel_id,
        part="snippet",
        order="date",
        maxResults=max_results,
        type="video"
    ).execute()

    video_info = []
    for item in response["items"]:
        video_info.append({
            "video_id": item["id"]["videoId"],
            "video_title": item["snippet"]["title"]
        })

    return video_info


# Descarga comentarios de un video dado (hasta max_comments)
def get_comments(youtube, video_id, max_comments=1000):
    comments = []
    next_page_token = None

    while len(comments) < max_comments:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=100,
            pageToken=next_page_token,
            textFormat="plainText"
        )
        response = request.execute()

        for item in response.get("items", []):
            snippet = item["snippet"]["topLevelComment"]["snippet"]
            comments.append({
                "video_id": video_id,
                "comment_id": item["id"],
                "author_id": snippet.get(
                    "authorChannelId", {}
                ).get("value", "NA"),
                "author_name": snippet.get("authorDisplayName", "NA"),
                "comment_text": snippet.get("textDisplay", "NA"),
                "published_at": snippet.get("publishedAt", "NA")
            })

        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments
