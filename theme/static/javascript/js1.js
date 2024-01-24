

// function for dashboard toggle button
function func1() {
        $("#left-side-pane").hide();
        console.log('i am cliked')

}
function func2() {
        $("#left-side-pane").show('visible');
        console.log('i am cliked show')

}
//end dashboard toggle button


/// wallet connect toggle button

// function func3() {
//         $("#dropdown").fadeToggle(100);
//         console.log('dropdown clicked');
        
// }

$("#wallet-cnt").mouseenter(
        () => {
                $("#dropdown").show();
        }
)
$("*").onclick(
        () => {
                $("#dropdown").hide();
        }
)

// end of wallet connect toggle button 



//  toggle function for surport button 
function func4() {
        $("#dropdown1").fadeToggle(100);
        
        
}

$("#surport").mouseover(
        ()=> {
                $("#dropdown1").show();
                console.log('i hovered');
        }
);
$("#dropdown1").mouseleave(
        function() {
                $("#dropdown1").hide(100);
        }
);

// end of toggle function for surport button 
