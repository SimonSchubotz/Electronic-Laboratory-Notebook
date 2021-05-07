from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from Exp_Main.models import ExpBase, ExpPath
from Exp_Main.models import OCA as OCA_Main
from Exp_Main.models import SEL as SEL_Main
from Exp_Main.models import SFG as SFG_Main
from Analysis.models import Comparison as Comparison_Main
from Exp_Main.models import Group
from Analysis.models import OszAnalysisJoin as OszAnalysis_Main
from Lab_Dash.dash_plot_SEL import Gen_dash
from Lab_Dash.dash_plot_Generic import Gen_dash as Gen_dash_Generic
from Lab_Dash.dash_plot_SFG import Gen_dash as Gen_dash_SFG
from Lab_Dash.dash_plot_OszAnalysis import Gen_dash as Gen_dash_OszAnalysis
from Lab_Dash.dash_plot_comparison import Gen_dash as Gen_dash_Comparisons
from Lab_Dash.dash_plot_SFG_kin_3D import Gen_dash as Gen_dash_SFG_kin_3D
from Lab_Dash.dash_plot_SFG_kin_drive import Gen_dash as Gen_dash_SFG_kin_drive
from Lab_Dash.dash_plot_SFG_abrastern import Gen_dash as Gen_dash_SFG_abrastern
from Lab_Dash.dash_plot_SFG_cycle import Gen_dash as Gen_dash_SFG_cycle
from django.apps import apps
from Lab_Dash.dash_plot_SEL_compare import Gen_dash as Gen_dash_compare
from .forms import OCAForm, get_Form, From_Choice
from .models import OCA
from bootstrap_modal_forms.generic import (BSModalUpdateView)
# Create your views here.

def Comparison(request, pk):
    entry = Comparison_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    all_dash_entry = list(entry.Dash.Entry.all().values_list('Name', flat=True))
    all_dash_entry.insert(0, 'All')
    label_to_number = {label: i for i, label in enumerate(all_dash_entry, 0)}
    choices = [(label_to_number[label], label) for label in all_dash_entry]
    form_class = From_Choice(choices)
    context['form'] = form_class
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'SEL'
    Name_dash_app = 'dash_SEL_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_Comparisons(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}}
    if request.method == 'POST' and 'Select_edit' in request.POST:
        selected = all_dash_entry[int(request.POST['field'])]
        if selected == 'All':
            return redirect('/Dash/update_model/Comparison/' + str(entry.Dash.id))
        else:
            return redirect('/Dash/update_model/ComparisonEntry/' + str(entry.Dash.Entry.get(Name = selected).id))

    return render(request, "plot_comparison.html", context)

def OszAnalysis(request, pk):
    entry = OszAnalysis_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    all_dash_entry = list(entry.Dash.Entry.all().values_list('Name', flat=True))
    all_dash_entry.insert(0, 'All')
    label_to_number = {label: i for i, label in enumerate(all_dash_entry, 0)}
    choices = [(label_to_number[label], label) for label in all_dash_entry]
    form_class = From_Choice(choices)
    context['form'] = form_class
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'SEL'
    Name_dash_app = 'dash_SEL_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_OszAnalysis(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}}
    if request.method == 'POST' and 'Select_edit' in request.POST:
        selected = all_dash_entry[int(request.POST['field'])]
        if selected == 'All':
            return redirect('/Dash/update_model/OszAnalysis/' + str(entry.Dash.id))
        else:
            return redirect('/Dash/update_model/OszAnalysisEntry/' + str(entry.Dash.Entry.get(Name = selected).id))

    return render(request, "plot_OszAnalysis.html", context)

def update_model(request, ModelName, pk):
    formset = get_Form(ModelName)
    model = apps.get_model('Lab_Dash', ModelName)
    entry = model.objects.get(id = pk)
    formset = formset(request.POST or None, instance=entry)
    if formset.is_valid():
        formset.save()
        #return redirect('next_view')
    return render(request, 'update_Dash_model.html', {'formset': formset})

def GRP_graph(request, model, pk):
    if model == 'SFG':
        render = GRP_SFG(request, pk)
        return render

def GRP_SFG(request, pk):
    entry = Group.objects.get(id = pk)
    if entry.Dash.Typ == 'SFG_kin_drive':
        render = GRP_SFG_kin_drive(request, pk)
        return render
    if entry.Dash.Typ == 'SFG_kin_3D':
        render = Gen_SFG_kin_3D(request, pk)
        return render
    if entry.Dash.Typ == 'SFG_abrastern':
        render = Gen_SFG_abrastern(request, pk)
        return render
    if entry.Dash.Typ == 'SFG_cycle':
        render = Gen_SFG_cycle(request, pk)
        return render

def Gen_SFG_cycle(request, pk):
    entry = Group.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    curr_model = apps.get_model('Lab_Dash', entry.Dash.Typ)
    if curr_model.objects.filter(Group_id = entry.Dash.pk).count() == 0:
        entry_dash = entry.Dash
        This_curr_model = curr_model(Name = entry.Dash.Typ + '_' + entry.Dash.Name[5:], Group = entry_dash)
        This_curr_model.save()
    else:
        This_curr_model = curr_model.objects.get(Group_id = entry.Dash.pk)
    context['pk_dash'] = This_curr_model.pk # '-' is theseperator defined in url
    context['model_name'] = entry.Dash.Typ
    Name_dash_app = entry.Dash.Typ + str(entry.pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_SFG_cycle(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    path = 'Private/Saved_plots/GRP/SFG/' + pk +'/'
    context['dash_context'] = {'target_id': {'value': entry.pk}, 'path': {'value': path}}
    return render(request, "plot.html", context)

def Gen_SFG_abrastern(request, pk):
    entry = Group.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    curr_model = apps.get_model('Lab_Dash', entry.Dash.Typ)
    if curr_model.objects.filter(Group_id = entry.Dash.pk).count() == 0:
        entry_dash = entry.Dash
        This_curr_model = curr_model(Name = entry.Dash.Typ + '_' + entry.Dash.Name[5:], Group = entry_dash)
        This_curr_model.save()
    else:
        This_curr_model = curr_model.objects.get(Group_id = entry.Dash.pk)
    context['pk_dash'] = This_curr_model.pk # '-' is theseperator defined in url
    context['model_name'] = entry.Dash.Typ
    Name_dash_app = entry.Dash.Typ + str(entry.pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_SFG_abrastern(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    path = 'Private/Saved_plots/GRP/SFG/' + pk +'/'
    context['dash_context'] = {'target_id': {'value': entry.pk}, 'path': {'value': path}}
    return render(request, "plot.html", context)

def Gen_SFG_kin_3D(request, pk):
    entry = Group.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    curr_model = apps.get_model('Lab_Dash', entry.Dash.Typ)
    if curr_model.objects.filter(Group_id = entry.Dash.pk).count() == 0:
        entry_dash = entry.Dash
        This_curr_model = curr_model(Name = entry.Dash.Typ + '_' + entry.Dash.Name[5:], Group = entry_dash)
        This_curr_model.save()
    else:
        This_curr_model = curr_model.objects.get(Group_id = entry.Dash.pk)
    context['pk_dash'] = This_curr_model.pk # '-' is theseperator defined in url
    context['model_name'] = entry.Dash.Typ
    Name_dash_app = entry.Dash.Typ + str(entry.pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_SFG_kin_drive(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    path = 'Private/Saved_plots/GRP/SFG/' + pk +'/'
    context['dash_context'] = {'target_id': {'value': entry.pk}, 'path': {'value': path}}
    return render(request, "plot.html", context)

def GRP_SFG_kin_drive(request, pk):
    entry = Group.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    curr_model = apps.get_model('Lab_Dash', entry.Dash.Typ)
    if curr_model.objects.filter(Group_id = entry.Dash.pk).count() == 0:
        entry_dash = entry.Dash
        This_curr_model = curr_model(Name = entry.Dash.Typ + '_' + entry.Dash.Name[5:], Group = entry_dash)
        This_curr_model.save()
    else:
        This_curr_model = curr_model.objects.get(Group_id = entry.Dash.pk)
    context['pk_dash'] = This_curr_model.pk # '-' is theseperator defined in url
    context['model_name'] = entry.Dash.Typ
    Name_dash_app = entry.Dash.Typ + str(entry.pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_SFG_kin_drive(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    path = 'Private/Saved_plots/GRP/SFG/' + pk +'/'
    context['dash_context'] = {'target_id': {'value': entry.pk}, 'path': {'value': path}}
    return render(request, "plot.html", context)

def OCA_graph(request, pk):
    entry = OCA_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'OCA'
    context['dash_context'] = {'target_id': {'value': pk}}
    context['Experiment_Name'] = entry.Name
    return render(request, "plot_OCA.html", context)

def Generic(request, ModelName, pk):
    try:
        model = apps.get_model('Exp_Main', ModelName)
    except:
        model = apps.get_model('Exp_Sub', ModelName)
    entry = model.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['model_name'] = ModelName
    Name_dash_app = 'dash_' + ModelName + '_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_Generic(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}, 'ModelName': {'value': ModelName}}
    return render(request, "plot_Generic.html", context)

def SFG_graph(request, pk):
    entry = SFG_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'SFG'
    Name_dash_app = 'dash_SFG_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_SFG(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}}
    return render(request, "plot_SEL.html", context)

def SEL_graph(request, pk):
    entry = SEL_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'SEL'
    Name_dash_app = 'dash_SEL_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}}
    return render(request, "plot_SEL.html", context)

def SEL_compare_graph(request, pk):
    entry = SEL_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['pk_dash'] = entry.Dash.pk # '-' is theseperator defined in url
    context['model_name'] = 'SEL'
    Name_dash_app = 'dash_SEL_compare_' + str(pk)
    context['Name_dash_app'] = Name_dash_app
    Gen_dash_compare(Name_dash_app)#Creates a new app for every pk so the data will not corrupt
    context['dash_context'] = {'target_id': {'value': pk}}
    return render(request, "plot_SEL.html", context)

def MFL_graph(request, pk):
    entry = OCA_Main.objects.get(id = pk)
    context = {'stuff': 'somestuff'}
    context['dash_prop'] = entry.Dash.pk
    context['dash_context'] = {'target_id': {'value': pk}}
    return render(request, "plot.html", context)

def Success_return(request):
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))#redirects to previous url

class Update_dash(BSModalUpdateView):
    model = OCA
    def get_queryset(self, **kwargs):
        pk = self.kwargs['pk']
        model_name = self.kwargs['model']
        curr_model = apps.get_model('Lab_Dash', model_name)
        self.curr_entry = curr_model.objects.get(pk = pk)
        queryset = curr_model.objects.all()
        return queryset
    template_name = 'Modal/update_entry.html'
    form_class = OCAForm
    def get_form_class(self, **kwargs):
        model_name = self.kwargs['model']
        formset_class = get_Form(model_name)
        return formset_class
    success_message = 'Success: Dash was updated.'
    success_url = reverse_lazy('Success_return')