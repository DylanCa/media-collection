from rest_framework_json_api import serializers

from collection.shows.models import Episode, Season, Show


class EpisodeSerializer(serializers.ModelSerializer):
    included_serializers = {
        "season": "collection.shows.api.serializers.SeasonSerializer",
    }

    class Meta:
        model = Episode
        fields = (
            "id",
            "episode_number",
            "name",
            "description",
            "cover_image",
            "season",
        )
        read_only_fields = ("season",)

    def validate(self, attrs):
        if not self.instance:
            season = Season.objects.get(
            season_number=self.context.get("view").kwargs["season_pk"], show=self.context.get("view").kwargs["show_pk"]
        )
            attrs["season_id"] = season.id
        if "overview" in self.initial_data.keys():
            attrs["description"] = self.initial_data["overview"]
        
        if "still_path" in self.initial_data.keys():
            attrs[
                "cover_image"
            ] = f"https://image.tmdb.org/t/p/w500{self.initial_data['still_path']}"
        elif "cover" in self.initial_data.keys():
            attrs[
                "cover_image"
            ] = f"https://image.tmdb.org/t/p/w500{self.initial_data['cover']}"
        return attrs


class SeasonSerializer(serializers.ModelSerializer):
    included_serializers = {
        "show": "collection.shows.api.serializers.ShowSerializer",
    }

    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = (
            "id",
            "season_number",
            "name",
            "description",
            "cover_image",
            "show",
            "episodes",
        )
        read_only_fields = ("show",)

    def validate(self, attrs):
        if not self.instance:
            attrs["show_id"] = self.context.get("view").kwargs["show_pk"]

        if "overview" in self.initial_data.keys():
            attrs["description"] = self.initial_data["overview"]
        
        if "poster_path" in self.initial_data.keys():
            attrs[
                "cover_image"
            ] = f"https://image.tmdb.org/t/p/w500{self.initial_data['poster_path']}"
        return attrs


class ShowSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = (
            "id",
            "name",
            "description",
            "cover_image",
            "seasons",
        )

    def validate(self, attrs):
        if "overview" in self.initial_data.keys():
            attrs["description"] = self.initial_data["overview"]
        
        if "poster_path" in self.initial_data.keys():
            attrs[
                "cover_image"
            ] = f"https://image.tmdb.org/t/p/w500{self.initial_data['poster_path']}"
        return attrs
