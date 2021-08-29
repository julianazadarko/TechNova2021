window.onload = () => {
    const tab_switchers = document.querySelectorAll('[data-switcher]');

    for (let i = 0; i < tab_switchers.length; i++) {
        const tab_switcher = tab_switchers[i];
        const tab_id = tab_switcher.dataset.tab;

        //console.log('in for loop with dataset :' + JSON.stringify(tab_switcher.dataset));
        //console.log('in for loop with dataset :' + JSON.stringify(tab_switcher.dataset.tab));
        //console.log('in for loop with :' + tab_id);

        tab_switcher.addEventListener('click', () => {
            document.querySelector('.row .column.is-active').classList.remove('is-active');
            tab_switcher.parentNode.parentNode.classList.add('is-active');
            SwitchTab(tab_id);
        });
    }
}

function SwitchTab (tab_id) {
    //console.log("tab_id: " + tab_id);
    const current_tab = document.querySelector('.input-qs .q-group.is-active');
    current_tab.classList.remove('is-active');
    
    const next_tab = document.querySelector(`.input-qs .q-group[data-page="${tab_id}"]`);
    next_tab.classList.add('is-active');
}