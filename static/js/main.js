// Form validation
document.addEventListener('DOMContentLoaded', function() {
    // Contact form validation
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', function(e) {
            let isValid = true;
            const email = document.getElementById('email');
            const message = document.getElementById('message');

            if (!validateEmail(email.value)) {
                showError(email, 'Please enter a valid email address');
                isValid = false;
            }

            if (message.value.trim().length < 10) {
                showError(message, 'Message must be at least 10 characters long');
                isValid = false;
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // Donation form validation
    const donateForm = document.getElementById('donateForm');
    if (donateForm) {
        donateForm.addEventListener('submit', function(e) {
            let isValid = true;
            const amount = document.getElementById('amount');
            
            if (isNaN(amount.value) || amount.value <= 0) {
                showError(amount, 'Please enter a valid donation amount');
                isValid = false;
            }

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // Initialize tooltips
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });

    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
});

// Helper functions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showError(element, message) {
    const errorDiv = document.createElement('div');
    errorDiv.className = 'invalid-feedback';
    errorDiv.innerText = message;
    element.classList.add('is-invalid');
    
    // Remove existing error message if any
    const existing = element.parentElement.querySelector('.invalid-feedback');
    if (existing) {
        existing.remove();
    }
    
    element.parentElement.appendChild(errorDiv);
}

// Remove validation styling on input
document.addEventListener('input', function(e) {
    if (e.target.classList.contains('is-invalid')) {
        e.target.classList.remove('is-invalid');
        const errorDiv = e.target.parentElement.querySelector('.invalid-feedback');
        if (errorDiv) {
            errorDiv.remove();
        }
    }
});
