document.addEventListener('DOMContentLoaded', () => {
    // Copy to Clipboard
    const copyButtons = document.querySelectorAll('.copy-btn');
    
    copyButtons.forEach(button => {
        button.addEventListener('click', async () => {
            const container = button.closest('.code-container');
            const code = container.querySelector('code').innerText;
            
            try {
                await navigator.clipboard.writeText(code);
                const originalText = button.innerText;
                button.innerText = '✅ Copiado!';
                button.style.background = '#10b981';
                
                setTimeout(() => {
                    button.innerText = originalText;
                    button.style.background = '';
                }, 2000);
            } catch (err) {
                console.error('Falha ao copiar:', err);
                alert('Erro ao copiar código.');
            }
        });
    });

    // Scroll Animations (opcional - apenas se quiser manter o efeito)
    const observerOptions = {
        threshold: 0.1
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animate');
            }
        });
    }, observerOptions);

    document.querySelectorAll('section, .step-item, .toc').forEach(el => {
        observer.observe(el);
    });
});
