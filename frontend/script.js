const API_URL = "http://localhost:5000/api";

function loadData() {
    fetch(`${API_URL}/info`)
        .then(res => res.json())
        .then(data => {
            document.getElementById('title').innerText = data.judul_katalog;
            document.getElementById('owner').innerText = data.pemilik;
            document.getElementById('nim').innerText = data.nim;

            const list = document.getElementById('item-list');
            list.innerHTML = '';

            data.items.forEach(item => {
                let li = document.createElement('li');
                li.innerText = item;
                list.appendChild(li);
            });
        });
}

function tambahItem() {
    const input = document.getElementById('item-input');

    fetch(`${API_URL}/add-item`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ item: input.value })
    })
    .then(() => {
        input.value = '';
        loadData();
    });
}

loadData();