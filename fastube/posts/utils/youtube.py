def get_youtube_original_url(video_id):
    return "https://www.youtube.com/watch?v={video_id}".format(
        video_id=video_id,
    )


def get_youtube_embed_url(video_id):
    return "https://www.youtube.com/embed/{video_id}".format(
        video_id=video_id,
    )
