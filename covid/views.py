# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
# Create your views here.
from rest_framework import viewsets, status
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import detail_route, list_route
from django.shortcuts import get_object_or_404
from covid.models import Covid
from covid.serializers import CovidSerializer
from rest_framework.pagination import PageNumberPagination
from paginations import MyPageNumberPagination

# Create your views here.
class CovidViewSet(viewsets.ModelViewSet):
    queryset = Covid.objects.all()
    serializer_class = CovidSerializer
    # permission_classes = (IsAuthenticated,)
    parser_classes = (JSONParser,)

    # /api/covid/information/
    @list_route(methods=['get'])
    def information(self, request):
        result = {
            'status': 200,
            'msg':'Get Covid information successfully',
            'list': [],
            'total':''
        }
        student_covid_list = Covid.objects.filter(role='1').all()
        major = request.GET.get('major', None)
        infected = request.GET.get('infected', None)
        vaccinated = request.GET.get('vaccinated', None)
        recovered = request.GET.get('recovered', None)
        guid = request.GET.get('guid', None)
        mode = request.GET.get('mode', None)


        if major !=None:
            student_covid_list=student_covid_list.filter(major=major)

        if infected !=None:
            student_covid_list=student_covid_list.filter(infected=infected)

        if vaccinated !=None:
            student_covid_list=student_covid_list.filter(vaccinated=vaccinated)

        if recovered !=None:
            student_covid_list=student_covid_list.filter(recovered=recovered)

        if guid!=None:
            student_covid_list = student_covid_list.filter(guid__contains=guid)

        if mode !=None:
            student_covid_list = student_covid_list.exclude(apply_result=0)

        # For Pagination
        paginator = MyPageNumberPagination()

        pager_roles = paginator.paginate_queryset(student_covid_list,request)
        # result['total']= pager_roles.count
        result['list'] = [{'name': item.name,
                           'guid': item.guid,
                           'major': item.major,
                           'vaccinated': item.vaccinated,
                           'vaccinated_time': item.vaccinated_time,
                           'infected': item.infected,
                           'recovered': item.recovered,
                           'recovered_time': item.recovered_time,
                           'apply_result': item.apply_result,
                           'id': item.id,
                           } for item in pager_roles]
        result['total']=student_covid_list.count()
        return Response(result, status=status.HTTP_200_OK)




    # /api/covid/{pk}/apply/
    @detail_route(methods=['put'])
    def apply(self, request, pk=None):
        result = {
            'status': 0,
            'msg': '',
        }
        #get the student Covid information
        student = get_object_or_404(Covid, pk=pk)

        #preprocess the params form front-end
        infected = request.data.get('infected', None)
        infected = True if infected == '1' else False
        recovered = request.data.get('recovered', None)
        recovered = True if recovered == '1' else False
        recovered_time = request.data.get('recoveredDate', None)
        vaccinated = request.data.get('vaccinated', None)
        vaccinated = True if vaccinated == '1' else False
        vaccinated_time = request.data.get('vaccinatedDate', None)

        if infected == False:   # if student is uninfected, then recovered and recovered_time is null.
            recovered = None
            recovered_time = None

        if infected==True and recovered==False: # if student is unrecovered, then recovered_time is null.
            recovered_time = None

        if vaccinated == False: # if student is unvaccinated, then vaccinated_time is null.
            vaccinated_time = None

        #Modify data to database
        student.infected = infected
        student.recovered = recovered
        student.recovered_time = recovered_time
        student.vaccinated = vaccinated
        student.vaccinated_time = vaccinated_time
        student.apply_result=3  # when student apply, the apply result should be waiting
        student.save()

        #return result information to front
        result['status']=200
        result['msg'] ='Apply successfully!'
        return Response(result, status=status.HTTP_200_OK)



    # /api/covid/{pk}/examine/
    @detail_route(methods=['put'])
    def examine(self, request, pk=None):
        result = {
            'status': 0,
            'msg': '',
        }
        #get the student Covid information
        student = get_object_or_404(Covid, pk=pk)

        #preprocess the params form front-end
        apply_result = request.data.get('result', None)


        #Modify data to database
        student.apply_result=apply_result  # when student apply, the apply result should be waiting
        student.save()
        result['status']=200
        result['msg'] ='Examine successfully!'


        return Response(result, status=status.HTTP_200_OK)



    # /api/covid/{pk}/editProfile/
    @detail_route(methods=['put'])
    def editProfile(self, request, pk=None):
        result = {
            'status': 0,
            'msg': '',
        }
        #get the student Covid information
        student = get_object_or_404(Covid, pk=pk)

        #preprocess the params form front-end
        profile = request.data.get('profile', None)


        #Modify data to database
        student.profile=profile  # modify student's profile
        student.save()
        result['status']=200
        result['msg'] ='Edit Profile successfully!'


        return Response(result, status=status.HTTP_200_OK)



