from services.recommendation_service import (
    RecommendationService
)


def test_recommendation():

    phones = (

        RecommendationService.recommend(

            budget=30000,

            purpose="gaming"

        )

    )

    assert isinstance(
        phones,
        list
    )