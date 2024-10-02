from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from bangazonapi.models import Store, Product, Customer

class StoreSellerSerializer(serializers.ModelSerializer):
    """Serializer for seller details (Customer's User fields)"""

    first_name = serializers.CharField(source='user.first_name')
    last_name = serializers.CharField(source='user.last_name')

    class Meta:
        model = Customer
        fields = ('first_name', 'last_name')

class StoreProductSerializer(serializers.ModelSerializer):
    """JSON serializer for products in a store"""
    
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'description', 'quantity')

class StoreSerializer(serializers.ModelSerializer):
    """JSON serializer for stores and their products"""
    
    seller = StoreSellerSerializer(read_only=True)
    products = StoreProductSerializer(many=True, read_only=True)

    class Meta:
        model = Store
        fields = ('id', 'name', 'description', 'seller', 'products')

class StoreViewSet(ViewSet):
    """View for handling requests about stores"""

    def list(self, request):
        """GET a list of stores with products for sale"""
        stores = Store.objects.all()  # Fetch all stores
        serializer = StoreSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        """POST a new store"""
        customer = Customer.objects.get(user=request.auth.user)  # Fetch customer
        
        new_store = Store.objects.create(
            name=request.data['name'],
            description=request.data['description'],
            seller=customer
        )
        
        serializer = StoreSerializer(new_store)
        print("Store Created with ID:", new_store.id)  # Debugging log for backend
        print("Serialized data:", serializer.data)  # Add this log for debugging
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        """GET a single store by ID"""
        try:
            store = Store.objects.get(pk=pk)
            serializer = StoreSerializer(store)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Store.DoesNotExist:
            return Response({'message': 'Store not found.'}, status=status.HTTP_404_NOT_FOUND)