const endpoint = `http://localhost:8000/`;

let deleteButton = document.getElementById('deleteButton');
let updateButton = document.getElementById('updateButton');

let parkId = document.getElementById('parkId').value;

deleteButton.addEventListener('click', () => {
  fetch(`${endpoint}deletepoint/${parkId}`, {
    method: 'POST',
  });
});
