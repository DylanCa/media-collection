from rest_framework_json_api import serializers

from collection.shows.models import Episode, Season, Show


class EpisodeSerializer(serializers.ModelSerializer):
    included_serializers = {
        'season': 'collection.shows.api.serializers.SeasonSerializer',
    }

    class Meta:
        model = Episode
        fields = (
            "episode_number",
            "name",
            "description",
            "duration",
            "season",
        )
        read_only_fields = ("season",)

    def validate(self, attrs):
        if not self.instance:
            attrs["season_id"] = self.context.get("view").kwargs["season_pk"]
        return attrs


class SeasonSerializer(serializers.ModelSerializer):
    included_serializers = {
        'show': 'collection.shows.api.serializers.ShowSerializer',
    }

    episodes = EpisodeSerializer(many=True, read_only=True)

    class Meta:
        model = Season
        fields = (
            "season_number",
            "episodes",
            "show"
        )
        read_only_fields = ("show",)

    def validate(self, attrs):
        if not self.instance:
            attrs["show_id"] = self.context.get("view").kwargs["show_pk"]
        return attrs


class ShowSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True, read_only=True)

    class Meta:
        model = Show
        fields = (
            "name",
            "seasons",
        )
