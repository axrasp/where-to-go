from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from places.models import Place


def get_place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    img_urls = [img.image.url for img in place.imgs.all()]
    place = {
        "title": place.title,
        "imgs": img_urls,
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lat": place.lat,
            "lng": place.lng
        },
    }
    return JsonResponse(
        place, json_dumps_params={"indent": 2, "ensure_ascii": False}
    )


def index(request):
    features = []
    places = Place.objects.all()
    for place in places:
        details_url = reverse("place", args=(place.id, ))
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": details_url
            }
        }
        features.append(feature)

    map_places = {
        "map_places": {
            "type": "FeatureCollection",
            "features": features
        }
    }

    return render(request, "index.html", context=map_places)
