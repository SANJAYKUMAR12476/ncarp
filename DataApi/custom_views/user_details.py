from rest_framework.views import APIView
from rest_framework.response import Response
from ncarp_lens_app.DataApi.service.user_details import Login_User
import logging

logger = logging.getLogger("django")

class Login_Verification(APIView):
    def post(self,request,*args,**kwargs):
        try:
            logger.info("Validating the User Credentials")
            username = request.data.get('username') 
            password = request.data.get('password')
            request.session['username'] = username
            data = Login_User.verification(username,password)
            final_result = data if 'access_token' in data.keys() else 'Invalid credentials. Please check your Username and password'
            return Response(final_result)
        except Exception as e:
            return Response(e)

