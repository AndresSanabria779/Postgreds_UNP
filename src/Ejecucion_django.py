from django.db import connection
from django.db import connections

print(connections.databases)
print(connections.all())
