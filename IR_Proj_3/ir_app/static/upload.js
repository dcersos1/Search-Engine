var datafile=null;

document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('uploadForm');
    const uploadMessage = document.getElementById('uploadMessage');
    const numFilesUploaded = document.getElementById('numFilesUploaded');

    form.addEventListener('submit', function(e) {
        e.preventDefault();

        const fileInput = document.getElementById('fileInput');
        const files = fileInput.files;

        if (files.length === 0) {
            uploadMessage.textContent = 'Please select at least one file to upload.';
            return;
        }

        const formData = new FormData(form);

        fetch('/upload', {
            method: 'POST',
            body: formData
        })
        .then(response => {
            console.log('Response status:', response.status);
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        })
        .then(data => {
            datafile=data
            console.log('Response data:', data);
            uploadMessage.textContent = data.message;
            numFilesUploaded.textContent = `Files uploaded: ${data.filenames.length}`;
            jsonfile={"datafile":datafile.uploaded_files[0].processed_text[0]};
            console.log(jsonfile)
            
        })
        .catch(error => {
            console.error('Error:', error);
            uploadMessage.textContent = 'Failed to upload files.';
        });
    });
});