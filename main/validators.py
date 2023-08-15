import re

from rest_framework.serializers import ValidationError


class YoutubeValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        value = dict(value).get(self.field)
        youtube_regex = r'(https?://)?(www\.)?(youtube|youtu|youtube-nocookie)\.(com|be)/.+'
        if not re.match(youtube_regex, value):
            raise ValidationError("Видео не с YouTube")

