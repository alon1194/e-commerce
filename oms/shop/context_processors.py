from .models import Custumer

def profile_data(request):

    if request.user.is_authenticated:

        profile, created = Custumer.objects.get_or_create(
            user=request.user
        )

        return {
            "profile": profile
        }

    return {}