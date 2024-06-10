from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import FiatWallet, CryptoWallet, Transaction, BankAccount
# from .serializers import FiatTransferSerializer, CryptoTransferSerializer, TransactionSerializer
from .serializers import *
from .services import Transaction

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class TransactionView(APIView):
    def post(self, request):
        # Предположим, у вас есть сериализатор TransactionSerializer
        serializer = TransactionSerializer(data=request.data)
        
        # Проверяем валидность данных
        if serializer.is_valid():
            # Сохраняем данные, если они валидны
            serializer.save()
            
            # Возвращаем успешный ответ с кодом 201 CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            # Если данные не валидны, возвращаем ошибку с кодом 400 BAD REQUEST
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    


class FiatTransferView(APIView):
    """
    Представление для перевода фиатных средств.
    """
    def post(self, request):
        serializer = FiatTransferSerializer(data=request.data)
        if serializer.is_valid():
            from_wallet = get_object_or_404(FiatWallet, user=request.user)
            to_wallet_id = serializer.validated_data['to_wallet_id']
            amount = serializer.validated_data['amount']
            bank_account_id = serializer.validated_data['bank_account_id']
            to_wallet = get_object_or_404(FiatWallet, id=to_wallet_id)
            bank_account = get_object_or_404(BankAccount, id=bank_account_id)
            try:
                transaction_record = from_wallet.transfer(to_wallet, amount, bank_account)
                transaction_serializer = TransactionSerializer(transaction_record)
                return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CryptoTransferView(APIView):
    """
    Представление для перевода криптовалютных средств.
    """
    def post(self, request):
        serializer = CryptoTransferSerializer(data=request.data)
        if serializer.is_valid():
            from_wallet = get_object_or_404(CryptoWallet, user=request.user)
            to_wallet_id = serializer.validated_data['to_wallet_id']
            amount = serializer.validated_data['amount']
            currency_code = serializer.validated_data['currency_code']
            to_wallet = get_object_or_404(CryptoWallet, id=to_wallet_id)
            try:
                transaction_record = from_wallet.transfer(to_wallet, amount, currency_code)
                transaction_serializer = TransactionSerializer(transaction_record)
                return Response(transaction_serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
