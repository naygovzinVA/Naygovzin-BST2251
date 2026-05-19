function togglePost(postId) {
    const postContent = document.getElementById('postContent-' + postId);
    const button = document.querySelector('[onclick="togglePost(' + postId + ')"]');

    if (postContent.classList.contains('collapsed')) {
        postContent.classList.remove('collapsed');
        button.textContent = 'Свернуть';
    } else {
        postContent.classList.add('collapsed');
        button.textContent = 'Развернуть';
    }
}