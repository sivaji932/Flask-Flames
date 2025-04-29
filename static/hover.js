document.addEventListener('DOMContentLoaded', () => {
    const tooltips = document.querySelectorAll('.has-tooltip');
  
    tooltips.forEach(button => {
      const tooltip = button.querySelector('.tooltip');
  
      button.addEventListener('mouseenter', () => {
        tooltip.classList.remove('opacity-0', 'invisible');
        tooltip.classList.add('opacity-100', 'visible');
      });
  
      button.addEventListener('mouseleave', () => {
        tooltip.classList.remove('opacity-100', 'visible');
        tooltip.classList.add('opacity-0', 'invisible');
      });
    });
  });
  