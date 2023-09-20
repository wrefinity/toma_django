from django.shortcuts import render, redirect
from django.db.models import Q
from django.views.generic.base import (
    View,
    TemplateView
)
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from .models import Tomatoes
from django.db import IntegrityError


class DiseaseView(View):
    template_name = 'pages/diseases.html'

    def get(self, request):
        # Retrieve all Tomatoes records
        tomatoes = Tomatoes.objects.all()
        # Pass the retrieved records to the template
        context = {'tomatoes': tomatoes}
        return render(request, self.template_name, context)

    def post(self, request):
        try:
            variety = request.POST['variety']
            name = request.POST["name"]
            age = request.POST['age']
            climate = request.POST['location']
            color = request.POST['color']
            spot_size = request.POST['spot_size']
            spot_color = request.POST['spot_color']
            spot_dist = request.POST['spot_dist']
            leaf_texture = request.POST['leaf_texture']
            overall_health = request.POST['overall_health']
            nearby_plant_obs = request.POST['nearby_plant_observations']
            spore_fungal = request.POST['spore_fungal']
            onset_time = request.POST['onset_time']
            recent_pest_activities = request.POST['disease_history']
            disease_history = request.POST['onset_time']
            desc = request.POST['desc']
            # Create a Tomatoes instance
            toma = Tomatoes(
                variety=variety,
                name=name,
                age=age,
                climate=climate,
                color=color,
                spot_size=spot_size,
                spot_color=spot_color,
                spot_dist=spot_dist,
                leaf_texture=leaf_texture,
                overall_health=overall_health,
                nearby_plant_observations=nearby_plant_obs,
                spore_fungal=spore_fungal,
                onset_time=onset_time,
                recent_pest_activities=recent_pest_activities,
                disease_history=disease_history,
                diagnosis=desc
            )
            toma.save()
            return redirect('list-tomatoes')
        except IntegrityError as e:
            print(e)


class SearchMixin:
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        
        if search_query:
            queryset = queryset.filter(
                Q(variety__icontains=search_query) |
                Q(age__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(color__icontains=search_query) |
                Q(spot_color__iexact=search_query) |
                Q(spot_size__iexact=search_query) |
                Q(spot_dist__iexact=search_query) |
                Q(leaf_texture__icontains=search_query) |
                Q(overall_health__iexact=search_query) |
                Q(spore_fungal__iexact=search_query) |
                Q(onset_time__icontains=search_query)
            )      
        return queryset


class TomatoesListView(SearchMixin, ListView):
    model = Tomatoes
    template_name = 'pages/disease_list.html'
    context_object_name = 'tomatoes'
    paginate_by = 100  # Set the number of items per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('q', '')
        return context


class TomatoesDetailView(DetailView):
    model = Tomatoes
    template_name = 'pages/disease_detail.html'
    context_object_name = 'tomato'


class TomatoesDeleteView(DeleteView):
    model = Tomatoes
    template_name = 'tomatoes/tomatoes_confirm_delete.html'
    success_url = reverse_lazy('list-tomatoes')


# class TomatoesSearchView(TemplateView):
#     template_name = 'pages/disease_search.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         # Get the search query from the request
#         search_query = self.request.GET.get('search_query')

#         print(search_query)

#         # Perform the search
#         if search_query:
#             results = Tomatoes.objects.filter(
# variety__icontains=search_query)
#             # if not results:
#             #     results = Tomatoes.objects.all()
#         else:
#             results = Tomatoes.objects.all()

#         context['tomatoes'] = results
#         context['search_query'] = search_query
#         return context
    

class TomatoesSearchView(TemplateView):
    template_name = 'pages/disease_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the input values from the query parameters
        variety = self.request.GET.get('variety', '')
        age = self.request.GET.get('age', '')
        location = self.request.GET.get('location', '')
        color = self.request.GET.get('color', '')
        spot_color = self.request.GET.get('spot_color', '')
        spot_size = self.request.GET.get('spot_size', '')
        spot_dist = self.request.GET.get('spot_dist', '')
        leaf_texture = self.request.GET.get('leaf_texture', '')
        overall_health = self.request.GET.get('overall_health', '')
        spore_fungal = self.request.GET.get('spore_fungal', '')
        onset_time = self.request.GET.get('onset_time', '')

        # Perform the search based on the input values
        results = Tomatoes.objects.all()

        if variety:
            results = results.filter(variety__icontains=variety)
        if age:
            results = results.filter(age=age)
        if location:
            results = results.filter(location__icontains=location)
        if color:
            results = results.filter(color__icontains=color)
        if spot_color:
            results = results.filter(spot_color__iexact=spot_color)
        if spot_size:
            results = results.filter(spot_size__iexact=spot_size)
        if spot_dist:
            results = results.filter(spot_dist__iexact=spot_dist)
        if leaf_texture:
            results = results.filter(leaf_texture__icontains=leaf_texture)
        if overall_health:
            results = results.filter(overall_health__iexact=overall_health)
        if spore_fungal:
            results = results.filter(spore_fungal__iexact=spore_fungal)
        if onset_time:
            results = results.filter(onset_time=onset_time)

        context = {
            'results': results,
        }

        context['tomatoes'] = results
        return context
  

class TomatoesMultiFieldSearchView(TemplateView):
    template_name = 'pages/disease_search.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = None

        # Check if a search query is present in the GET parameters
        search_query = self.request.GET.get('q')

        if search_query:
            print("request data made")
            # Get the input values from the query parameters
            variety = self.request.GET.get('variety', '')
            print(variety)
            age = self.request.GET.get('age', '')
            location = self.request.GET.get('location', '')
            color = self.request.GET.get('color', '')
            spot_color = self.request.GET.get('spot_color', '')
            spot_size = self.request.GET.get('spot_size', '')
            spot_dist = self.request.GET.get('spot_dist', '')
            leaf_texture = self.request.GET.get('leaf_texture', '')
            overall_health = self.request.GET.get('overall_health', '')
            spore_fungal = self.request.GET.get('spore_fungal', '')
            onset_time = self.request.GET.get('onset_time', '')

            # Perform the search based on the input values
            results = Tomatoes.objects.all()

            if variety:
                results = results.filter(variety__icontains=variety)
            if age:
                results = results.filter(age=age)
            if location:
                results = results.filter(climate__icontains=location)
            if color:
                results = results.filter(color__icontains=color)
            if spot_color:
                results = results.filter(spot_color__iexact=spot_color)
            if spot_size:
                results = results.filter(spot_size__iexact=spot_size)
            if spot_dist:
                results = results.filter(spot_dist__iexact=spot_dist)
            if leaf_texture:
                results = results.filter(leaf_texture__icontains=leaf_texture)
            if overall_health:
                results = results.filter(overall_health__iexact=overall_health)
            if spore_fungal:
                results = results.filter(spore_fungal__iexact=spore_fungal)
            if onset_time:
                results = results.filter(onset_time=onset_time)

        context['tomatoes'] = results
        context['search_query'] = search_query

        return context


def tomato_search(request):
    # Get the input values from the query parameters
    variety = request.GET.get('variety', '')
    age = request.GET.get('age', '')
    location = request.GET.get('location', '')
    color = request.GET.get('color', '')
    spot_color = request.GET.get('spot_color', '')
    spot_size = request.GET.get('spot_size', '')
    spot_dist = request.GET.get('spot_dist', '')
    leaf_texture = request.GET.get('leaf_texture', '')
    overall_health = request.GET.get('overall_health', '')
    spore_fungal = request.GET.get('spore_fungal', '')
    onset_time = request.GET.get('onset_time', '')

    # Perform the search based on the input values
    results = Tomatoes.objects.all()

    if variety:
        results = results.filter(variety__icontains=variety)
    if age:
        results = results.filter(age=age)
    if location:
        results = results.filter(location__icontains=location)
    if color:
        results = results.filter(color__icontains=color)
    if spot_color:
        results = results.filter(spot_color__iexact=spot_color)
    if spot_size:
        results = results.filter(spot_size__iexact=spot_size)
    if spot_dist:
        results = results.filter(spot_dist__iexact=spot_dist)
    if leaf_texture:
        results = results.filter(leaf_texture__icontains=leaf_texture)
    if overall_health:
        results = results.filter(overall_health__iexact=overall_health)
    if spore_fungal:
        results = results.filter(spore_fungal__iexact=spore_fungal)
    if onset_time:
        results = results.filter(onset_time=onset_time)

    context = {
        'results': results,
    }

    return render(request, 'tomato_search_results.html', context)
