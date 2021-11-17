from django.db import models


class RequisiteHistory(models.Model):
    description = Models.TextField('History of requisite')
    price = Models.FloatField('Price of requisite')
    requisite_id = Models.ForeignKey(Requisite, on_delete=Models.CASCADE)


class RequisiteType(models.Model):
    type = Models.CharField('Type of requisite', max_length=50)


class Requisite(models.Model):
    name = Models.CharField('Name of requisite', max_length=30)
    requisite_type_id = Models.ForeignKey(RequisiteType, on_delete=Models.CASCADE)


class RequisitePosterRole(models.Model):
    requisite_id = Models.ForeignKey(Requisite, on_delete=Models.CASCADE)
    poster_id = Models.ForeignKey(Poster, on_delete=Models.CASCADE)
    role_id = Models.ForeignKey(Role, on_delete=Models.CASCADE)
