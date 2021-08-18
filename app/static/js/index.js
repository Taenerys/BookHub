function deleteBook(bookId) {
    fetch('/delete', {
        method: 'POST',
        body: JSON.stringify({ bookId: bookId }),
    }).then((_res) => {
        // Note: can change this URL to any endpoint you'd like
        window.location.href = "/catalog"
    });
}