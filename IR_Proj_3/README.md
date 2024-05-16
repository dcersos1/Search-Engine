INFO-533 Project 3

The project that we have created is a web application that has the ability to take uploaded files from a user and allow them to query the words in these files and display the matching terms in a highlighting representation. 

Requirements

- Python
- Django
- Postgres
- some python libraries

Libraries and dependencies 

pip install Django
pip install PyPDF2
pip install pymupdf  # Also known as `fitz`
pip install nltk
pip install Pillow  # If image processing is needed, used by `PIL`
After installing Nltk , you might need to download certain data packages within a Python script or an interactive Python session:
import nltk
nltk.download('punkt')  # For tokenization
nltk.download('stopwords')  # If stopwords are used


Installation and Running the Application
# Install virtualenv if not already installed
pip install virtualenv

# Create a virtual environment
virtualenv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate

# On Unix or MacOS
source venv/bin/activate

# Install all required packages
pip install -r requirements.txt

1. Project Setup
Once the environment is ready with all the dependencies installed, the next steps involve setting up the Django project itself.

Initialize the Project:
If not already done, you can start a new Django project using:

django-admin startproject myproject

Navigate into the project directory:

cd myproject

Start an Application:

python manage.py startapp ir_app

2. Configure the Project
 Settings :

- Configure your settings in `myproject/settings.py`. Important settings include:

  - `INSTALLED_APPS` – Add your newly created app and any third-party apps.
  - `DATABASES` – Set up your database connection settings.
  - `STATIC_URL` and `MEDIA_URL` – Configure if serving media and static files.

Database Migrations:
Create and apply migrations for your database:

python manage.py makemigrations
python manage.py migrate



3. Create Superuser

To interact with the admin panel:

python manage.py createsuperuser

Follow the prompts to create an admin user.

4. Running the Development Server
You can run your Django development server using:

python manage.py runserver

This command starts the server on the default port 8000. You can access it by navigating to `http://127.0.0.1:8000/` in your web browser.

 5. Accessing the Admin Panel

Go to `http://127.0.0.1:8000/admin` and log in using the superuser credentials  created to manage your Django project's data.

Another way (once its uploaded on the git repository) :

1. Clone the repository:

2. Navigate to the project directory:

3. Install the required Python packages:

4. Apply the database migrations

5. Start server

6. Open a web browser and navigate to `http://127.0.0.1:8000/` to view the application.

Usage

Upload a file through the interface and its inverted index will be saved into the postgres database. You can do this as many times as you want and the new files will continue to be saved. We accept a variety of file formats which gives the website versatility in comparison to others. After uploading the files, the user has the ability to make query searches to see if the terms appear in any of the documents. The user can search one word queries, multi-word queries, and multiple queries at the same time. After doing this, the documents where the queries are present will be shown to the user. The user can click one of the documents for further investigation where he/she will see the terms are highlighted in different colors. Moreover, the format of the file is maintained, meaning a pdf will maintain its original format rather than looking different. 



 Uploading Documents
Our application provides a user-friendly interface that allows you to upload documents seamlessly. Once uploaded, each document is processed to create an inverted index which is then stored in a PostgreSQL database. This index plays a crucial role in enabling efficient search capabilities across the uploaded documents.

Supported File Formats:
The versatility of our application comes from its ability to handle a variety of file formats, including but not limited to PDF, DOCX, TXT, . This flexibility ensures that users can upload and process documents in the format most convenient to them without worrying about compatibility issues.

 Searching Documents
Once documents are uploaded and indexed, you can perform searches using the query interface provided on the website. This feature supports various types of queries to enhance your search experience:

- Single Word Queries: Enter a single word to find all documents containing that word.

- Multi-Word Queries: You can search for phrases or a combination of words to find documents that contain all specified terms in any order.

- Multiple Queries at Once: For advanced users, our system allows the submission of multiple distinct queries at the same time, providing results for each queried term or phrase in a consolidated view.

 Viewing Search Results
After submitting your queries, the system displays a list of documents where the search terms were found. Each entry in the search results provides basic document metadata such as the filename, and an option to delve deeper into the content. To render and highlight pdfs we leveraged PDF.js, an open source library developed by Mozilla which supports various functionality pertaining to pdfs. Feel free to view the inline comments in the views.py for a detailed description of this usage.

Document Investigation:
Clicking on a document in the search results will open a viewer where the relevant terms are highlighted in different colors. This not only helps in quickly locating the terms within the document but also maintains the original formatting and layout of the document. For PDFs, this means that the original pagination, graphics, and typesetting are preserved, offering a viewing experience that mirrors viewing the document in standard PDF readers.

Benefits of Our System:
- Efficiency: The use of a positional inverted index reduces the time needed to search documents dramatically, making it ideal for handling large volumes of data.
- Accuracy: Our advanced search algorithms ensure that users receive the most relevant results for their queries.
- User Experience:Designed with ease of use in mind, our platform ensures that even users with minimal technical knowledge can effectively upload documents and perform complex searches.
- Preservation of Document Integrity:Unlike some systems that alter the visual format of texts during processing, our system maintains the original appearance of all documents, ensuring that the context and visual cues remain intact.

This  robust set of features makes our document management system an indispensable tool for anyone needing to store, manage, and search through large sets of documents efficiently. Whether you're a researcher, a legal professional, or just someone needing to organize extensive data, our system provides the tools you need to simplify your workflow.

Authors
Adam Cersosimo
Daniel Cersosimo
Krishianjan Lanka
Owen Hovey
Vincent Ranieri
