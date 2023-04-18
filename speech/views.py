from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import time
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .helpers import SpeechTextConverter


# Create your views here.


@csrf_exempt
def upload_speech(request):
    if request.method == "POST":
        recording = request.FILES["recording"]

        path = default_storage.save(
            f"tmp/{time.strftime('%Y%m%d-%H%M%S')}.webm",
            ContentFile(recording.read()),
        )

        tmp_file = os.path.join(settings.MEDIA_ROOT, path)

        converter = SpeechTextConverter()
        bucket_url = converter.upload_to_gcs(tmp_file)

    return JsonResponse(
        {"uri": bucket_url},
    )
