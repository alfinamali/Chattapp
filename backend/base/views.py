from django.shortcuts import render
from django.http import JsonResponse
import random
import time
from agora_token_builder import RtcTokenBuilder
from .models import RoomMember
import json
from django.views.decorators.csrf import csrf_exempt
import logging


# Create your views here.


def lobby(request):
    return render(request, "base/lobby.html")


def room(request, room_name):
    return render(request, "base/room.html", {"room_name": room_name})


def getToken(request):
    appId = "1403921aacde46bfa0003f241b50d6cf"
    appCertificate = "f76386de85b94087b86b7acbaf183269"
    channelName = request.GET.get("channel")
    uid = random.randint(1, 230)
    expirationTimeInSeconds = 3600
    currentTimeStamp = int(time.time())
    privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
    role = 1

    token = RtcTokenBuilder.buildTokenWithUid(
        appId, appCertificate, channelName, uid, role, privilegeExpiredTs
    )

    return JsonResponse({"token": token, "uid": uid}, safe=False)


@csrf_exempt
def createMember(request):
    data = json.loads(request.body)
    member, created = RoomMember.objects.get_or_create(
        name=data["name"], uid=data["UID"], room_name=data["room_name"]
    )

    return JsonResponse({"name": data["name"]}, safe=False)


def getMember(request):
    uid = request.GET.get("UID")
    room_name = request.GET.get("room_name")

    member = RoomMember.objects.get(
        uid=uid,
        room_name=room_name,
    )
    name = member.name
    return JsonResponse({"name": member.name}, safe=False)


logger = logging.getLogger(__name__)


@csrf_exempt
def deleteMember(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            logger.debug("Data received for deleteMember: %s", data)

            try:
                member = RoomMember.objects.get(
                    name=data["name"], uid=data["UID"], room_name=data["room_name"]
                )
                member.delete()
                logger.debug("Member deleted: %s", data)
                return JsonResponse({"message": "Member deleted"}, safe=False)
            except RoomMember.DoesNotExist:
                logger.error("Member does not exist: %s", data)
                return JsonResponse(
                    {"error": "Member does not exist"}, status=404, safe=False
                )

        except json.JSONDecodeError:
            logger.error("Invalid JSON received")
            return JsonResponse({"error": "Invalid JSON"}, status=400, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=405, safe=False)
