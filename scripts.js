/* =======================================
           DASHBOARD SCRIPTS          
 ======================================= */
   
    // Popover effects for Dashboard app icons

    var bindToMe_1 = document.createElement('a')    
    $('#target1').popover({
        content: bindToMe_1,                
        placement: 'left',
        trigger: 'hover',
        delay: {
            show: 1000,                // 500 = half a second, 1000 = 1 second, etc... In case you want to adjust the delay for longer or shorter
        },
        html: true
    });    
    bindToMe_1.innerHTML = "<em>Description:</em> <br> Take the opportunity to plan steps of your upcoming trips.  Check them off as you go.  <br> CLICK THE APP ICON TO GET STARTED!!";

    var bindToMe_2 = document.createElement('a')  
    $('#target2').popover({
        content: bindToMe_2,    
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1000,
        },
        html: true
    });    
    bindToMe_2.innerHTML = "<em>Description:</em> <br> Take the opportunity to plan expenses of your upcoming trips.  Make adjustments to give you the best experience possible! <br> CLICK THE APP ICON TO GET STARTED!!";
    
    var bindToMe_3 = document.createElement('a')   
    $('#target3').popover({
        content: bindToMe_3,        
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1000,
        },
        html: true
    });     
    bindToMe_3.innerHTML = "<em>Description:</em> <br> Take the opportunity to research potential travel destinations.  Look up current reports to ensure a safe trip. <br> CLICK THE APP ICON TO GET STARTED!!";

    var bindToMe_4 = document.createElement('a')    
    $('#target4').popover({
        content: bindToMe_4,       
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1000,
        },
        html: true
    });      
    bindToMe_4.innerHTML = "<em>Description:</em> <br> Take the opportunity to examine the current currency exchange between home and abroad.  <br> CLICK THE APP ICON TO GET STARTED!!";
        
   
    var bindToMe_5 = document.createElement('a')    
    $('#target5').popover({
        content: bindToMe_5,
        placement: "left",
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_5.innerHTML = "<em>Description:</em> <br> Take the opportunity to find information of flights available for your next trip.  <br> CLICK THE APP ICON TO GET STARTED!!";
    
    var bindToMe_6 = document.createElement('a')
    $('#target6').popover({
        content: bindToMe_6,
        placement: "bottom",
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_6.innerHTML = "<em>Description:</em> <br> Take the opportunity to research hotel and lodging options for your next trip.  <br> CLICK THE APP ICON TO GET STARTED!!";

    var bindToMe_7 = document.createElement('a')
    $('#target7').popover({
        content: bindToMe_7,
        placement: 'bottom',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_7.innerHTML = "<em>Description:</em> <br> Chat about your findings with your friends and colleagues.  <br> CLICK THE APP ICON TO GET STARTED!!";

    var bindToMe_8 = document.createElement('a')
    $('#target8').popover({
        content: bindToMe_8,
        placement: 'bottom',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_8.innerHTML = "This is what the Future App is for...Currently under construction";

    var bindToMe_9 = document.createElement('a')
    $('#target9').popover({
        content: bindToMe_9,
        placement: 'left',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_9.innerHTML = "This is what the Future App is for...Currently under construction";

    var bindToMe_10 = document.createElement('a')
    $('#target10').popover({
        content: bindToMe_10,
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_10.innerHTML = "This is what the Future App is for...Currently under construction";

    var bindToMe_11 = document.createElement('a')
    $('#target11').popover({
        content: bindToMe_11,
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_11.innerHTML = "This is what the Future App is for...Currently under construction";

    var bindToMe_12 = document.createElement('a')
    $('#target12').popover({
        content: bindToMe_12,
        placement: 'top',
        trigger: 'hover',
        delay: {
            show: 1500,
        },
        html: true
    });    
    bindToMe_12.innerHTML = "This is what the Future App is for...Currently under construction";

/********SCRIPTS FOR TOGGLING SIDEMENU**********/

function openMenu() {
    document.getElementById("sideMenu").style.width = "250px";
}
function closeMenu() {
    document.getElementById("sideMenu").style.width = "0";
}
/*toggleWidgetOff/navbar-btn is display = none*/
/*toggleWidgetOn/btn-close  is display = block*/

$(document).ready(function() {
    document.getElementById("btn-close").addEventListener("click", toggleWidgetOn)
    document.getElementById("navbar-btn").addEventListener("click", toggleWidgetOff)
})

function toggleWidgetOff() {
    document.getElementById("widgetPopup").style.display = "none";
}

function toggleWidgetOn() {
    var e = document.getElementById("widgetPopup").style.display = "block";
}

/********SCRIPTS FOR CHANGING BACKGROUND IMAGE**********/
$(userBackground);
var img = ["/static/images/traveling.jpg","/static/images/Airplane.jpg","/static/images/Beach.jpg","/static/images/Florence.jpg"];
var len = img.length;
var current = -1;
for (i in img){
    console.log(i+' '+img[i]);
}
function changeBg(dir) {
    if (dir === 'right' && current === len - 1) { 
        current = 0;
        renderImgIndex(current);
    } else if (dir === 'right' && current < len - 1) {
        current++;
        renderImgIndex(current);
    } else if (dir === 'left' && current === 0) {
        current = len - 1;
        renderImgIndex(current);
    } else if (dir === 'left' && current > 0) {
        current--;
        renderImgIndex(current);
    }
}
function userBackground() {
    var backgroundImage = localStorage.getItem('b');
    if (backgroundImage) {
        $('body').css('background-image', 'url(' + backgroundImage + ')');
    }
}
function renderImgIndex(imgIndex) {
    $('body').css('background-image', 'url(' + img[imgIndex] + ')');
        console.log(imgIndex +" "+ img[imgIndex]);
        localStorage.setItem('b', img[imgIndex]);
        console.log(localStorage)
        userBackground();
}
/*************END BACKGROUND SCRIPTS***************/

/*************START HOME PAGE BOTTOM WIDGET SCRIPTS***************/

/******START WIDGET 1**********/
  function openForm1() {
    document.getElementById("myWidget1").style.display = "block";
  }
  
  function submitForm1() {
      document.getElementById("myWidget1").style.display = "block";
  }
  
  function closeForm1() {
    document.getElementById("myWidget1").style.display = "none";
  }
  /********END WIDGET 1*********/
  
  /*******START WIDGET 2********/
    function openForm2() {
      document.getElementById("myWidget2").style.display = "block";
    }
    
    function submitForm2() {
        document.getElementById("myWidget2").style.display = "block";
    }
    
    function closeForm2() {
      document.getElementById("myWidget2").style.display = "none";
    }
  /********END WIDGET 2*********/
  
  /*******START WIDGET 3********/
    function openForm3() {
      document.getElementById("myWidget3").style.display = "block";
    }
    
    function submitForm3() {
        document.getElementById("myWidget3").style.display = "block";
    }
    
    function closeForm3() {
      document.getElementById("myWidget3").style.display = "none";
    }
   /********END WIDGET 3*********/
  
  /*******START WIDGET 4********/
    function openForm4() {
      document.getElementById("myWidget4").style.display = "block";
    }
    
    function submitForm4() {
        document.getElementById("myWidget4").style.display = "block";
    }
    
    function closeForm4() {
      document.getElementById("myWidget4").style.display = "none";
    }
    /********END WIDGET 4*********/

/****  JS FOR COUNTRIES APP *************************/  

// Global Variables
const countriesList = document.getElementById("countries");
let countries; // will contain "fetched" data

// Event Listeners
// countriesList.addEventListener("change", event => displayCountryInfo(event.target.value));

countriesList.addEventListener("change", newCountrySelection);

function newCountrySelection(event) {
  displayCountryInfo(event.target.value);
}

// Fetches data from json in url //

fetch("https://restcountries.eu/rest/v2/all")
.then(res => res.json())
.then(data => initialize(data))
.catch(err => console.log("Error:", err));


// Sets data into json file
function initialize(countriesData) {
  countries = countriesData;
  let options = "";
  // for(let i=0; i<countries.length; i++) {
  //   options += `<option value="${countries[i].alpha3Code}">${countries[i].name}</option>`;
  //   // options += `<option value="${countries[i].alpha3Code}">${countries[i].name} (+${countries[i].callingCodes[0]})</option>`;
  // }
  countries.forEach(country => options+=`<option value="${country.alpha3Code}">${country.name}</option>`);
 
  countriesList.innerHTML = options;
  
  // Sets opening display to a random country with its data
  countriesList.selectedIndex = Math.floor(Math.random()*countriesList.length);
  displayCountryInfo(countriesList[countriesList.selectedIndex].value);
}
// Gathers specific data for country specified by country code and returns to frontend
function displayCountryInfo(countryByAlpha3Code) {
  const countryData = countries.find(country => country.alpha3Code === countryByAlpha3Code);
  document.querySelector("#flag-container img").src = countryData.flag;
  document.querySelector("#flag-container img").alt = `Flag of ${countryData.name}`;  
  document.getElementById("capital").innerHTML = countryData.capital;
  document.getElementById("languages").innerHTML = countryData.languages.filter(l => l.name).map(l => `${l.name} (${l.iso639_1})`).join(", ");
  document.getElementById("dialing-code").innerHTML = `+${countryData.callingCodes[0]}`;
  document.getElementById("population").innerHTML = countryData.population.toLocaleString("en-US");
  document.getElementById("currencies").innerHTML = countryData.currencies.filter(c => c.name).map(c => `${c.name} (${c.code})`).join(", ");
  document.getElementById("region").innerHTML = countryData.region;
  document.getElementById("subregion").innerHTML = countryData.subregion;
}

/*************END HOME PAGE BOTTOM WIDGET SCRIPTS***************/



/*  JS for the BudgetApp Application  */

(function(){

    document.querySelector('#categoryInput').addEventListener('keydown', function(e){
        if (e.keyCode != 13){
            return;
        }

        e.preventDefault()

        var categoryName = this.value
        this.value = ''
        addNewCategory(categoryName)
        updateCategoriesString()
    })

    function addNewCategory(name){

        document.querySelector('#categoriesContainer').insertAdjacentHTML('beforeend',
        `<li class="category">
            <span class="name">${name}</span>
            <span onclick="removeCategory(this)" class="btnRemove bold">X</span>
        </li>`)
    }

    

})()

function fetchCategoryArray(){
    var categories = []

    document.querySelectorAll('.category').forEach(function(e){
        name = e.querySelector('.name').innerHTML
        if (name == '') return

        categories.push(name)
    })

    return categories
}

function updateCategoriesString(){
    categories = fetchCategoryArray()
    document.querySelector('input[name="categoriesString"]').value = categories.join(',')

} 

function removeCategory(e){
    e.parentElement.remove()
    updateCategoriesString()
}

