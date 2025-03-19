# from django.urls import path
# from .views import trainee_list ,add_trainee ,update_trainee ,delete_trainee

# urlpatterns = [
#     path('traineelist/', trainee_list, name='trainee_list'),
#     path('update/<int:trainee_id>/', update_trainee, name='update_trainee'),
#     path('delete/<int:trainee_id>/', delete_trainee, name='delete_trainee'),
#     path('add/', add_trainee, name='add_trainee'),
# ]

from django.urls import path
from .views import TraineeListView, TraineeCreateView,TraineeDetailView, TraineeUpdateView, TraineeDeleteView

urlpatterns = [
    path('traineelist/', TraineeListView.as_view(), name='trainee_list'),  
    path('add/', TraineeCreateView.as_view(), name='add_trainee'),  
    path('trainee/<int:pk>/', TraineeDetailView.as_view(), name='trainee_detail'),
    path('update/<int:pk>/', TraineeUpdateView.as_view(), name='update_trainee'),  
    path('delete/<int:pk>/', TraineeDeleteView.as_view(), name='delete_trainee'), 
]



