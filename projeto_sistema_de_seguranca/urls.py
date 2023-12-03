
from django.contrib import admin
from django.urls import path
from app_sistema__seguranca import views  # Importe as views do seu aplicativo
from django.conf import settings
from django.conf.urls.static import static
from app_sistema__seguranca.views import reconhecimento, protecao, reconhecimento2, protecao2, sincronizacao, sincronizar

#from app_sistema__seguranca.back_end.detector_faces import sincron
#from app_sistema__seguranca.views import ReconhecimentoFacialView
#from django.urls import path, include

urlpatterns = [
    # Rotas existentes

    #Exemplo de rota para a view de login
    path('', views.login_view, name='login'),
    
    path('index/', views.index, name='index'),
    
     path('cadastros/', views.cadastros, name='cadastros'),
    
    path('bloquear/', views.bloquear, name='bloquear'),
    
    path('sincronizacao/', sincronizacao, name='sincronizacao'),
    
    path('reconhecimento/', reconhecimento, name='reconhecimento'),
    
    path('reconhecimento2/', reconhecimento2, name='reconhecimento2'),
    
    path('protecao/', protecao, name='protecao'),
    
    path('protecao2/', protecao2, name='protecao2'),
    
    
    path('sincronizar/', views.sincronizar, name='sincronizar'),
    
    path('alerta/', views.alerta_view, name='alerta'),
    
    
    #path('contagem/', contar_pessoas, name='index'),
    #path('', views.contar_pessoas, name='index'),
    #path('reconhecimento/', views.reconhecimento, name='reconhecimento'),
    
    #path('myapp/', include('myapp.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
