from django.contrib import admin
from .models import *


admin.site.register(Machine)
admin.site.register(TechniqueModel)
admin.site.register(EngineModel)
admin.site.register(TransmissionModel)
admin.site.register(DriveAxleModel)
admin.site.register(SteerableAxleModel)
admin.site.register(ServiceCompany)
admin.site.register(TypeMaintenance)
admin.site.register(Maintenance)
admin.site.register(DescriptionFailure)
admin.site.register(RecoveryMethod)
admin.site.register(Reclamations)

