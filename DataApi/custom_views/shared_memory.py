from rest_framework.views import APIView
from rest_framework.response import Response
import multiprocessing.shared_memory
import numpy as np
from django.apps import apps
import psycopg2
from ncarp_lens_app.DataApi.models.datasource import DataSource

class Read_Shared_Memory(APIView):
    def get(self,request,*args,**kwargs):
        try:
            final_result = []
            tag_names = request.query_params.get('tag_name','')
            tag_list = tag_names.split(',')
            shared_memory = multiprocessing.shared_memory.SharedMemory(name='sample')
            arr = np.ndarray([5000], 'f4', shared_memory.buf)
            for tag_name in tag_list:
                try:
                    tag_id = DataSource.objects.get(parametername=tag_name)
                    value = arr[int(tag_id.sharedmemoryid)]
                except Exception as e:
                    return Response(e)                
                final_result.append({
                    'tag_name':tag_name,
                    'tag_value':value,
                })                
            return Response(final_result)
        except Exception as e:
            return Response(e)
    
    def post(self,request,*args,**kwargs):
        try:
            tag_id = request.data.get('tag_id','')
            tag_value = request.data.get('tag_value','')
            shared_memory = multiprocessing.shared_memory.SharedMemory(name='sample')
            arr = np.ndarray([5000], 'f4', shared_memory.buf)
            arr[int(tag_id)] = tag_value
            return Response('Data saved')
        except Exception as e:
            return Response(e)
        