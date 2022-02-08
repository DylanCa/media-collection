from rest_framework_json_api import serializers

from collection.shows.models import Episode, Season, Show


class EpisodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episode
        fields = (
            "episode_number",
            "name",
            "description",
            "duration",
        )
        # read_only_fields = ("season",)

    def validate(self, attrs):
        if not self.instance:
            attrs["season_id"] = self.context.get("view").kwargs["season_pk"]
        return attrs


class SeasonSerializer(serializers.ModelSerializer):
    episodes = EpisodeSerializer(many=True)

    class Meta:
        model = Season
        fields = (
            "season_number",
            "episodes",
        )
        read_only_fields = ("episodes",)

    def validate(self, attrs):
        if not self.instance:
            attrs["show_id"] = self.context.get("view").kwargs["show_pk"]
        return attrs


class ShowSerializer(serializers.ModelSerializer):
    seasons = SeasonSerializer(many=True)

    class Meta:
        model = Show
        fields = (
            "name",
            "seasons",
        )
        read_only_fields = ("seasons",)
