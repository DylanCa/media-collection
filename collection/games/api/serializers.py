from rest_framework_json_api import serializers

from collection.games.models import Game, Genre, Platform


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"


class GameSerializer(serializers.ModelSerializer):
    platforms = PlatformSerializer(many=True, read_only=True)
    genres = GenreSerializer(many=True, read_only=True)

    class Meta:
        model = Game
        fields = (
            "id",
            "title",
            "description",
            "platforms",
            "genres",
            "cover_image",
        )

    def validate(self, attrs):
        if "summary" in self.initial_data.keys():
            attrs["description"] = self.initial_data["summary"]
        if "cover" in self.initial_data.keys():
            attrs["cover_image"] = self.initial_data["cover"]["url"][2:]
        if "platforms" in self.initial_data.keys():
            attrs["platforms"] = []
            for platform in self.initial_data["platforms"]:
                p, _ = Platform.objects.get_or_create(name=platform["name"])
                attrs["platforms"] += [p]
        if "genres" in self.initial_data.keys():
            attrs["genres"] = []
            for genre in self.initial_data["genres"]:
                g, _ = Genre.objects.get_or_create(name=genre["name"])
                attrs["genres"] += [g]
        return attrs