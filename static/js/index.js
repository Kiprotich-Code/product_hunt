// Animation - paragraphs 
document.addEventListener('DOMContentLoaded', function() {
    const fadeInElements = document.querySelectorAll('.fade-in');
  
    function fadeInOnScroll() {
      fadeInElements.forEach(element => {
        const elementTop = element.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
  
        if (elementTop < windowHeight) {
          element.classList.add('visible'); // Add the visible class
        } else {
          element.classList.remove('visible'); // Remove the visible class
        }
      });
    }
  
    window.addEventListener('scroll', fadeInOnScroll);
    fadeInOnScroll(); // Initial check
  });
  

// animation - cards 
document.addEventListener('DOMContentLoaded', function() {
    const card = document.querySelector('.card');
  
    function slideInCardOnScroll() {
      const elementTop = card.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
  
      if (elementTop < windowHeight) {
        card.classList.add('slide-in');
      }
    }
  
    window.addEventListener('scroll', slideInCardOnScroll);
    slideInCardOnScroll(); // Initial check
  });

  
function inProgress() {
    alert('Men at work! Feature build in progress!')
}

// TRUNCATED WORDS IN PRODUCTS 
function toggleDescription(index) {
  var preview = document.getElementById('desc-preview-' + index);
  var full = document.getElementById('desc-full-' + index);
  
  if (preview.classList.contains('d-none')) {
      preview.classList.remove('d-none');
      full.classList.add('d-none');
  } else {
      preview.classList.add('d-none');
      full.classList.remove('d-none');
  }
}