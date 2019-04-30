from django.urls import path
from .views import HomePageView, MenPageView, WomenPageView, AfricaPageView, EuropePageView, NorthAmericaPageView, \
    OceaniaPageView, SouthAmericaPageView, AsiaPageView, WorldCupPageView, AfricacupofNationPageView,  AsianCupPageView,\
    EuropeanFootballChampionshipPageView, CONCACAFGoldCupPageView, OFCNationsCupPageView, CopaAmericaPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('men', MenPageView.as_view(), name='men'),
    path('women', WomenPageView.as_view(), name='women'),
    path('Africa', AfricaPageView.as_view(), name='Africa'),
    path('Europe', EuropePageView.as_view(), name='Europe'),
    path('North America', NorthAmericaPageView.as_view(), name='North America'),
    path('Oceania', OceaniaPageView.as_view(), name='Oceania'),
    path('South America', SouthAmericaPageView.as_view(), name='South America'),
    path('Asia', AsiaPageView.as_view(), name='Asia'),
    path('World Cup', WorldCupPageView.as_view(), name='World Cup'),
    path('Africa cup of Nation', AfricacupofNationPageView.as_view(), name='Africa cup of Nation'),
    path('Asian Cup', AsianCupPageView.as_view(), name='Asian Cup'),
    path('European Football Championship', EuropeanFootballChampionshipPageView.as_view(), name='European Football Championship'),
    path('CONCACAF Gold Cup', CONCACAFGoldCupPageView.as_view(), name='CONCACAF Gold Cup'),
    path('OFC Nations Cup', OFCNationsCupPageView.as_view(), name='OFC Nations Cup'),
    path('Copa America', CopaAmericaPageView.as_view(), name='Copa America'),

]