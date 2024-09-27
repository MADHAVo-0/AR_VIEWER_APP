# ar_app/views.py
from django.shortcuts import render, redirect
from .models import ARModel
from .forms import UploadARModelForm
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import ARModel  # Adjust the model name as per your app

@require_http_methods(["DELETE"])
def delete_model(request, model_id):
    try:
        model = ARModel.objects.get(id=model_id)  # Replace ARModel with your model class
        model.delete()
        return JsonResponse({"success": True}, status=200)
    except ARModel.DoesNotExist:
        return JsonResponse({"error": "Model not found"}, status=404)


def upload_model(request):
    if request.method == 'POST':
        form = UploadARModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_ar_models')
    else:
        form = UploadARModelForm()
    return render(request, 'ar_app/upload.html', {'form': form})

def view_ar_models(request):
    models = ARModel.objects.all()
    return render(request, 'ar_app/view_ar.html', {'models': models})
