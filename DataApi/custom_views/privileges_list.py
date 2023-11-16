from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ncarp_lens_app.DataApi.models.privilege_details import Previlege_Details


class Privileges_List(APIView):
    def get(self,request,*args,**kwargs):
        result = []
        previlege_list = Previlege_Details.objects.filter(visibility=True)
        for data in previlege_list:
            result.append({
                'id':data.id,
                'value': data.name,
            })
        return Response(result)

