document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('searchForm');
    const searchResults = document.getElementById('searchResults');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const formData = new FormData(form);
        fetch('/search_documents', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            searchResults.innerHTML = ''; 
            if (data.results.length === 0) {
                searchResults.innerHTML = '<p>No documents found.</p>';
            } else {
                data.results.forEach(result => {
                    const documentHTML = `<div class="document">
                                            <h3>Document ID: ${result.doc_id}</h3>
                                            <p>${result.content}</p>
                                        </div>`;
                    searchResults.insertAdjacentHTML('beforeend', documentHTML);
                });
            }
        })
        .catch(error => {
            searchResults.innerHTML = '<p>Failed to fetch search results.</p>';
        });
    });
});
