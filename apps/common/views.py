import json

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response


# Create your views.py here.


class getJson(RetrieveAPIView):
    def get(self, request):
        foydalanuchilar = {'olma'}
        sorovlar = ['']
        umumiy = ['']
        try:
            with open("/home/nodirbek/PycharmProjects/uz_cours/apps/common/result.json", 'r') as file:

                json_data = json.load(file)
                messages = json_data['messages']
                for item in messages:
                    umumiy.append(item)
                    if item['from'] == 'Road24.uz - yordam':
                        if item['text'] != 'Bot was blocked by the user.':

                            sorovlar.append(item)
                            foydalanuchilar.add(item['forwarded_from'])
                print(len(foydalanuchilar))
                print(len(sorovlar))
                print(len(umumiy))
        except Exception as e:
            raise ValidationError(str(e))

        return Response({"result": "success"}, status=status.HTTP_200_OK)
