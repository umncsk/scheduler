from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.parsers import JSONParser

from .scraping import getPageSource, getTime, exportAsDict, makeList, changeData, beRowData
from django.contrib.auth.models import User, Group
from app_scheduler.serializers import UserSerializer, GroupSerializer
from .models import Organization

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

def index(request):
    #indexを読み込んでデフォルトの画面表示
    return render(request, "scheduler/index.html")


def execute(request):
    if request.method == 'POST':
        # ユーザー登録に必要なデータ軍の定義
        student_id = request.POST["student_id"]
        team_id    = request.POST["team_id"]
        pswd       = request.POST["password"]
        team_name  = request.POST["display_name"]
        user_name  = request.POST["username"]

        # ユーザーの講義データを取得
        html      = getPageSource(id, pswd)
        dict_data = exportAsDict(html)
        dict_data = dict_data['Spring']
        pre_class, aft_class = changeData(dict_data)

        # 講義データのバイナリ変換
        pre_class = beRowData(pre_class)
        aft_class = beRowData(aft_class)

        # 書き出しサイズがオーバーフローを起こすため10進数に変換して書き込む
        """
        db_org = Organization(
            share_pre = int(pre_class, 2),
            share_aft = int(aft_class, 2),
        )
        database_p.save()
        """

    return render(request, "scheduler/index.html")


def makeorg(request):
    if request.method == 'POST':
        team_id = request.POST["team_id"] # 任意のteam_id
        db_org = Organization(team_id=team_id)
        db_org.save()

    return render(request, "scheduler/makeorg.html")


def joinorg(request):
    if request.method == 'POST':
        if request.filter(Organization.objects.get("team_id").exists()):
            print("ok")
        team_id = request.POST["org"] # 参加するチームのteam_id
        display_name = request.POST["display_name"] #チーム内での任意の表示名

        db_usr = User(team_id=team_id, display_name=display_name)
        db_usr.save()

    return render(request, "scheduler/join.html")
