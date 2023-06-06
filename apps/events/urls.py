from django.urls import path
app_name = 'general_parameters'

urlpatterns = [
    path('tipos-de-documentos/', TypesOfDocuments.as_view(), name='types_of_documents_index') 
]