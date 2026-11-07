const adviserGallery = document.querySelector('.adviser-gallery');
const adviserDialog = document.querySelector('.adviser-gallery-dialog');
const adviserMobile = window.matchMedia('(max-width: 768px)');

function resetAdviserGallery(event) {
    adviserGallery.open = !event.matches;
}

resetAdviserGallery(adviserMobile);
adviserMobile.addEventListener('change', resetAdviserGallery);

if (typeof adviserDialog.showModal === 'function') {
    const enlargedImage = adviserDialog.querySelector('img');
    const enlargedCaption = adviserDialog.querySelector('p');
    let imageTrigger;

    adviserGallery.addEventListener('click', (event) => {
        const link = event.target.closest('.adviser-gallery-image');
        if (!link || event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) {
            return;
        }

        event.preventDefault();
        imageTrigger = link;
        enlargedImage.src = link.href;
        enlargedImage.alt = link.querySelector('img').alt;
        enlargedCaption.textContent = link.nextElementSibling.textContent;
        adviserDialog.showModal();
    });

    adviserDialog.addEventListener('close', () => {
        const focusTarget = adviserGallery.open ? imageTrigger : adviserGallery.querySelector('summary');
        focusTarget.focus();
    });
}
