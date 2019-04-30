from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class MenPageView(TemplateView):
    template_name = 'Men.html'


class WomenPageView(TemplateView):
    template_name = 'WoMen.html'


class AfricaPageView(TemplateView):
    template_name = 'Africa.html'


class EuropePageView(TemplateView):
    template_name = 'Europe.html'


class NorthAmericaPageView(TemplateView):
    template_name = 'North America.html'


class OceaniaPageView(TemplateView):
    template_name = 'Oceania.html'


class SouthAmericaPageView(TemplateView):
    template_name = 'South America.html'


class AsiaPageView(TemplateView):
    template_name = 'Asia.html'


class WorldCupPageView(TemplateView):
    template_name = 'World Cup.html'


class AfricacupofNationPageView(TemplateView):
    template_name = 'Africa cup of Nation.html'


class AsianCupPageView(TemplateView):
    template_name = 'Asian Cup.html'


class EuropeanFootballChampionshipPageView(TemplateView):
    template_name = 'European Football Championship.html'


class CONCACAFGoldCupPageView(TemplateView):
    template_name = 'CONCACAF Gold Cup.html'


class OFCNationsCupPageView(TemplateView):
    template_name = 'OFC Nations Cup.html'


class CopaAmericaPageView(TemplateView):
    template_name = 'Copa America.html'