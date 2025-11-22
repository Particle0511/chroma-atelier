async function generatePalette() {
    const input = document.getElementById('queryInput');
    const container = document.getElementById('paletteContainer');
    const loader = document.getElementById('loader');
    const query = input.value.trim();

    if (!query) return;

    
    loader.classList.remove('hidden');
    
    
    container.innerHTML = '';
    container.style.opacity = '0';
    
    
    resetFusion();

    try {
        
        const minLoadingTime = new Promise(resolve => setTimeout(resolve, 1500));
        const apiCall = fetch('/generate', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ query: query })
        });

        
        const [_, response] = await Promise.all([minLoadingTime, apiCall]);

        if (!response.ok) throw new Error('API Error');
        const data = await response.json();
        
        
        renderArtisticPalette(data.colors);
        activateFusion(data.colors);

    } catch (error) {
        console.error(error);
        showToast("THE MUSE IS SILENT");
    } finally {
        loader.classList.add('hidden');
    }
}

function renderArtisticPalette(colors) {
    const container = document.getElementById('paletteContainer');
    container.style.opacity = '1';

    colors.forEach((color, index) => {
        const strip = document.createElement('div');
        strip.className = 'color-strip';
        strip.style.backgroundColor = color.hex;
        
        strip.style.transform = 'translateY(100%)';
        strip.style.opacity = '0';
        
        const tag = document.createElement('div');
        tag.className = 'hex-tag';
        tag.textContent = color.hex;
        
        strip.appendChild(tag);
        
        strip.onclick = () => {
            navigator.clipboard.writeText(color.hex);
            showToast(`${color.hex} COPIED`);
        };
        
        container.appendChild(strip);

        setTimeout(() => {
            strip.style.transition = 'transform 1s cubic-bezier(0.22, 1, 0.36, 1), opacity 1s ease, flex 0.7s ease';
            strip.style.transform = 'translateY(0)';
            strip.style.opacity = '1';
        }, index * 150);
    });
}

function activateFusion(colors) {
    const fusionBg = document.getElementById('fusionBg');
    const subheading = document.getElementById('mainHeading');
    
   
    const gradient = `linear-gradient(135deg, ${colors[0].hex}, ${colors[2].hex}, ${colors[4].hex})`;
    
    fusionBg.style.background = gradient;
    fusionBg.classList.add('active');
    
    subheading.style.backgroundImage = gradient;
    subheading.classList.add('dynamic-text');

    
    const hex = colors[2].hex.replace('#', '');
    const r = parseInt(hex.substr(0, 2), 16);
    const g = parseInt(hex.substr(2, 2), 16);
    const b = parseInt(hex.substr(4, 2), 16);
    
    
    const brightness = ((r * 299) + (g * 587) + (b * 114)) / 1000;

    if (brightness < 128) {
        document.body.classList.add('dark-theme');
    } else {
        document.body.classList.remove('dark-theme');
    }
}

function resetFusion() {
    const fusionBg = document.getElementById('fusionBg');
    const subheading = document.getElementById('mainHeading');
    
    fusionBg.classList.remove('active');
    subheading.classList.remove('dynamic-text');
    subheading.style.backgroundImage = 'none';
    document.body.classList.remove('dark-theme'); 
}

function showToast(message) {
    const toast = document.getElementById('toast');
    toast.textContent = message;
    toast.classList.add('visible');
    setTimeout(() => { toast.classList.remove('visible'); }, 3000);
}

document.getElementById('queryInput').addEventListener('keypress', (e) => {
    if (e.key === 'Enter') generatePalette();
});