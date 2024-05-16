from django.db import models

# Create your models here.

#Here we create the classes for two relations

#One is the invertedindex which will store to positional inverted index to allow for conistentent updating 
#as the corpus grows as well as allow for storage of said data even when the application is not running.
#We leverage json_field here so it can store this positonal inverted index effecivley
class invertedindex(models.Model):
    Index = models.JSONField()  # List of document IDs and positions

#The second is the documents which is a postgresrelation to store the binary content of each file type
#alongside said filetype. In additon we leverage djanogs automatic pk generation to track doc_ids
#while implementing logic later to ensure this is an effecilve practice
class documents(models.Model):
    content = models.BinaryField()  # Store binary content of the files
    file_type = models.CharField(max_length=50)  # Store the file type as a string (e.g., 'pdf', 'txt', 'docx')


    