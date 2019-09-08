from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, status

from api.models import Post
from api.serializers import UserInputSerializer
from demo import api_utils


class UserInputView(APIView):
    """
    """
    authentication_classes = (authentication.TokenAuthentication,)
    serializer_class = UserInputSerializer

    def post(self, request, format=None):
        """
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user_input = serializer.save()

        picture = serializer.data.get('picture')
        gender = serializer.data.get('gender')
        angle = serializer.data.get('angle')

        result, stat = api_utils.get_image_response(user_input.image.url, gender, angle, picture)

        if stat == 400:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)

        bust_waist = round(result.get('Chest/Waist'), 2)
        waist_hips = round(result.get('Wasit/Hip'), 2)
        legs_body = round(result.get('Leg/Body'), 2)
        body_waist = round(result.get('Body/ Waist'), 2)
        shoulder_hips = round(result.get('Shoulder/Hip'), 2)
        score = round(result.get('score'), 2)
        ratios = result.get('ratios')

        user_input.bust_waist = bust_waist
        user_input.waist_hips = waist_hips
        user_input.legs_body = legs_body
        user_input.body_waist = body_waist
        user_input.shoulder_hips = shoulder_hips
        user_input.score = score
        user_input.save()

        post = Post.objects.create(user_id=user_input.user_id, input_id=user_input.id)

        result = serializer.data
        result.update(bust_waist=bust_waist)
        result.update(waist_hips=waist_hips)
        result.update(legs_body=legs_body)
        result.update(body_waist=body_waist)
        result.update(shoulder_hips=shoulder_hips)
        result.update(score=score)
        result.update(post_id=post.id)
        result.pop('image', None)
        result.update(ratios=ratios)

        return Response(result, status=status.HTTP_201_CREATED)
