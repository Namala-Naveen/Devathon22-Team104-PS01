const select = document.querySelector('#asking');
const cseselect = document.querySelector('.cse');
const eeeselect = document.querySelector('.eee');
const mechselect = document.querySelector('.mech');

let store = select;

select.addEventListener('change' , (eve)=>{
    if (store!==select)
     store.classList.remove('unhide');
    setTimeout(()=>{
     if (eve.target.value=='CSE')
    {  cseselect.classList.add('unhide'); store=cseselect;}
    else if (eve.target.value=='EEE')
    {  eeeselect.classList.add('unhide'); store=eeeselect;}
    else if (eve.target.value=='MECH')
    {  mechselect.classList.add('unhide'); store=mechselect;}
},250)})
