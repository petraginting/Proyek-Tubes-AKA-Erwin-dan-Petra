function searchGame() {
    const query = document.getElementById('searchInput').value.toLowerCase();
    const games = document.querySelectorAll('.game-card');
    
    games.forEach(game => {
        const gameName = game.querySelector('p').textContent.toLowerCase();
        if (gameName.includes(query)) {
            game.style.display = 'block';  // Show game if it matches
        } else {
            game.style.display = 'none';  // Hide game if it doesn't match
        }
    });
}

function showGameDetails(gameName) {
    alert('Menampilkan detail untuk ' + gameName);
}
