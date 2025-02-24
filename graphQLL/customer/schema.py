import graphene
from graphene_django import DjangoObjectType
from .models import *

# ClientType is a GraphQL type based on the Django Client model.
class ClientType(DjangoObjectType):
    class Meta:
        model = Client
        fields = ('id', 'first_name', 'last_name', 'city')

# all_clients = graphene.List(ClientType):
# Defines a field all_clients that returns a list of ClientType objects.
class Query(graphene.ObjectType):

    all_clients = graphene.List(ClientType)

    def resolve_all_clients(root, info):
        return Client.objects.all()

#This creates the GraphQL schema with the Query class as the entry point.
# It enables GraphQL queries like:
schema = graphene.Schema(query=Query)


# ✅ GraphQL Type: Defines what data looks like (ClientType).
# ✅ GraphQL Query Type: Defines what data can be requested (Query).
# ✅ all_clients is not predefined; you can name it anything.