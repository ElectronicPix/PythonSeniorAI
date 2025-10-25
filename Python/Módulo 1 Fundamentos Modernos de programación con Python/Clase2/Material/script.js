document.addEventListener('DOMContentLoaded', function () {
    // Navegación profesional por menú
    const navLinks = document.querySelectorAll('.main-nav .nav-link');
    const sections = document.querySelectorAll('.section');

    navLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            e.preventDefault();
            // Quitar activo de todos
            navLinks.forEach(l => l.classList.remove('active'));
            link.classList.add('active');
            // Scroll suave a la sección
            const targetId = link.getAttribute('href').replace('#', '');
            const targetSection = document.getElementById(targetId);
            if (targetSection) {
                window.scrollTo({
                    top: targetSection.offsetTop - 80,
                    behavior: 'smooth'
                });
            }
        });
    });

    // Mostrar/ocultar ejemplos de código
    const buttons = document.querySelectorAll('.toggle-btn');
    const codeBlocks = document.querySelectorAll('.code-example');
    const cards = document.querySelectorAll('.data-type-card');

    buttons.forEach((btn, idx) => {
        btn.addEventListener('click', function () {
            // Cerrar todos los bloques de código excepto el de la misma lista
            const parentSection = btn.closest('.section');
            const sectionCodeBlocks = parentSection.querySelectorAll('.code-example');
            sectionCodeBlocks.forEach((block, i) => {
                if (block !== btn.nextElementSibling) block.classList.remove('active');
            });
            // Alternar el bloque correspondiente
            const codeBlock = btn.nextElementSibling;
            if (codeBlock) codeBlock.classList.toggle('active');
        });
    });

    // Efecto hover profesional en las tarjetas
    cards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.boxShadow = '0 4px 24px rgba(48, 105, 152, 0.18)';
            card.style.transform = 'translateY(-4px) scale(1.02)';
        });
        card.addEventListener('mouseleave', () => {
            card.style.boxShadow = '';
            card.style.transform = '';
        });
    });
}); 