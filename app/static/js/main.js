console.log("Flask SPA loaded successfully!");

// Add a small delay before starting the animation to ensure proper rendering
setTimeout(() => {
    const scrollingText = document.querySelector('.scrolling-text span');
    scrollingText.style.animationPlayState = 'running';
}, 100);
