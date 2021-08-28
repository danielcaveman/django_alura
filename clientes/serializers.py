from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
    
    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':'O CPF deve ter 11 dígitos'})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome':'O nome não deve conter caracteres numéricos'})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg':'O RG deve conter 9 dígitos'})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular':'O celular deve conter pelo menos 11 dígitos'})            
        return data    

