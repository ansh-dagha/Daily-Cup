

function update_feed(){
    var checkBoxes = document.getElementsByClassName('interested-news');
    let count=0;
    for (var i = 0; i < checkBoxes.length; i++)
    {  
        if ( !checkBoxes[i].checked )
        {
            count++;
            var cards = document.getElementsByClassName(('card-'+checkBoxes[i].id));
            for (var j = 0; j < cards.length; j++){
                cards[j].classList.add('hidden-card');
            }  
        }
        else{
            var cards = document.getElementsByClassName(('card-'+checkBoxes[i].id));
            for (var j = 0; j < cards.length; j++){
                cards[j].classList.remove('hidden-card');
            }
        }
    }
    if(count == 4){
        var cards = document.getElementsByClassName('hidden-card');
        for (var j = 0; j < cards.length; j++){
            cards[j].classList.remove('hidden-card');
        }
    }
}