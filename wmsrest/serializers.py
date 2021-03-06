# -*- coding: utf-8 -*-
from rest_framework import serializers
from wms.models import VirtualLayer, Dataset, Layer, SGridDataset, UGridDataset, RGridDataset, Variable


class VariableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Variable
        fields = ('id', 'std_name', 'units', 'default_min', 'default_max', 'logscale')


class LayerSerializer(serializers.ModelSerializer):
    styles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Layer
        fields = ('id', 'var_name', 'std_name', 'units', 'description', 'active', 'styles', 'default_min', 'default_max', 'logscale')


class VirtualLayerSerializer(serializers.ModelSerializer):
    styles = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = VirtualLayer
        fields = ('id', 'var_name', 'std_name', 'units', 'description', 'active', 'styles', 'default_min', 'default_max', 'logscale')


class DatasetSerializer(serializers.ModelSerializer):
    layer_set = LayerSerializer(many=True, read_only=True)
    virtuallayer_set = VirtualLayerSerializer(many=True, read_only=True)

    class Meta:
        model = Dataset
        fields = ('id',
                  'uri',
                  'type',
                  'name',
                  'title',
                  'abstract',
                  'keep_up_to_date',
                  'display_all_timesteps',
                  'layer_set',
                  'virtuallayer_set')


class UGridDatasetSerializer(serializers.ModelSerializer):
    layer_set = LayerSerializer(many=True, read_only=True)
    virtuallayer_set = VirtualLayerSerializer(many=True, read_only=True)

    class Meta:
        model = UGridDataset
        fields = ('id',
                  'uri',
                  'type',
                  'name',
                  'title',
                  'abstract',
                  'keep_up_to_date',
                  'display_all_timesteps',
                  'layer_set',
                  'virtuallayer_set')


class SGridDatasetSerializer(serializers.ModelSerializer):
    layer_set = LayerSerializer(many=True, read_only=True)
    virtuallayer_set = VirtualLayerSerializer(many=True, read_only=True)

    class Meta:
        model = SGridDataset
        fields = ('id',
                  'uri',
                  'type',
                  'name',
                  'title',
                  'abstract',
                  'keep_up_to_date',
                  'display_all_timesteps',
                  'layer_set',
                  'virtuallayer_set')


class RGridDatasetSerializer(serializers.ModelSerializer):
    layer_set = LayerSerializer(many=True, read_only=True)
    virtuallayer_set = VirtualLayerSerializer(many=True, read_only=True)

    class Meta:
        model = RGridDataset
        fields = ('id',
                  'uri',
                  'type',
                  'name',
                  'title',
                  'abstract',
                  'keep_up_to_date',
                  'display_all_timesteps',
                  'layer_set',
                  'virtuallayer_set')
