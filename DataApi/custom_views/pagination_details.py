
from rest_framework.views import APIView
from rest_framework.response import Response
from ncarp_lens_app.DataApi.service.pagination_details import Page_Lists
from rest_framework import status
from ncarp_lens_app.DataApi.models.user_details import Login_User_Details
 
class Page_List(APIView):
    def get(self,request,*args,**kwargs):
        try:
            data = request.session
            # user_id = data['_auth_user_id']
            user_id = 4
            project_name = request.query_params.get('project','')
            page_name = request.query_params.get('page','')
            data = Page_Lists.fetch_list(user_id,project_name,page_name)
            return Response(data)
        except Exception as e:
            return Response({"message": f"error: {str(e)}"})
   
    def post(self,request,*args,**kwargs):
        try:
            page_data =  request.data
            # user_id = request.session['_auth_user_id']
            user_id = 4
            page_name = page_data.get('name','')
            description = page_data.get('description','')
            access_to = page_data.get('access_to','')
            background = page_data.get('background','')
            layout = page_data.get('layout','')
 
            if not page_name or not description or not access_to or not background or not layout:
                return Response('Missing Data')
            page_result = Page_Lists.save_pages(user_id=user_id,
                                     name=page_name,
                                     description=description,
                                     access_to=access_to,
                                     background=background,
                                     layout= layout
                                     )
            return Response(page_result)
       
        except Exception as e:
            return Response({"message": f"error: {str(e)}"})
   
    def put(self, request, *args, **kwargs):
        try:
           
            page_data = request.data
           
            print(page_data['userInfo']['username'])
           
            user_name = page_data['userInfo']['username']
            user = Login_User_Details.objects.get(user_name = user_name)            
            page_name = page_data['userInfo']['pageName']
            project_name = page_data['userInfo']['projectName']
           
            page_data.pop('userInfo')
           
            print(page_data)
            if page_name and project_name and user.id:
                result = Page_Lists.update_pages(user_id=user.id, page_name=page_name, project_name=project_name, json_data=page_data)
            else:
                result = {"message": "Missing data"}
            return Response(result)
        except Exception as e:
            print('--*******888--->',e)
            return Response({"message": f"error: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)
       