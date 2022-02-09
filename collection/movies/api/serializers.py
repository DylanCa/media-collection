from rest_framework_json_api import serializers

from collection.movies.models import Collection, Movie


class CollectionSerializer(serializers.ModelSerializer):
    included_serializers = {
        "movies": "collection.movies.api.serializers.MovieSerializer",
    }

    class Meta:
        model = Collection
        fields = (
            "id",
            "name",
            "cover_image",
            "movies",
        )

    def validate(self, attrs):

        return attrs


class MovieSerializer(serializers.ModelSerializer):
    collection = CollectionSerializer(read_only=True)

    class Meta:
        model = Movie
        fields = (
            "id",
            "title",
            "description",
            "cover_image",
            "collection",
        )

    def validate(self, attrs):
        if "overview" in self.initial_data.keys():
            attrs["description"] = self.initial_data["overview"]

        if "poster_path" in self.initial_data.keys():
            attrs[
                "cover_image"
            ] = f"https://image.tmdb.org/t/p/w500{self.initial_data['poster_path']}"

        if "belongs_to_collection" in self.initial_data.keys():
            collection = {
                "name": self.initial_data["belongs_to_collection"]["name"],
                "cover_image": self.initial_data["belongs_to_collection"][
                    "poster_path"
                ],
            }
            collection, _ = Collection.objects.get_or_create(
                name=collection["name"], cover_image=collection["cover_image"]
            )
            attrs['collection'] = collection
        return attrs
