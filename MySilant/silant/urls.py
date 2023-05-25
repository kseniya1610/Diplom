from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('index', Index.as_view()),

    path('info', Info.as_view(), name='info'),
    path('info/<int:pk>', InfoItem.as_view()),
    path('info/<int:pk>/edit', EditMachine.as_view()),
    path('info/<int:pk>/delete', DeleteMachine.as_view()),
    path('create_machine', CreateMachine.as_view(), name='create_machine'),

    path('maintenance', MaintenanceList.as_view(), name='maintenance'),
    path('maintenance/<int:pk>', MaintenanceItem.as_view()),
    path('maintenance/<int:pk>/edit', MaintenanceEdit.as_view()),
    path('maintenance/<int:pk>/delete', MaintenanceDelete.as_view()),
    path('create_maintenance', CreateMaintenances.as_view(), name='create_maintenance'),

    path('reclamations', ReclamationsList.as_view(), name='reclamations'),
    path('reclamations/<int:pk>', ReclamationsItem.as_view()),
    path('reclamations/<int:pk>/edit', ReclamationsEdit.as_view()),
    path('reclamations/<int:pk>/delete', ReclamationsDelete.as_view()),
    path('create_reclamations', CreateReclamations.as_view(), name='create_reclamations'),

    path('reference_book/', reference_book, name='reference_book'),
    path('reference_book/<int:pk>/', ReferenceBookList.as_view()),
    path('reference_book/1/create/', TechniqueModelCreate.as_view()),
    path('reference_book/1/<int:pk>/edit/', TechniqueModelEdit.as_view()),
    path('reference_book/2/create/', EngineModelCreate.as_view()),
    path('reference_book/2/<int:pk>/edit/', EngineModelEdit.as_view()),
    path('reference_book/3/create/', TransmissionModelCreate.as_view()),
    path('reference_book/3/<int:pk>/edit/', TransmissionModelEdit.as_view()),
    path('reference_book/4/create/', DriveAxleModelCreate.as_view()),
    path('reference_book/4/<int:pk>/edit/', DriveAxleModelEdit.as_view()),
    path('reference_book/5/create/', SteerableAxleModelCreate.as_view()),
    path('reference_book/5/<int:pk>/edit/', SteerableAxleModelEdit.as_view()),
    path('reference_book/6/create/', ServiceCompanyCreate.as_view()),
    path('reference_book/6/<int:pk>/edit/', ServiceCompanyEdit.as_view()),
    path('reference_book/7/create/', TypeMaintenanceCreate.as_view()),
    path('reference_book/7/<int:pk>/edit/', TypeMaintenanceEdit.as_view()),
    path('reference_book/8/create/', DescriptionFailureCreate.as_view()),
    path('reference_book/8/<int:pk>/edit/', DescriptionFailureEdit.as_view()),
    path('reference_book/9/create/', RecoveryMethodCreate.as_view()),
    path('reference_book/9/<int:pk>/edit/', RecoveryMethodEdit.as_view()),

]
