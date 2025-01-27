document.querySelectorAll('.chain-button').forEach(button => {
    button.addEventListener('click', () => {
        const checkbox = button.querySelector('input[type="checkbox"]');
        checkbox.checked = !checkbox.checked;
        button.classList.toggle('selected', checkbox.checked);
    });
});

document.getElementById('select-all').addEventListener('click', () => {
    const allButtons = document.querySelectorAll('.chain-button');
    const selectAll = [...allButtons].some(button => !button.querySelector('input').checked);
    allButtons.forEach(button => {
        const checkbox = button.querySelector('input[type="checkbox"]');
        checkbox.checked = selectAll;
        button.classList.toggle('selected', selectAll);
    });
});

function clearError() {
    const errorMessage = document.getElementById('error-message-label');
    if (errorMessage) {
        errorMessage.style = 'display: none';
    }
}

