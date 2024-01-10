// current_year.js

document.addEventListener('DOMContentLoaded', function() {
    var currentYear = new Date().getFullYear();
    var yearElement = document.getElementById('año-actual');
    if (yearElement) {
        yearElement.textContent = currentYear;
    }
});
