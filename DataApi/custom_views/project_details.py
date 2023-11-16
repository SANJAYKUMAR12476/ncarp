from rest_framework.views import APIView
from rest_framework.response import Response
from ncarp_lens_app.DataApi.service.project_details import Project_Lists
from rest_framework import status

class Project_List(APIView):
    def get(self,request,*args,**kwargs):
        try:
            data = request.session
            user_id = data['_auth_user_id']
            data = Project_Lists.fetch_list(user_id)
            final_result = data if isinstance(data,list) else None
            return Response(final_result)
        except Exception as e:
            return Response({"message": f"error: {str(e)}"})
    
    def post(self,request,*args,**kwargs):
        try:
            project_data =  request.data
            user_id = project_data.get('user_id','')
            project_name = project_data.get('name','')
            description = project_data.get('description','')
            logo = project_data.get('logo','')
            result = Project_Lists.save_projects(user_id=user_id, name=project_name, description=description, logo=logo) if all([user_id, project_name, description, logo]) else {"message": "Missing data"}
            return Response(result)
        except Exception as e:
            return Response({"message": f"error: {str(e)}"})

