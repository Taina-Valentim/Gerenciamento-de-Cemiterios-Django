"""cemiterio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import Registrar, home, cadastro_jazigo, cadastro_obito, cadastro_sepultamento, \
atualiza_jazigo, atualiza_obito, atualiza_sepultamento, \
exclui_jazigo, exclui_obito, exclui_sepultamento, \
listagem_jazigos, listagem_obitos, listagem_sepultamentos


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="url_principal"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name="url_registrar"),

    path('cadastro-jazigo/', cadastro_jazigo ,name="url_cadastro_jazigo"),
    path('cadastro-obito/', cadastro_obito ,name="url_cadastro_obito"),
    path('cadastro-sepultamento/', cadastro_sepultamento ,name="url_cadastro_sepultamento"),

    path('listagem-jazigos/', listagem_jazigos ,name="url_listagem_jazigos"),
    path('listagem-obitos/', listagem_obitos ,name="url_listagem_obitos"),
    path('listagem-sepultamentos/', listagem_sepultamentos ,name="url_listagem_sepultamentos"),

    path('atualiza-jazigo/<int:id>/', atualiza_jazigo ,name="url_atualiza_jazigo"),
    path('atualiza-obito/<int:id>/', atualiza_obito ,name="url_atualiza_obito"),
    path('atualiza-sepultamento/<int:id>/', atualiza_sepultamento ,name="url_atualiza_sepultamento"),

    path('exclui-jazigo/<int:id>/', exclui_jazigo ,name="url_exclui_jazigo"),
    path('exclui-obito/<int:id>/', exclui_obito ,name="url_exclui_obito"),
    path('exclui-sepultamento/<int:id>/', exclui_sepultamento ,name="url_exclui_sepultamento"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
