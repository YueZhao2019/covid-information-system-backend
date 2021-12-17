# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from users.models import User
from covid.models import Covid
from users.serializers import UserSerializer
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.decorators import detail_route, list_route


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    # /api/users/login/
    @list_route(methods=['post'])
    def login(self, request):
        result = {
            'status': 0,
            'msg': '',
        }
        myUsername = request.data.get('username', None)
        myPassword = request.data.get('password', None)
        myRole = request.data.get('role', None)
        user = User.objects.filter(username=myUsername).first()

        if user == None:
            result['msg'] = 'The username is not exist!'
            result['status'] = -1
        else:
            if myUsername == user.username and check_password(myPassword, user.password):
                if myRole == user.role:
                    result['status'] = 200
                    result['msg'] = 'Login successfully!'
                    covid_info = user.covid_info
                    #return the basic information of the login user
                    userInfo = {
                        'name':covid_info.name,
                        'cid':covid_info.id,
                        'major':covid_info.major,
                        'guid':covid_info.guid,
                        'username':user.username,
                        'role': user.role,
                        'uid':user.id
                    }
                    result['userInfo']=userInfo

                else:
                    result['msg'] = 'Please choose the right user role!'
            else:
                result['msg'] = 'Please input the right username and password '

        return Response(result, status=status.HTTP_200_OK)

    # /api/users/addUser/
    @list_route(methods=['post'])
    def addUser(self, request):
        result = {
            'status': 0,
            'msg': '',
        }
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        password= make_password(password, None, 'pbkdf2_sha256')
        role = request.data.get('role', None)
        name = request.data.get('name', None)
        major = request.data.get('major', None)
        user = User.objects.filter(username=username).first()

        #if username is not exist, then create a new user
        if user == None:
            new_user_covid = Covid.objects.create(name=name, major=major, guid=username, role=role)
            new_user = User.objects.create(username=username, password=password, role=role, covid_info=new_user_covid)

            print(new_user.covid_info)
            print(new_user_covid)

            result['status'] = 200
            result['msg'] = 'Add user successfully!'
        else: #thorw the error that the username already exists
            result['msg'] = 'The username/guid already exists!'
            result['status'] = -1

        return Response(result, status=status.HTTP_200_OK)



