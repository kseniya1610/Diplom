from django.db import models
from django.contrib.auth.models import User


class CustomUser(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.first_name


class TechniqueModel(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель техники'
        verbose_name_plural = 'Модели техники'


class EngineModel(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель двигателя'
        verbose_name_plural = 'Модели двигателей'


class TransmissionModel(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель трансмиссии'
        verbose_name_plural = 'Модели трансмиссий'


class DriveAxleModel(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель ведущего моста'
        verbose_name_plural = 'Модели ведущих мостов'


class SteerableAxleModel(models.Model):
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Модель управляемого моста'
        verbose_name_plural = 'Модели управляемых мостов'


class ServiceCompany(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, verbose_name='Имя пользователя')
    name = models.TextField(unique=True, verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Сервисные компании'
        verbose_name_plural = 'Сервисные компании'


class Machine(models.Model):
    factory_number = models.TextField(max_length=17, unique=True, db_index=True, verbose_name='Заводской номер')
    technique_model = models.ForeignKey(TechniqueModel, on_delete=models.CASCADE, db_index=True,
                                        verbose_name='Модель техники')
    engine_model = models.ForeignKey(EngineModel, on_delete=models.CASCADE, db_index=True,
                                     verbose_name='Модель двигателя')
    engine_number = models.TextField(max_length=17, verbose_name='Номер двигателя')
    transmission_model = models.ForeignKey(TransmissionModel, on_delete=models.CASCADE, db_index=True,
                                           verbose_name='Модель трансмиссии')
    transmission_number = models.TextField(max_length=50, verbose_name='Номер трансмиссии')
    drive_axle_model = models.ForeignKey(DriveAxleModel, on_delete=models.CASCADE, db_index=True,
                                         verbose_name='Модель ведущего моста')
    drive_axle_number = models.TextField(max_length=50, verbose_name='Номер ведущего моста')
    steerable_axle_model = models.ForeignKey(SteerableAxleModel, on_delete=models.CASCADE, db_index=True,
                                             verbose_name='Модель управляемого моста')
    steerable_axle_number = models.TextField(max_length=50, verbose_name='Номер управляемого моста')
    supply_contract = models.TextField(max_length=50, blank=True, verbose_name='Договор поставки №, дата.')
    date_of_shipment_from_the_factory = models.DateField(db_index=True, verbose_name='Дата отгрузки с завода')
    consignee = models.TextField(max_length=50, blank=True, verbose_name='Грузополучатель')
    delivery_address = models.TextField(max_length=300, blank=True, verbose_name='Адрес поставки')
    equipment = models.TextField(blank=True, verbose_name='Комплектация (доп. опции)')
    client = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Клиент')
    service_company = models.ForeignKey(ServiceCompany, null=True, on_delete=models.CASCADE, blank=True,
                                        verbose_name='Сервисная организация')

    def __str__(self):
        return f'{self.factory_number}'

    class Meta:
        verbose_name = 'Машины'
        verbose_name_plural = 'Машины'
        ordering = ['date_of_shipment_from_the_factory']


class TypeMaintenance(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Вид ТО'
        verbose_name_plural = 'Вид ТО'


class Maintenance(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная организация')
    type_maintenance = models.ForeignKey(TypeMaintenance, on_delete=models.CASCADE, verbose_name='Вид ТО')
    maintenance_date = models.DateField(verbose_name='Дата проведения ТО')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    order = models.TextField(max_length=50, verbose_name='Номер заказа-наряда')
    order_date = models.DateField(verbose_name='Дата заказа-наряда')

    def __str__(self):
        return f'{self.machine, self.type_maintenance}'

    class Meta:
        verbose_name = 'ТО'
        verbose_name_plural = 'ТО'
        ordering = ['maintenance_date']


class DescriptionFailure(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Характер отказа'
        verbose_name_plural = 'Характер отказа'


class RecoveryMethod(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(blank=True, verbose_name='Описание')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Способ восстановления'
        verbose_name_plural = 'Способ восстановления'


class Reclamations(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE, verbose_name='Машина')
    service_company = models.ForeignKey(ServiceCompany, on_delete=models.CASCADE, verbose_name='Сервисная организация')
    date_of_refusal = models.DateField(verbose_name='Дата отказа')
    operating_time = models.IntegerField(verbose_name='Наработка м/час')
    failure_node = models.TextField(verbose_name='Узел отказа')
    description_failure = models.ForeignKey(DescriptionFailure, on_delete=models.CASCADE,
                                            verbose_name='Характер отказа')
    recovery_method = models.ForeignKey(RecoveryMethod, on_delete=models.CASCADE, verbose_name='Способ восстановления')
    parts_used = models.TextField(blank=True, verbose_name='Используемые запасные части')
    date_of_restoration = models.DateField(verbose_name='Дата восстановления')
    equipment_downtime = models.TextField(verbose_name='Время простоя техники')

    def __str__(self):
        return f'{self.machine, self.failure_node}'

    class Meta:
        verbose_name = 'Рекламации'
        verbose_name_plural = 'Рекламации'
        ordering = ['date_of_refusal']
